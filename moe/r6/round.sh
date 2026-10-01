#!/bin/zsh
cd /Users/samrudh/Documents/Projects/kaggle/Kaggriculture
for pair in "sonnet:claude-sonnet-5" "opus:claude-opus-5-5" "opusb:claude-opus-5-5"; do
  n=${pair%%:*}; m=${pair#*:}; [ -f moe/r6/$n.md ] || { echo "skip $n"; continue; }
  ./moe/r6/claude_turn.sh $n $m; echo "$n posted"
done
[ -f moe/r6/astra.md ] && { ./moe/r6/astra_turn.sh; echo "astra posted"; }
echo "ROUND DONE $(date -u +%H:%M)"
