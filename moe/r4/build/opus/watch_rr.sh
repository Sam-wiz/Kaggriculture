#!/bin/zsh
cd /Users/samrudh/Documents/Projects/kaggle/Kaggriculture
F=moe/r4/build/opus/rr_retro.jsonl
for m in 100 200 300 400; do
  while true; do
    n=$(wc -l < $F)
    if [ $n -ge $m ]; then break; fi
    if ! pgrep -f "opus/rr.py" >/dev/null; then break; fi
    sleep 20
  done
  echo "rr games=$(wc -l < $F) at $(date -u +%H:%M) errs=$(grep -c err $F)"
  if ! pgrep -f "opus/rr.py" >/dev/null; then echo "rr process exited"; break; fi
done
