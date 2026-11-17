# Round 43 — 15 branded pairs, male track bound to app

Equipment split: small-bucket sweep (band x1 + kettlebell x1 + smith x2 + weighted x1) + dumbbell x6 + cable x4.

| ID | Exercise | Male | Female |
|----|----------|------|--------|
| exercises-dataset:1010 | band straight leg deadlift | pass | pass |
| exercises-dataset:0530 | kettlebell double windmill | pass | pass |
| exercises-dataset:1626 | smith machine reverse decline close grip bench press | pass | pass |
| exercises-dataset:0763 | smith reverse calf raises | pass | pass |
| exercises-dataset:3313 | weighted straight bar dip | pass | pass |
| exercises-dataset:2401 | dumbbell biceps curl (with arm blaster) | pass | pass |
| exercises-dataset:2402 | dumbbell hammer curls (with arm blaster) | pass | pass |
| exercises-dataset:1655 | dumbbell biceps curl squat | pass | pass |
| exercises-dataset:0298 | dumbbell cross body hammer curl | pass | pass |
| exercises-dataset:1664 | dumbbell high curl | pass | pass |
| exercises-dataset:1631 | cable concentration curl | pass | pass |
| exercises-dataset:1722 | cable high pulley overhead tricep extension | pass | pass |
| exercises-dataset:0203 | cable rear delt row (with rope) | pass | pass |
| exercises-dataset:1634 | cable lying bicep curl | pass | pass |
| exercises-dataset:0305 | dumbbell decline shrug | pass | pass |

Review: 30/30 passed visual review (incl. replacement pairs for 1634 and 0305).

Swaps and unbinds:
- exercises-dataset:0656 push-up (on stability ball) produced localPath `push_up_on_stability_ball_male.webp`,
  already bound to exercises-dataset:0655 — semantic near-duplicate, replaced by exercises-dataset:1634 cable lying bicep curl.
- exercises-dataset:1023 band straight back stiff leg deadlift deferred — near-duplicate of 1010 (same movement).
- exercises-dataset:0197 cable pulldown (pro lat bar) considered, skipped — near-duplicate of already-bound 0198/0150 pulldown records.
- free-exercise-db:Kettlebell_Halo_With_Overhead_Extension was generated and briefly bound, then UNBOUND:
  tests/regression.cjs requires this reviewed-supplement record to keep `media === undefined`
  (the existing free-exercise-db:Kettlebell_Halo keeps `exercise_media/kettlebell_halo.webp` untouched).
  Generated PNGs removed from media/ and App assets; metadata/NOTICE/PROVENANCE/test rows rolled back.
  Replaced by exercises-dataset:0305 dumbbell decline shrug (generated + reviewed + bound).
- Note: reviewed-supplement (`free-exercise-db:`) candidates are effectively unavailable for new bindings
  while the regression suite asserts their no-media state; remaining rounds draw from exercises-dataset records.

Notes:
- All assisted-bucket records (10) remain shelved — they are inherently two-person partner stretches.
- 2401/2402 show the arm blaster harness with the wordmark on the harness (male) / tank (female).
- A rollback-script bug briefly rewrote exercise_metadata.json with 4-space indent on both platforms;
  restored to canonical 2-space formatting before the 0305 delta integration.

Bound app media: 15 male WebP (1024px q82 method 4), byte-identical across HarmonyOS and Flutter bundles.
Metadata: 780 records both platforms; dup ids/paths/hashes: 0.
Media library: media/ 1230 PNG (+30 net vs round 42; 0656/halo pairs never entered or were removed).
media-open/ unchanged (688, open track paused).
