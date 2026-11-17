# Round 44 — 15 branded pairs, male track bound to app

Equipment split: leverage machine x6 + weighted x1 + dumbbell x3 + cable x2 + barbell x1 + bodyweight x2.

| ID | Exercise | Male | Female |
|----|----------|------|--------|
| exercises-dataset:2331 | cycle cross trainer | pass | pass |
| exercises-dataset:0591 | lever overhand triceps dip | pass | pass |
| exercises-dataset:2335 | lever seated calf press | pass | pass |
| exercises-dataset:1385 | lever seated squat calf raise on leg press machine | pass | pass |
| exercises-dataset:1351 | lever t-bar reverse grip row | pass | pass |
| exercises-dataset:0673 | reverse grip machine lat pulldown | pass | pass |
| exercises-dataset:3641 | weighted kneeling step with swing | pass | pass |
| exercises-dataset:3545 | dumbbell incline alternate press | pass | pass |
| exercises-dataset:0318 | dumbbell incline curl | pass | pass |
| exercises-dataset:0322 | dumbbell incline inner biceps curl | pass | pass |
| exercises-dataset:0173 | cable incline triceps extension | pass | pass |
| exercises-dataset:1633 | cable one arm preacher curl | pass | pass |
| exercises-dataset:0024 | barbell bench front squat | pass | pass |
| exercises-dataset:0284 | donkey calf raise | pass | pass |
| exercises-dataset:3292 | elevator | pass | pass |

Review: 30/30 passed visual review.

Retries:
- exercises-dataset:3641 female — first exec session generated the image but ended without printing the path;
  re-ran the same prompt once, collected output path normally. No image-quality rework needed.

Screening exclusions this round:
- 1439 lever gripless shrug v.2 / 0595+3760 lever seated crunch variants / 0869+2318 lever shoulder press v.2+v.3
  / 1614 lever preacher curl v.2 — exact-base near-duplicates of already-bound records.
- 1394 smith reverse calf raises — literal duplicate name of bound 0763.
- 0772 smith standing behind head military press — near-duplicate of bound 0788 behind-neck press.
- 2736 lever reverse grip lateral pulldown — near-duplicate of 0673 + contradictory steps text.
- 2364 assisted wide-grip chest dip / 2462 chest dip on straight bar — near-duplicates of bound chest dips.
- 2333 arm slingers hanging straight legs — variant of bound "arm slingers hanging bent knee legs" + hanging leg raise.
- 0443 elbow-to-knee, 0267 crunch (hands overhead), 3016 curl-up — saturated crunch family near-duplicates.
- 3287 elbow dips — near-duplicate of bound bench dip (knees bent).
- 0139/0140/1327/3019 pull-up variants — pull-up/chin-up family saturated.
- 3156/3158/3161/3162/3165/3167 standing towel row variants — near-duplicates of bound bodyweight rows.
- 0578 lever deadlift — name/steps contradiction persists; shelved.
- 1023 band straight back stiff leg deadlift — near-duplicate of bound 1010; shelved.
- 0656 push-up (on stability ball) — localPath collision with bound 0655; shelved.
- 2371 weighted russian twist v.2 — collision with bound 0846; shelved.
- All 10 assisted-bucket records — inherently two-person partner stretches; shelved.

Bound app media: 15 male WebP (1024px q82 method 4), byte-identical across HarmonyOS and Flutter bundles.
Metadata: 795 records both platforms; dup ids/paths/hashes: 0.
Media library: media/ 1260 PNG (+30). media-open/ unchanged (688, open track paused).
