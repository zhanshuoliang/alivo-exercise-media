"""One-shot, guarded integration of three visually reviewed round-eight stills."""
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
APP = Path('D:/codex-temp/alivo')
MEDIA = Path('D:/codex-temp/alivo-exercise-media')
GENERATED = Path('C:/Users/Paul/.codex/generated_images/01a1bfc8-05ed-7822-ba35-20f05b5d62af')
ROOTS = [APP / 'entry/src/main/resources/rawfile', APP / 'mobile/alivo_app/assets/catalog']
TARGETS = [
    ('1004', 'band_squat.png', 'exec-3c56ed7f-58e9-432f-97fe-3b650662dd98.png'),
    ('1408', 'band_hip_lift.png', 'exec-bbba3726-36a6-445e-98f2-49a1cf005f90.png'),
    ('3006', 'resistance_band_seated_hip_abduction.png', 'exec-b69cb945-c756-4dd7-ae40-ee19f00fca05.png'),
]


def check(condition, message):
    if not condition:
        raise ValueError(message)


for repo in (APP, MEDIA):
    state = subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain=v1']).decode()
    check(not state, 'Concurrent edits found; preserve them and stop integration: ' + str(repo) + '\n' + state)

writes = []


def prepare(path, data):
    writes.append((path, path.read_bytes() if path.exists() else None, data))


old_meta = (ROOTS[0] / 'exercise_metadata.json').read_bytes()
old_notice = (ROOTS[0] / 'exercise_media/NOTICE.md').read_bytes()
for root in ROOTS[1:]:
    check((root / 'exercise_metadata.json').read_bytes() == old_meta, 'Metadata already differs')
    check((root / 'exercise_media/NOTICE.md').read_bytes() == old_notice, 'NOTICE already differs')
check((MEDIA / 'catalog/exercise_metadata.json').read_bytes() == old_meta, 'Snapshot metadata differs')
check((MEDIA / 'media/NOTICE.md').read_bytes() == old_notice, 'Snapshot NOTICE differs')
metadata = json.loads(old_meta)
ids = {row['catalogId'] for row in metadata['media']}
paths = {row['localPath'] for row in metadata['media']}
hashes = {row['sha256'] for row in metadata['media']}
catalog = {row['id']: row for row in json.loads((ROOTS[0] / 'exercises_zh.json').read_text('utf-8'))}
overrides = {row['catalogId']: row for row in metadata['overrides']}
records = []
selection = []
for identity, filename, source in TARGETS:
    cid, local = 'exercises-dataset:' + identity, 'exercise_media/' + filename
    data = (GENERATED / source).read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    check(cid not in ids and local not in paths and digest not in hashes, 'Duplicate binding: ' + cid)
    check(data.startswith(b'\x89PNG\r\n\x1a\n'), 'Not PNG: ' + source)
    check(identity in catalog, 'Unknown catalog identity')
    row = dict(catalogId=cid, sourceRecordId='alivo:editorial:' + filename, localPath=local,
               sourceUrl='https://openai.com/policies/terms-of-use/', author='ALIVO',
               license='ALIVO-editorial', licenseUrl='https://openai.com/policies/terms-of-use/',
               changes='ALIVO 原创彩色编辑插图，服装带 ALIVO 品牌字标',
               sha256=digest, reviewedAt='2026-11-09')
    records.append(row)
    selection.append(dict(catalogId=cid, name=catalog[identity]['nz'], filename=filename,
                          equipment=catalog[identity]['eq'],
                          instructionSteps=overrides.get(cid, {}).get('instructionSteps', catalog[identity]['st']),
                          instructionSource='metadata.instructionSteps' if 'instructionSteps' in overrides.get(cid, {}) else 'catalog.st (no maintained override)',
                          generatedSource=source, reviewStatus='accepted', sha256=digest))
    for destination in [root / local for root in ROOTS] + [MEDIA / 'media' / filename]:
        check(not destination.exists(), 'Existing asset would be overwritten: ' + str(destination))
        prepare(destination, data)

text = old_meta.decode('utf-8')
eol = '\r\n' if '\r\n' in text else '\n'
at = text.rfind(eol + '  ]')
check(at >= 0, 'Metadata media array marker missing')
insert = (',' + eol).join(eol.join('    ' + line for line in json.dumps(row, ensure_ascii=False, indent=2).splitlines()) for row in records)
new_text = text[:at].rstrip() + ',' + eol + insert + text[at:]
expected = dict(metadata, media=metadata['media'] + records)
check(json.loads(new_text) == expected, 'Append affected non-media metadata')
notice_eol = '\r\n' if b'\r\n' in old_notice else '\n'
notice = old_notice.decode('utf-8').rstrip() + notice_eol * 2
notice += '## ALIVO editorial gap-fill illustrations — round 8, 2026-11-09' + notice_eol * 2
notice += 'ALIVO 编辑插图，非动作教学示范。Generated specifically for ALIVO with OpenAI ImageGen.' + notice_eol * 2
notice += notice_eol.join('- `' + row['localPath'] + '` — `' + row['catalogId'] + '`; SHA-256 `' + row['sha256'] + '`.' for row in records) + notice_eol
for destination in [root / 'exercise_metadata.json' for root in ROOTS] + [MEDIA / 'catalog/exercise_metadata.json']:
    prepare(destination, new_text.encode('utf-8'))
for destination in [root / 'exercise_media/NOTICE.md' for root in ROOTS] + [MEDIA / 'media/NOTICE.md']:
    prepare(destination, notice.encode('utf-8'))

for relative, marker, additions in [
    ('mobile/alivo_app/test/exercise_media_test.dart', '    for (final entry in {',
     ['      \'exercises-dataset:' + identity + '\': \'' + filename + '\',' for identity, filename, _ in TARGETS]),
    ('tests/regression.cjs', '  for (const [id, file] of [',
     ['    [\'exercises-dataset:' + identity + '\', \'' + filename + '\'],' for identity, filename, _ in TARGETS]),
]:
    path = APP / relative
    original = path.read_bytes().decode('utf-8')
    check(original.count(marker) == 1, 'Ambiguous test marker: ' + relative)
    end = '\r\n' if '\r\n' in original else '\n'
    prepare(path, original.replace(marker, marker + end + end.join(additions), 1).encode('utf-8'))

doc_root = MEDIA / 'docs/round8'
for filename, data in [('accepted.json', records), ('selection.json', selection)]:
    prepare(doc_root / filename, (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
prepare(doc_root / 'prompts.json', (HERE / 'prompts.json').read_bytes())
prepare(MEDIA / 'tools/audit_media.py', (HERE / 'audit_media.py').read_bytes())
prepare(doc_root / 'integrate_round8.py', Path(__file__).read_bytes())
prepare(doc_root / 'review.md', (HERE / 'review.md').read_bytes())

# Check every original again before the first mutation.
for path, original, _ in writes:
    check((path.read_bytes() if path.exists() else None) == original, 'Concurrent file change: ' + str(path))
for path, _, data in writes:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
print(json.dumps(dict(newCount=len(records), priorCount=len(metadata['media']), records=records), ensure_ascii=True, indent=2))
