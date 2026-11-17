# Round 41 — branded-only batch（男带标绑定 + 女带标入库）

- Date: 2026-11-17
- Tracks: branded male (bound to App) + branded female (media repo only). Open/unbranded track paused.
- Result: **30/30 images passed visual review — 1 in-pool replacement, 0 image regenerations**.

## Selected (15)

| catalogId | exercise | equipment |
|---|---|---|
| exercises-dataset:1000 | band single leg reverse calf raise | band |
| exercises-dataset:1001 | band single leg split squat | band |
| exercises-dataset:1369 | band two legs calf raise v. 2 | band |
| exercises-dataset:1016 | band wrist curl | band |
| exercises-dataset:0844 | weighted round arm | weighted (dumbbell) |
| exercises-dataset:0193 | cable one arm straight back high row (kneeling) | cable |
| exercises-dataset:1754 | weighted three bench dips | weighted |
| exercises-dataset:1313 | lever unilateral row | leverage machine |
| exercises-dataset:1301 | machine inner chest press | leverage machine |
| exercises-dataset:0600 | lever seated leg raise crunch | leverage machine |
| exercises-dataset:2288 | lever gripper hands | leverage machine |
| exercises-dataset:0055 | barbell lying close-grip press | barbell |
| exercises-dataset:0073 | barbell pullover | barbell |
| exercises-dataset:0068 | barbell one leg squat | barbell |
| exercises-dataset:0040 | barbell front raise and pullover | barbell |

## Notes

- `2371` weighted russian twist v. 2 was replaced by `0193` at integration time: its slug collided with already-bound `0846` weighted_russian_twist (v.1) and it is a near-duplicate anyway. `0193` images were generated after the batch and passed review.
- `1301` female track: the `ALIVO` wordmark is partially occluded by the forearm crossing the chest; spelling is correct where visible — accepted, logged.
- `1754` depicted as classic weighted bench dip: hands on rear bench, feet on front bench, plate on lap.
- Band bucket (4/4 remaining) is now exhausted; weighted bucket leaves `3641`/`3313`.

## Review log

All 15 pairs reviewed visually: exercise posture/equipment, grip, anatomy, framing, `ALIVO` spelling, single-frame constraints. 30/30 pass.

## Integration

- App bundles: 735 → **750** bound records (HarmonyOS + Flutter identical WebP q82/m4, byte-diff 0).
- Metadata count: 750/750 both platforms; duplicate ids/paths/hashes: 0.
- `media/` PNG masters: 1,140 → **1,170**.
- `media/NOTICE.md`: Round 41 section appended (15 rows × 2 tracks, SHA-256 recorded).
- `catalog/exercise_metadata.json` synced; `catalog-review.html` rebuilt (1,352 records).
- Archive: `docs/round41/` contains prompts_m/, prompts_f/, plan/batch/manifest JSON, scripts and this report.

## Excluded (pool-side)

- `exercises-dataset:2371` weighted russian twist v. 2 — filename collision + near-duplicate of bound `0846`.
- `exercises-dataset:3313` weighted straight bar dip — crowded dip family.
