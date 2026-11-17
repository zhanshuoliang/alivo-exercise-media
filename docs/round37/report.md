# Round 37 — branded-only edition

Date: 2026-11-17

## Scope

15 exercises × 2 branded tracks (male + female) = 30 PNGs. Open/unbranded track remains paused.

- Male branded: bound into both app bundles, 675 → **690** of 1,352.
- Female branded + male PNG masters: archived in `media/` (1050 PNGs total).

## Selected exercises

| catalogId | name | bucket |
|---|---|---|
| exercises-dataset:0045 | barbell guillotine bench press | barbell |
| exercises-dataset:0065 | barbell one arm floor press | barbell |
| exercises-dataset:0083 | barbell rollerout from bench | barbell |
| exercises-dataset:1751 | barbell pin presses | barbell |
| exercises-dataset:2187 | barbell reverse close-grip bench press | barbell |
| exercises-dataset:0185 | cable lying fly | cable |
| exercises-dataset:0189 | cable one arm bent over row | cable |
| exercises-dataset:0204 | cable rear drive | cable |
| exercises-dataset:1319 | cable palm rotational row | cable |
| exercises-dataset:1261 | cable decline press | cable |
| exercises-dataset:0496 | inverse leg curl (bench support) | body weight |
| exercises-dataset:0464 | front plank with twist | body weight |
| exercises-dataset:1771 | bodyweight kneeling triceps extension | body weight |
| exercises-dataset:3214 | arms apart circular toe touch (male) | body weight |
| exercises-dataset:3168 | bodyweight squatting row | body weight |

Rejected near-duplicates during selection: `2300` inverted row bent knees (vs bound `0499`), `1275` drop push up (vs bound `1310`), `0262` cross body crunch (vs bound crunch family incl. `0972`/`3640`).

## Review

30/30 passed; 3 retries:

- `2187` reverse close-grip bench press (both tracks): first render used an overhand grip instead of the required SUPINATED underhand grip. Prompt strengthened to explicit palms-up/fingers-under-bar wording; regenerated correctly on first retry.
- `0185` cable lying fly (female): first render misspelled the wordmark ("OAIVO") and placed the head off the bench end. Regenerated correctly on first retry with same prompt.

All other 27 images passed on first generation.

## Packaging

- 15 male WebP at 1024×1024, quality 82, method 4 — byte-identical in both app bundles.
- `exercise_metadata.json` media records: 690 entries each end, no duplicate catalogIds/paths/sha256.
- NOTICE / PROVENANCE / `exercise_media_test.dart` appended on both platforms.
- `media/NOTICE.md` Round 37 section with SHA-256 for all 30 PNGs.
- `media-open/` unchanged at 688 manifest records.

## Verification

- Node regression `tests/regression.cjs`: 777/777 pass.
- Flutter `exercise_media_test.dart`: 5/5 pass.
- `catalog-review.html` rebuilt with Round 37 records; JS parses clean.
