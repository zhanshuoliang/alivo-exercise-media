"""Audit both ALIVO bundles and this resource snapshot against an explicit Git baseline.

Usage: python -B tools/audit_media.py --app-root D:/codex-temp/alivo
       --baseline <commit> --expected docs/round8/accepted.json [--out result.json]
No fixed round number or historical media count is embedded in this audit.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--app-root', type=Path, required=True)
    parser.add_argument('--baseline', required=True)
    parser.add_argument('--expected', type=Path, required=True)
    parser.add_argument('--resource-root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    app, resource = args.app_root.resolve(), args.resource_root.resolve()
    roots = [app / 'entry/src/main/resources/rawfile', app / 'mobile/alivo_app/assets/catalog']

    def git(*command):
        return subprocess.check_output(['git', '-C', str(app), *command])

    baseline_commit = git('rev-parse', '--verify', args.baseline + '^{commit}').decode().strip()
    baseline_path = 'entry/src/main/resources/rawfile/'
    baseline_bytes = git('show', baseline_commit + ':' + baseline_path + 'exercise_metadata.json')
    baseline = json.loads(baseline_bytes)['media']
    prior = {item['catalogId']: item for item in baseline}
    require(len(prior) == len(baseline), 'Duplicate baseline identity')
    expected = json.loads(args.expected.read_text('utf-8-sig'))
    require(isinstance(expected, list), 'Expected bindings must be an array')
    require(len({x['catalogId'] for x in expected}) == len(expected), 'Duplicate expected identity')

    for name in ['exercise_metadata.json', 'exercise_measures.json']:
        files = [root / name for root in roots] + [resource / 'catalog' / name]
        require(all(p.read_bytes() == files[0].read_bytes() for p in files), name + ' bytes differ')
    notices = [root / 'exercise_media/NOTICE.md' for root in roots] + [resource / 'media/NOTICE.md']
    notice = notices[0].read_bytes()
    require(all(p.read_bytes() == notice for p in notices), 'NOTICE bytes differ')
    baseline_notice = git('show', baseline_commit + ':' + baseline_path + 'exercise_media/NOTICE.md')
    require(notice.replace(b'\r\n', b'\n').startswith(baseline_notice.replace(b'\r\n', b'\n').rstrip()),
            'Historical NOTICE content changed')

    catalog = {}
    for name, prefix in [('exercises_zh.json', 'exercises-dataset:'), ('exercises_extra.json', 'alivo:'),
                         ('exercises_reviewed.json', 'free-exercise-db:')]:
        documents = [json.loads((root / name).read_text('utf-8')) for root in roots]
        documents.append(json.loads((resource / 'catalog' / name).read_text('utf-8')))
        # Flutter intentionally omits legacy third-party im/gf references.
        normalized = [[{k: v for k, v in row.items() if k not in ('im', 'gf')} for row in doc]
                      for doc in documents]
        require(normalized[0] == normalized[1] == normalized[2], name + ' catalog data differ')
        for row in documents[0]:
            cid = prefix + row['id']
            require(cid not in catalog, 'Duplicate catalog identity: ' + cid)
            catalog[cid] = row

    current = json.loads((roots[0] / 'exercise_metadata.json').read_text('utf-8'))['media']
    ids, paths, hashes = set(), set(), set()
    by_id = {}
    notice_lines = notice.decode('utf-8').splitlines()
    for item in current:
        cid, local, digest = item['catalogId'], item['localPath'], item['sha256']
        require(cid in catalog and cid not in ids, 'Invalid or duplicate media identity: ' + cid)
        require(re.fullmatch(r'exercise_media/[a-z0-9_-]+\.(png|jpg)', local), 'Invalid path: ' + local)
        require(local not in paths and digest not in hashes, 'Duplicate path or image: ' + cid)
        require(item['license'] == 'ALIVO-editorial' and item['author'] == 'ALIVO', 'Attribution: ' + cid)
        require(item['sourceRecordId'] == 'alivo:editorial:' + Path(local).name, 'Source identity: ' + cid)
        require(re.fullmatch(r'[a-f0-9]{64}', digest), 'Invalid digest: ' + cid)
        files = [root / local for root in roots] + [resource / 'media' / Path(local).name]
        data = files[0].read_bytes()
        require(all(file.read_bytes() == data for file in files), 'Asset bytes differ: ' + local)
        require(sha(data) == digest, 'SHA-256 mismatch: ' + local)
        require(data.startswith(b'\x89PNG\r\n\x1a\n') or data.startswith(b'\xff\xd8\xff'), 'Invalid raster: ' + local)
        require(any(local in line and cid in line and digest in line for line in notice_lines), 'NOTICE row: ' + cid)
        require(not item.get('exerciseImageUrl') and not item.get('exerciseGifUrl'), 'Remote media URL: ' + cid)
        ids.add(cid); paths.add(local); hashes.add(digest); by_id[cid] = item
    for cid, item in prior.items():
        require(by_id.get(cid) == item, 'Historical binding changed or removed: ' + cid)
    additions = [item for item in current if item['catalogId'] not in prior]
    require(sorted(additions, key=lambda x: x['catalogId']) == sorted(expected, key=lambda x: x['catalogId']),
            'Actual new records differ from reviewed expected bindings')

    baseline_names = set(git('ls-tree', '--name-only', baseline_commit + ':' + baseline_path + 'exercise_media')
                         .decode().splitlines())
    allowed = baseline_names | {Path(item['localPath']).name for item in additions}
    for directory in [root / 'exercise_media' for root in roots] + [resource / 'media']:
        require({p.name for p in directory.iterdir() if p.is_file()} == allowed, 'Unexpected/missing files: ' + str(directory))
    legacy_names = baseline_names - {Path(item['localPath']).name for item in baseline} - {'NOTICE.md'}
    for name in legacy_names:
        old_bytes = git('show', baseline_commit + ':' + baseline_path + 'exercise_media/' + name)
        for directory in [root / 'exercise_media' for root in roots] + [resource / 'media']:
            require((directory / name).read_bytes() == old_bytes, 'Historical unbound asset changed: ' + name)

    sys.path.insert(0, str(resource / 'tools'))
    from motion_samples import load_motion_samples
    motions = load_motion_samples(resource)
    coverage = Counter(catalog[cid]['eq'] for cid in by_id)
    result = dict(baseline=baseline_commit, baselineCount=len(baseline), total=len(current),
                  priorPreserved=len(prior), newCount=len(additions), catalogCount=len(catalog),
                  platformAndSnapshotBytesEqual=True, metadataMeasuresAndNoticeEqual=True,
                  noticeRowsAndSha256Valid=True, noGifProductionBindings=True,
                  historicalUnboundFilesPreserved=sorted(legacy_names),
                  experimentalMotionSamplesVerified=len(motions), boundByEquipment=dict(coverage),
                  records=additions)
    text = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.out:
        args.out.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
