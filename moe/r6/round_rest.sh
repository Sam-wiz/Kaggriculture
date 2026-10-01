#!/bin/zsh
cd /Users/samrudh/Documents/Projects/kaggle/Kaggriculture
./moe/r6/claude_turn.sh opus claude-opus-5-5; echo "opus posted"
./moe/r6/claude_turn.sh opusb claude-opus-5-5; echo "opusb posted"
./moe/r6/astra_turn.sh; echo "astra posted"
echo "ROUND DONE $(date -u +%H:%M)"
