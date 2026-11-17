# Round 60 — branded-only edition (2026-11-17)

Progress: **1020 → 1035 / 1352** bindable branded catalog records.

## Selection

15 records, chosen from the normalized-name-cleaned unbound pool (semantic collision
screening against all previously bound records; forbidden/conflicting identity
`exercises-dataset:3562` remains unbound by design):

| catalogId | exercise | equipment |
|---|---|---|
| `exercises-dataset:2400` | inverse leg curl (on pull-up cable machine) | cable |
| `exercises-dataset:3167` | bodyweight squatting row (with towel) | body weight |
| `exercises-dataset:3165` | bodyweight standing row (with towel) | body weight |
| `exercises-dataset:1773` | one arm towel row | body weight |
| `exercises-dataset:0651` | pull up (neutral grip) | body weight |
| `exercises-dataset:3315` | full maltese | body weight |
| `exercises-dataset:1656` | dumbbell biceps curl v sit on bosu ball | dumbbell |
| `exercises-dataset:1649` | dumbbell alternating bicep curl with leg raised on exercise ball | dumbbell |
| `exercises-dataset:1652` | dumbbell bicep curl on exercise ball with leg raised | dumbbell |
| `exercises-dataset:0427` | dumbbell standing palms in press | dumbbell |
| `exercises-dataset:1382` | exercise ball on the wall calf raise | dumbbell |
| `exercises-dataset:0709` | side hip (on parallel bars) | body weight |
| `exercises-dataset:3291` | stalder press | body weight |
| `exercises-dataset:1427` | straight leg outer hip abductor | body weight |
| `exercises-dataset:3213` | side-to-side toe touch (male) | body weight |

## Generation

- 30 images (15 Kai male + 15 Liv female branded variants), photorealistic-natural
  editorial style, neutral gray studio, single small white `ALIVO` wordmark.
- All 30 final images passed semantic review.
- **Late swap:** `free-exercise-db:Kettlebell_Halo_With_Overhead_Extension` was
  generated and briefly bound, then removed — `tests/regression.cjs` asserts that
  catalog identity must remain media-less (its canonical sibling `Kettlebell_Halo`
  is already bound). Replaced by `exercises-dataset:1382` exercise ball on the
  wall calf raise, generated and reviewed as a clean substitute. The KB images
  were deleted from `media/` and its NOTICE rows retracted.
- Male WebP (1024px, q82, method 4) bound into both app bundles
  (`entry/src/main/resources/rawfile`, `mobile/alivo_app/assets/catalog`).
- Female PNGs retained in `media/` only (not bound).

## Verification

- `exercise_metadata.json` identical across both platform roots; 1035 media records.
- No duplicate `localPath` / `sha256` / `catalogId`; `3562` and the KB supplement
  identity both remain unbound.
- `NOTICE.md` / `PROVENANCE.csv` byte-identical across platforms; 1035 WebP each side.
- `catalog/exercise_metadata.json` + `tools/catalog_snapshot.json` synced to 1035.
- `catalog-review.html` rebuilt: 1352 records, all 15 Round-60 slugs bound-marked.
- Backend regression `node --test tests/regression.cjs`: **777/777 pass**.
- Flutter `flutter test`: **7/7 pass** (asset checks kept in split `test()` blocks
  to stay under the platform's sequential `rootBundle` resource-stack limit).

## Files

- `plan_round60.json`, `batch_round60.json` — selection + binding manifest.
- `media/` — 1740 PNGs (30 new) + `NOTICE.md` Round-60 section (30 sha256 rows).
