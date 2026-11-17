# Round 38 Report — 2026-11-17

## Scope
- 15 exercises × 2 branded tracks (male + female ALIVO) = 30 PNGs.
- Male branded track bound into both app bundles (HarmonyOS + Flutter).
- Female branded track retained in `media/` unbound.
- Open/unbranded track remains paused (manifest stays at 688).

## Selection (from 653 unbound candidates)
- dumbbell ×4: `0286` alternate side press, `1646` alternate hammer preacher curl, `0306` decline triceps extension, `0311` full can lateral raise
- body weight ×5: `0137` body-up, `2466` bridge mountain climber (cross body), `0258` clock push-up, `3544` bodyweight incline side plank, `3204` arms overhead full sit-up
- cable ×3: `0153` cross-over lateral pulldown, `0171` incline fly, `0172` incline pushdown
- leverage ×2: `0590` one arm shoulder press, `2315` rotary calf
- smith ×1: `1396` smith toe raise

## Screening notes
- `0138` bottoms-up excluded — steps duplicate bound reverse-crunch semantics.
- `0578` lever deadlift excluded — dataset steps describe a seated press machine, contradicting the name.
- `0578` replaced by `0590` lever one arm shoulder press; `0138` replaced by `3544`/`3204` bodyweight entries.
- `3204` filename kept as `arms_overhead_full_sit_up` base (dataset "(male)" suffix handled by variant naming).

## Generation & review
- 30 exec tasks (15 male + 15 female branded), single wave via `launch38.sh`.
- Collected via `collect38.cjs`: copied 30, missing 0, suspect 0.
- Visual pair review: **30/30 accepted on first pass, zero regenerations.**

## Integration
- `integrate38.cjs batch_round38.json --apply`: 15 new WebP records (1024px, q82, method 4) written to both app bundles.
- Bound count: 690 → **705**.
- Dual-bundle verification: counts 705/705, duplicate ids/paths/hashes 0, byte-diff 0.
- `media/` PNG count: 1050 → **1080**.
- `media/NOTICE.md` Round 38 section appended (dedup-checked, 15 rows ×2).
- `catalog/exercise_metadata.json` synced from app metadata snapshot.
- `catalog-review.html` rebuilt (1,352 records) — all 15 round-38 records present with both tracks.
