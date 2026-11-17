# Round 35 — branded-only edition (2026-11-17)

15 exercises × 2 branded tracks = **30 images; 30/30 passed visual review** (1 exec-layer retry: job replied without generating; single re-run produced the image). Open track paused — `media-open/` unchanged this round.

## Selection (dumbbell ×5 + body weight ×5 + cable ×3 + barbell ×2)

| catalogId | exercise | equipment |
|---|---|---|
| exercises-dataset:2136 | dumbbell cuban press | dumbbell |
| exercises-dataset:0864 | dumbbell upright shoulder external rotation | dumbbell |
| exercises-dataset:0438 | dumbbell w-press | dumbbell |
| exercises-dataset:0777 | spell caster | dumbbell |
| exercises-dataset:3635 | dumbbell contralateral forward lunge | dumbbell |
| exercises-dataset:1297 | isometric chest squeeze | body weight |
| exercises-dataset:3663 | reverse plank with leg lift | body weight |
| exercises-dataset:3667 | side lying hip adduction | body weight |
| exercises-dataset:0795 | standing single leg curl | body weight |
| exercises-dataset:1362 | sphinx | body weight |
| exercises-dataset:0188 | cable middle fly | cable |
| exercises-dataset:0230 | cable standing lift | cable |
| exercises-dataset:0873 | cable reverse crunch | cable |
| exercises-dataset:1462 | barbell full squat (side pov) | barbell |
| exercises-dataset:0788 | standing behind neck press | barbell |

## Selection notes

- `0870` butt-ups dropped — steps overlap bound `reverse_crunch`; replaced by `1362` sphinx.
- `3635` contralateral lunge rendered with ONE dumbbell in the hand opposite the lead leg (name semantics; dataset steps mentioning both hands are generic).
- `2429` frog crunch skipped — dataset steps are a generic crunch description, too close to bound `floor_crunch`.

## Incidents

- **`1462` male exec-layer miss.** First run's codex exec session returned "What would you like me to do with this image?" without invoking the image tool (no moderation, no error). Re-launched the same prompt file; image produced normally and passed review.

## Integration

- **Male branded** bound into both app bundles: `exercise_metadata.json` media records 645 → **660**; 15 WebP 1024px q82/method4, byte-identical across `entry/.../rawfile` and `mobile/.../catalog`; NOTICE/PROVENANCE/`exercise_media_test.dart` updated together.
- **Male masters + female variants** archived to `media/` (**990 PNG** total); `media/NOTICE.md` Round 35 section with SHA-256 for all 30 files.
- `media-open/` untouched (manifest stays at 688).

## Verification

- Dual-bundle metadata equal; 0 duplicate catalogIds/paths/hashes; all 15 new WebP byte-identical.
- Node regression and Flutter media tests run post-integration (see commit notes).
- `catalog/` snapshot synced; `catalog-review.html` rebuilt.
