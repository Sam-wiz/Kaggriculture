#!/bin/zsh
# One thread turn for Codex astra (xhigh, ChatGPT login; no OpenAI API key in env).
cd /Users/samrudh/Documents/Projects/kaggle/Kaggriculture
SC=/private/tmp/claude-501/-Users-samrudh-Documents-Projects-kaggle/e0344d37-1f28-4f96-bc10-a69aad6c84c8/scratchpad
P="You are 'astra' in the MoE r6 LIVE discussion. Read moe/r6/THREAD.md in full (rules at the top of moe/r4/THREAD.md) and as needed moe/r6/BRIEF.md and moe/r6/{opus,opusb,sonnet,astra}.md. Append exactly ONE new post to moe/r6/THREAD.md (cat >> moe/r6/THREAD.md, never edit existing text): reply by name, AGREE/DISPUTE/NEW EVIDENCE with file paths and numbers, <=300 words, end with **Next action (<owner>):**. Small checks allowed (<=2 workers, <=15 min, scratch in moe/r6/build/astra/). Do not use moe/tools/oai.py or any OpenAI API key. No submissions."
env -u KAGGLE_USERNAME -u KAGGLE_KEY -u OPENAI_API_KEY KAGGLE_CONFIG_DIR=$SC/nokaggle codex exec --skip-git-repo-check -m gpt-6-astra -c model_reasoning_effort='"xhigh"' -c approval_policy='"never"' -s workspace-write -C "$PWD" "$P" < /dev/null > moe/r6/turn_astra_$(date -u +%H%M).log 2>&1
