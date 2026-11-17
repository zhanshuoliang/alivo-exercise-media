# Round 59 — branded-only batch (2026-11-17)

## Selection
15 semantically-screened exercises (dup-normalized name check vs bound list + step review):

| catalogId | exercise | track |
|---|---|---|
| exercises-dataset:1673 | dumbbell preacher curl over exercise ball | M bound / F retained |
| exercises-dataset:1294 | dumbbell pullover hip extension on exercise ball | M bound / F retained |
| exercises-dataset:1746 | exercise ball supine triceps extension | M bound / F retained |
| exercises-dataset:1734 | dumbbell kickbacks on exercise ball | M bound / F retained |
| exercises-dataset:3546 | dumbbell seated alternate shoulder | M bound / F retained |
| exercises-dataset:1725 | cable rope incline tricep extension | M bound / F retained |
| exercises-dataset:1726 | cable rope lying on floor tricep extension | M bound / F retained |
| exercises-dataset:3218 | hands clasped circular toe touch | M bound / F retained |
| exercises-dataset:0492 | incline push up depth jump | M bound / F retained |
| exercises-dataset:0730 | single leg platform slide | M bound / F retained |
| exercises-dataset:3318 | swing 360 | M bound / F retained |
| exercises-dataset:1355 | one arm against wall | M bound / F retained |
| exercises-dataset:0570 | leg pull in flat bench | M bound / F retained |
| exercises-dataset:2802 | twisted leg raise | M bound / F retained |
| exercises-dataset:3433 | swimmer kicks v. 2 | M bound / F retained |

## Review
- 30/30 images accepted after rework of item 2802 (twisted leg raise): first two
  attempts showed a plain leg raise without visible hip rotation; the third
  generation (feet-end three-quarter camera, legs tilted to one side with pelvis
  rolled) clearly depicts the twist and passed both tracks.
- All other 14 pairs passed first-review: single athlete, correct movement
  signature, complete framing, single ALIVO wordmark, no extra text.

## Integration
- 15 male WebP (1024x1024, q82, m4) bound into both bundles
  (entry rawfile + Flutter assets/catalog); metadata, NOTICE.md, PROVENANCE.csv
  identical across platforms; regression assertions added per record.
- 15 female + 15 male PNGs archived under `media/` (total 1710 PNG); media/
  NOTICE.md Round-59 section appended with per-file SHA-256.
- Bound count: 1005 -> 1020 of 1352 (remaining 332).
- `exercises-dataset:3562` remains deliberately unbound (conflicting hip-thrust
  identity per regression blacklist).
- catalog-review.html rebuilt: 1352 records, all 15 new slugs marked bound.

## Testing
- Node regression: 777/777 pass.
- Flutter media tests: 7/7 pass (bundled-record assertions chunked at 400/test after the asset-bundle mock hit a ~960-load stack limit; coverage unchanged).
