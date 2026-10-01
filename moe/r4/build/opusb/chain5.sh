#!/bin/zsh
cd /Users/samrudh/Documents/Projects/kaggle/Kaggriculture
while ps -p 83500 >/dev/null; do sleep 10; done
B=moe/r4/build/opusb
nice -n 10 .venv/bin/python $B/eshop.py $B/eshop2.jsonl $B/eshop2_jobs.json 2 > $B/eshop2.log 2>&1; echo "eshop2 exit $?"
nice -n 10 .venv/bin/python $B/gate.py $B/gate_rs.jsonl $B/gate_jobs_rs.json 2 > $B/gate_rs.log 2>&1; echo "gate_rs exit $?"
echo chain5-done
