# Round 40 — branded-only batch（男带标绑定 + 女带标入库）

- Date: 2026-11-17
- Tracks: branded male (bound to App) + branded female (media repo only). Open/unbranded track paused per project directive.
- Result: **30/30 images passed visual review on first generation — zero regenerations** (third consecutive clean round).

## Selected (15)

| catalogId | exercise | equipment |
|---|---|---|
| exercises-dataset:2403 | dumbbell alternate biceps curl (with arm blaster) | dumbbell |
| exercises-dataset:1651 | dumbbell bicep curl lunge with bowling motion | dumbbell |
| exercises-dataset:1276 | dumbbell decline one arm fly | dumbbell |
| exercises-dataset:1653 | dumbbell biceps curl with stork stance | dumbbell |
| exercises-dataset:1770 | biceps leg concentration curl | body weight |
| exercises-dataset:3166 | bodyweight standing row | body weight |
| exercises-dataset:3216 | chest tap push-up (male) | body weight |
| exercises-dataset:0002 | 45° side bend | body weight |
| exercises-dataset:3235 | cable assisted inverse leg curl | cable |
| exercises-dataset:0184 | cable lying extension pullover (with rope attachment) | cable |
| exercises-dataset:0190 | cable one arm curl | cable |
| exercises-dataset:3759 | lever seated good morning | leverage machine |
| exercises-dataset:0071 | barbell press sit-up | barbell |
| exercises-dataset:0072 | barbell prone incline curl | barbell |
| exercises-dataset:0066 | barbell one arm side deadlift | barbell |

## Notes

- `1770` biceps leg concentration curl: the Chinese step text describes a dumbbell concentration curl, but the exercise is a bodyweight move — depicted per name semantics as a seated curl of the athlete's own shin (hand gripping shin, curling leg up against arm resistance). Both tracks passed.
- `0002` 45° side bend: steps describe a standing lateral torso bend (hand slides toward knee); depicted standing, not on a 45° hyperextension bench, matching the supplied steps.
- `0066` barbell one arm side deadlift: depicted as suitcase-style single-center-grip barbell deadlift at shin level.
- `2403` arm blaster: harness plate rendered over upper arms; male wordmark on shorts, female wordmark on the blaster plate — both read `ALIVO` correctly.

## Review log

All 15 pairs reviewed visually: exercise posture/equipment, grip orientation, anatomy, framing, `ALIVO` spelling, single-frame/no-collage constraints. 30/30 pass, 0 regenerations.

## Integration

- App bundles: 720 → **735** bound records (HarmonyOS + Flutter identical WebP q82/m4, byte-diff 0).
- Metadata count: 735/735 both platforms; duplicate ids/paths/hashes: 0.
- `media/` PNG masters: 1,110 → **1,140** (male masters + female variants).
- `media/NOTICE.md`: Round 40 section appended (15 rows × 2 tracks, SHA-256 recorded).
- `catalog/exercise_metadata.json` synced; `catalog-review.html` rebuilt (1,352 records).
- Archive: `docs/round40/` contains prompts_m/, prompts_f/, plan/batch/manifest JSON, collect/integrate/launch/make_notice/make_prompts scripts and this report.

## Excluded (semantic duplicates / ambiguous, pool-side)

- `exercises-dataset:0164` cable front shoulder raise — near-duplicate of bound `0161` cable forward raise (Round 39).
- `exercises-dataset:1327` close grip chin-up — near-duplicate of bound `2987` weighted close grip chin up on dip cage.
- `exercises-dataset:3019` bench pull-ups — near-duplicate of bound `0499` inverted row family.
- `exercises-dataset:2462` chest dip on straight bar — crowded dip family already bound.
