#!/bin/zsh
# One discussion round: each available Claude expert posts once (sequentially), then luna. Skips a lane
# whose round-1 file is missing or whose round-1 process is still running.
cd /Users/samrudh/Documents/Projects/kaggle/Kaggriculture
for pair in "sonnet:claude-sonnet-5" "opus:claude-opus-5-5" "opusb:claude-opus-5-5"; do
  n=${pair%%:*}; m=${pair#*:}
  [ -f moe/r5/$n.md ] || { echo "skip $n (no r1)"; continue; }
  pgrep -f "You are the .$n. expert" >/dev/null && { echo "skip $n (r1 running)"; continue; }
  ./moe/r5/claude_turn.sh $n $m; echo "$n posted"
done
.venv/bin/python moe/r5/luna_turn.py gpt-6-luna luna > /dev/null 2>&1 && echo "luna posted"
echo "ROUND DONE $(date -u +%H:%M)"
