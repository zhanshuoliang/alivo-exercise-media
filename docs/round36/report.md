# Round 36 — branded-only edition

Date: 2026-11-17

## Scope

15 exercises × 2 branded tracks (male + female) = 30 PNGs. Open/unbranded track remains paused (deferred to a later independent phase).

- Male branded: bound into both app bundles (HarmonyOS rawfile + Flutter assets), 660 → **675** of 1,352.
- Female branded: archived in `media/` only, not bound.
- Male PNG masters: archived in `media/`.

## Selected exercises

| catalogId | name | bucket |
|---|---|---|
| exercises-dataset:0178 | cable lateral raise | cable |
| exercises-dataset:0202 | cable rear delt row | cable |
| exercises-dataset:0216 | cable seated shoulder internal rotation | cable |
| exercises-dataset:0228 | cable standing hip extension | cable |
| exercises-dataset:0240 | cable supine reverse fly | cable |
| exercises-dataset:0288 | dumbbell around pullover | dumbbell |
| exercises-dataset:0291 | dumbbell bench squat | dumbbell |
| exercises-dataset:2706 | dumbbell lying supination on floor | dumbbell |
| exercises-dataset:0411 | dumbbell single leg squat | dumbbell |
| exercises-dataset:1743 | dumbbell twisting bench press | dumbbell |
| exercises-dataset:3671 | ski step | body weight |
| exercises-dataset:3672 | back and forth step | body weight |
| exercises-dataset:3645 | single leg bridge with outstretched leg | body weight |
| exercises-dataset:0778 | spider crawl push up | body weight |
| exercises-dataset:0691 | seated side crunch | body weight |

## Review

30/30 passed visual review on first generation — zero retries.

- 0178 cable lateral raise: rear view facing away from low pulley, arm raised laterally to shoulder height.
- 0202 cable rear delt row: staggered stance, elbow flared pulling stirrup handle to chest.
- 0216 seated internal rotation: seated, handle pulled inward at rotated finish.
- 0228 standing hip extension: ankle cuff, leg extended back, holding upright for balance.
- 0240 supine reverse fly: prone on flat bench between two low pulleys, arms swept out.
- 0288 pullover: supine on bench, one dumbbell two-handed, arms stretched behind head.
- 0291 bench squat: hips lowered to touch bench, dumbbells hanging at sides.
- 2706 lying supination: supine on floor, dumbbells curled toward shoulders.
- 0411 single leg squat: loaded single-leg squat bottom, free leg extended forward.
- 1743 twisting bench press: flat bench, dumbbells at bottom with palms rotated inward.
- 3671 ski step: mid lateral hop, single-foot landing with trailing leg behind.
- 3672 back and forth step: forward lunge, hands on hips, upright torso.
- 3645 single leg bridge: hips lifted in line, one leg extended vertical.
- 0778 spider crawl push up: push-up bottom, knee driven toward same-side elbow.
- 0691 seated side crunch: seated against wall, hands behind head, lateral crunch.

## Packaging

- 15 male WebP at 1024×1024, quality 82, method 4 — byte-identical in both app bundles.
- `exercise_metadata.json` media records: 675 entries each end, no duplicate catalogIds/paths/sha256.
- NOTICE / PROVENANCE / `exercise_media_test.dart` appended on both platforms.
- `media/NOTICE.md` Round 36 section with SHA-256 for all 30 PNGs.
- `media/` PNG count: **1020**. `media-open/` unchanged at 688 manifest records.

## Verification

- Node regression `tests/regression.cjs`: 777/777 pass.
- Flutter `exercise_media_test.dart`: 5/5 pass.
- `catalog-review.html` rebuilt with Round 36 records; JS parses clean.
