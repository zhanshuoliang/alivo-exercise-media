# Round 43 — 15 branded pairs, male track bound to app

Equipment split: small-bucket sweep (band x1 + kettlebell x2 + smith x2 + weighted x1) + dumbbell x5 + cable x4.

| ID | Exercise | Male | Female |
|----|----------|------|--------|
| exercises-dataset:1010 | band straight leg deadlift | pass | pass |
| exercises-dataset:0530 | kettlebell double windmill | pass | pass |
| free-exercise-db:Kettlebell_Halo_With_Overhead_Extension | kettlebell halo with overhead extension | pass | pass |
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

Review: 30/30 passed visual review.

Swaps:
- exercises-dataset:0656 push-up (on stability ball) produced localPath `push_up_on_stability_ball_male.webp`,
  already bound to exercises-dataset:0655 — semantic near-duplicate, replaced by exercises-dataset:1634 cable lying bicep curl.
- exercises-dataset:1023 band straight back stiff leg deadlift deferred — near-duplicate of 1010 (same movement).

Notes:
- The free-exercise-db kettlebell halo record is the first bound `free-exercise-db:` catalog entry in this phase.
- All assisted-bucket records (10) remain shelved — they are inherently two-person partner stretches.
- 2401/2402 show the arm blaster harness with the wordmark on the harness (male) / tank (female).

Bound app media: 15 male WebP (1024px q82 method 4), byte-identical across HarmonyOS and Flutter bundles.
Metadata: 780 records both platforms; dup ids/paths/hashes: 0.
Media library: media/ 1230 PNG (+30). media-open/ unchanged (688, open track paused).
