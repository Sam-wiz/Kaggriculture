#!/bin/zsh
# One discussion turn for a Claude participant. usage: claude_turn.sh <name> <model>
cd /Users/samrudh/Documents/Projects/kaggle/Kaggriculture
SC=/private/tmp/claude-501/-Users-samrudh-Documents-Projects-kaggle/e0344d37-1f28-4f96-bc10-a69aad6c84c8/scratchpad
N=$1; M=$2
P="You are '$N' in the MoE r4 LIVE discussion. Read moe/r4/THREAD.md in full (its rules are at the top) and, as needed, moe/r4/BRIEF.md and the round-1 files it references. Then append exactly ONE new post to moe/r4/THREAD.md with a bash heredoc append (cat >> moe/r4/THREAD.md), never editing existing text. Reply by name to posts addressed to you or in your lane; bring NEW evidence where you can (you may run small checks IN THE FOREGROUND ONLY — never background jobs or waiting for notifications, this is a one-shot session that ends when you stop: <=2 workers, <=15 minutes, scratch under moe/r4/build/$N/; if a check from an earlier turn left output files, read them). You MUST append your post before finishing. End with **Next action (<owner>):** one concrete, checkable step. No submissions."
env -u KAGGLE_USERNAME -u KAGGLE_KEY KAGGLE_CONFIG_DIR=$SC/nokaggle claude -p --model $M --effort xhigh --allowedTools "Bash" "Read" "Write" "Edit" "Grep" "Glob" --disallowedTools "Bash(*competitions submit*)" "WebFetch" -- "$P" < /dev/null > moe/r4/turn_${N}_$(date -u +%H%M).log 2>&1
