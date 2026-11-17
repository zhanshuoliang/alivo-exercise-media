#!/usr/bin/env bash
cd /d/codex-temp/alivo-selfmade-generated-round7
REF_M="D:/codex-temp/alivo-exercise-media/media/handstand_male.png"
REF_F="D:/codex-temp/alivo-exercise-media/media/handstand_female.png"
mkdir -p logs31_m logs31_f logs31_open_m logs31_open_f
# wave 1: branded tracks (30 jobs)
for f in prompts31_m/exec_*.txt; do
  eid=$(basename "$f" .txt)
  (cat "$f" | codex exec -C . --skip-git-repo-check -i "$REF_M" > "logs31_m/${eid}.log" 2>&1) &
done
for f in prompts31_f/exec_*.txt; do
  eid=$(basename "$f" .txt)
  (cat "$f" | codex exec -C . --skip-git-repo-check -i "$REF_F" > "logs31_f/${eid}.log" 2>&1) &
done
wait
echo "wave1 done"
# wave 2: open tracks (30 jobs)
for f in prompts31_open_m/exec_*.txt; do
  eid=$(basename "$f" .txt)
  (cat "$f" | codex exec -C . --skip-git-repo-check > "logs31_open_m/${eid}.log" 2>&1) &
done
for f in prompts31_open_f/exec_*.txt; do
  eid=$(basename "$f" .txt)
  (cat "$f" | codex exec -C . --skip-git-repo-check > "logs31_open_f/${eid}.log" 2>&1) &
done
wait
echo "all done"
