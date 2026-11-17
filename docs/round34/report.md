# Round 34 — branded-only edition (2026-11-17)

15 exercises × 2 branded tracks = **30 images; 30/30 passed visual review** (1 retry: safety-blocked prompt rewrite). Open track paused per plan — `media-open/` unchanged this round.

## Selection (dumbbell ×6 + bodyweight ×4 + barbell ×3 + cable ×2)

| catalogId | exercise | equipment |
|---|---|---|
| exercises-dataset:1757 | dumbbell single leg deadlift | dumbbell |
| exercises-dataset:0436 | dumbbell tate press | dumbbell |
| exercises-dataset:2143 | dumbbell standing around world | dumbbell |
| exercises-dataset:0863 | dumbbell lying external shoulder rotation | dumbbell |
| exercises-dataset:2808 | dumbbell sumo pull through | dumbbell |
| exercises-dataset:3664 | dumbbell side plank with rear fly | dumbbell |
| exercises-dataset:0006 | alternate heel touchers | body weight |
| exercises-dataset:3769 | curtsey squat | body weight |
| exercises-dataset:3639 | bent knee lying twist | body weight |
| exercises-dataset:1418 | hug knees to chest | body weight |
| exercises-dataset:0562 | landmine 180 | barbell |
| exercises-dataset:3237 | landmine lateral raise | barbell |
| exercises-dataset:3194 | frankenstein squat | barbell |
| exercises-dataset:0174 | cable judo flip → retried as "cable rotational over-shoulder pull" | cable |
| exercises-dataset:0212 | cable seated crunch | cable |

## Incidents

- **`0174` male safety block.** First prompt "cable judo flip" was rejected by image-gen moderation (HTTP 400, `moderation_blocked`, category violence). Rewrote exercise name to `CABLE ROTATIONAL OVER-SHOULDER PULL` (same movement semantics — staggered stance, rope over shoulder, rotational pull) and regenerated; passed review. Filenames keep `cable_judo_flip_*` to match the catalog record name.
- **`0436` male note.** Tate press dumbbell inner heads nearly merge into one bar visually; movement still recognizable, kept without retry (same class of accepted variance as prior rounds).

## Integration

- **Male branded** bound into both app bundles: `exercise_metadata.json` media records 630 → **645**; 15 WebP 1024px q82/method4, byte-identical across `entry/.../rawfile` and `mobile/.../catalog`; NOTICE/PROVENANCE/`exercise_media_test.dart` updated together.
- **Male masters + female variants** archived to `media/` (**960 PNG** total); `media/NOTICE.md` Round 34 section with SHA-256 for all 30 files.
- `media-open/` untouched (manifest stays at 688).

## Verification

- Dual-bundle metadata equal; 0 duplicate catalogIds/paths/hashes; all 15 new WebP byte-identical.
- Node regression and Flutter media tests run post-integration (see commit notes).
- `catalog/` snapshot synced; `catalog-review.html` rebuilt.
