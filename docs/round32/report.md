# Round 32 — 15 exercises × 4 tracks

Date: 2026-11-17. Result: **60/60 images passed visual review on first generation (zero rework)** — third consecutive clean round (r30, r31, r32).

## Selection

Band ×5 + assisted machine ×1 + leverage machine ×4 + cable ×5. Band bucket reduced to 4 remaining near-duplicate/deferred entries after this round; assisted partner-dependent entries remain deferred.

| catalogId | name | equipment |
|---|---|---|
| exercises-dataset:3117 | band fixed back close grip pulldown | band |
| exercises-dataset:3116 | band fixed back underhand pulldown | band |
| exercises-dataset:0983 | band kneeling one arm pulldown | band |
| exercises-dataset:0996 | band seated hip internal rotation | band |
| exercises-dataset:1007 | band standing twisting crunch | band |
| exercises-dataset:1431 | assisted standing chin-up | assisted (machine) |
| exercises-dataset:0573 | lever back extension | leverage machine |
| exercises-dataset:1253 | lever donkey calf raise | leverage machine |
| exercises-dataset:3195 | lever lying two-one leg curl | leverage machine |
| exercises-dataset:1356 | lever one arm lateral high row | leverage machine |
| exercises-dataset:0148 | cable alternate shoulder press | cable |
| exercises-dataset:0149 | cable alternate triceps extension | cable |
| exercises-dataset:0150 | cable bar lateral pulldown | cable |
| exercises-dataset:0154 | cable cross-over reverse fly | cable |
| exercises-dataset:0157 | cable deadlift | cable |

Differentiation notes: 3117 seated close-grip vs 3116 standing underhand pulldown; 0996 seated hip internal rotation vs prior 0984 lying variation; 1431 standing assist platform vs prior 0015 kneeling assist; 1253 lever hip-pad donkey raise vs prior 0833 plate-on-back variant; 1356 single-arm high row vs prior 3200 V-bar two-arm row.

## Generation

- `make_prompts_r32.cjs` → 60 prompts (`prompts32_m/f/open_m/open_f`), `plan_round32.json`, `batch_round32.json`
- `launch32.sh` — two waves ×30 (branded m/f, then open m/f), gender reference images for branded tracks only; open tracks reference-free
- `collect32.cjs` → `copied 60, missing 0, suspect 0` on first pass
- Zero network failures, zero wrong-image incidents — cleanest pipeline run to date

## Review notes

All 15 groups × 4 tracks verified: correct exercise depiction, equipment, single athlete, full-body framing, one small ALIVO mark on branded tracks, none on open tracks, no split/collage layouts, no anatomy/equipment errors.

Notable frames: 3117 seated close-grip pulldown to chest; 1431 standing assist-platform chin-up with weight stack (clearly distinct from 0015 kneeling version); 1253 donkey calf raise at top position with lever pad on hips; 0154 cross-over reverse fly mid-retraction between dual towers; 0157 cable deadlift at lockout with flat back.

## Integration

- **Male branded**: packaged to `new/` → 1024px WebP q82/m4, bound in both app bundles (`entry/.../rawfile/` + `mobile/alivo_app/assets/catalog/`). Media bindings 600 → **615**. Both metadata files byte-identical; 615 webp each side, zero byte-diff.
- **Female branded ×15 + male masters ×15** → `media/` (total **900** PNG)
- **Open ×30** → `media-open/` (total **688** PNG); `manifest.json` 658 → **688** records (CC-BY-4.0, SHA-256 each)
- NOTICE: Round 32 sections appended to `media/NOTICE.md` + `media-open/NOTICE.md` with per-file SHA-256; `make_notice32.cjs` inherits r31 idempotence
- PROVENANCE.csv + exercise_media_test.dart updated in both app bundles via `integrate32.cjs` (marker = r31 tail entry `0162`)

## Archives

- `prompts/prompts32_{m,f,open_m,open_f}/` — 60 prompt files
- `plan_round32.json`, `batch_round32.json`, `manifest_round32.json`
- `make_prompts_r32.cjs`, `launch32.sh`, `collect32.cjs`, `integrate32.cjs`, `make_notice32.cjs`

## Regression

- Node `tests/regression.cjs`: pending at report time (see main repo commit note)
- Flutter exercise-media test: pending
- Catalog review page rebuilt and deployed via GitHub Pages
