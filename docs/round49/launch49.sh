#!/usr/bin/env bash
cd /d/codex-temp/alivo-selfmade-generated-round7
REF_M="D:/codex-temp/alivo-exercise-media/media/handstand_male.png"
REF_F="D:/codex-temp/alivo-exercise-media/media/handstand_female.png"
mkdir -p logs49_m logs49_f
for f in prompts49_m/exec_*.txt; do
  eid=$(basename "$f" .txt); eid=${eid#exec_}
  (cat "$f" | codex exec -C . --skip-git-repo-check -i "$REF_M" > "logs49_m/${eid}.log" 2>&1) &
done
for f in prompts49_f/exec_*.txt; do
  eid=$(basename "$f" .txt); eid=${eid#exec_}
  (cat "$f" | codex exec -C . --skip-git-repo-check -i "$REF_F" > "logs49_f/${eid}.log" 2>&1) &
done
wait
echo "all done"
