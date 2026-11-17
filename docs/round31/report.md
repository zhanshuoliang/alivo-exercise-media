# Round 31 — 15 exercises × 4 tracks

Date: 2026-11-17. Result: **60/60 images passed visual review on first generation (zero rework)** — second consecutive clean round after Round 30.

## Selection

Band ×5 + assisted machine ×2 + leverage machine ×3 + cable ×5 (first cable bucket round; assisted entries are machine-assisted, solo-depictable — partner-assisted entries remain deferred).

| catalogId | name | equipment |
|---|---|---|
| exercises-dataset:0984 | band lying hip internal rotation | band |
| exercises-dataset:0987 | band one arm single leg split squat | band |
| exercises-dataset:0994 | band reverse wrist curl | band |
| exercises-dataset:0999 | band single leg calf raise | band |
| exercises-dataset:1011 | band seated twist | band |
| exercises-dataset:0015 | assisted parallel close grip pull-up | assisted (machine) |
| exercises-dataset:0019 | assisted triceps dip (kneeling) | assisted (machine) |
| exercises-dataset:1479 | lever incline chest press v. 2 | leverage machine |
| exercises-dataset:3200 | lever bent-over row with v-bar | leverage machine |
| exercises-dataset:0582 | lever kneeling leg curl | leverage machine |
| exercises-dataset:0007 | alternate lateral pulldown | cable |
| exercises-dataset:0151 | cable bench press | cable |
| exercises-dataset:0167 | cable high row (kneeling) | cable |
| exercises-dataset:1632 | cable drag curl | cable |
| exercises-dataset:0162 | cable front raise | cable |

Planning note: `exercises-dataset:0578` (lever deadlift) was dropped during selection — its source instructions describe a seated leg-press-like movement too close to already-bound `2611`; replaced with `0582` lever kneeling leg curl.

## Generation

- `make_prompts_r31.cjs` → 60 prompts (`prompts31_m/f/open_m/open_f`), `plan_round31.json`, `batch_round31.json`
- `launch31.sh` — two waves ×30 (branded m/f, then open m/f), `codex exec` with gender reference images for branded tracks only; open tracks reference-free
- `collect31.cjs` → `copied 60, missing 0, suspect 0` on first pass
- Zero network failures this round (vs. 3 retries in r29, 1 wrong-image rework in r28)

## Review notes

All 15 groups × 4 tracks verified: correct exercise depiction, equipment, single athlete, full-body framing, one small ALIVO mark on branded tracks, none on open tracks, no split/collage layouts, no anatomy/equipment errors.

Notable frames: 0984 supine knees-rotating-outward hip rotation; 0007 alternating pulldown mid-switch (one elbow down, other arm extended); 1310-style timing not needed this round — all standard positions cleanly depicted.

Minor observations (accepted, not reworked): 0994 open-male band rendered red (color is a free variable); assisted machine designs vary slightly across tracks but all show kneeling pad + parallel grips consistent with the exercise.

## Integration

- **Male branded**: packaged to `new/` → 1024px WebP q82/m4, bound in both app bundles (`entry/.../rawfile/` + `mobile/alivo_app/assets/catalog/`). Media bindings 585 → **600**. Both metadata files byte-identical; 600 webp each side, zero byte-diff.
- **Female branded ×15 + male masters ×15** → `media/` (total **870** PNG)
- **Open ×30** → `media-open/` (total **658** PNG); `manifest.json` 628 → **658** records (CC-BY-4.0, SHA-256 each)
- NOTICE: Round 31 sections appended to `media/NOTICE.md` + `media-open/NOTICE.md` with per-file SHA-256; `make_notice31.cjs` now idempotent (skips existing manifest files / NOTICE headings — fixes the r30 double-append bug class)
- PROVENANCE.csv + exercise_media_test.dart updated in both app bundles via `integrate31.cjs`

## Archives

- `prompts/prompts31_{m,f,open_m,open_f}/` — 60 prompt files
- `plan_round31.json`, `batch_round31.json`, `manifest_round31.json`
- `make_prompts_r31.cjs`, `launch31.sh`, `collect31.cjs`, `integrate31.cjs`, `make_notice31.cjs`

## Regression

- Node `tests/regression.cjs`: pending at report time (see main repo commit note)
- Flutter exercise-media test: pending
- Catalog review page rebuilt and deployed via GitHub Pages
