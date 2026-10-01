#!/bin/zsh
# Sequential, <=2 workers at any time. No pgrep-based waits (they self-match the calling shell).
cd /Users/samrudh/Documents/Projects/kaggle/Kaggriculture
B=moe/r4/build/opusb; PY=".venv/bin/python"
nice -n 10 $PY kaggle_load_check.py $B/cand_C1R2.py > $B/loadcheck_C1R2.log 2>&1; echo "loadcheck C1R2 exit $?"
nice -n 10 $PY kaggle_load_check.py $B/cand_C1RS.py > $B/loadcheck_C1RS.log 2>&1; echo "loadcheck C1RS exit $?"
nice -n 10 $PY $B/statecompat.py $B/tfc_index.json $B/tfc_states.json > $B/statecompat.log 2>&1; echo "statecompat exit $?"
nice -n 10 $PY $B/openwlv_b.py $B/openwlv_b.json C1=subY_C1_predict2.py C1R2=$B/cand_C1R2.py C1RS=$B/cand_C1RS.py > $B/openwlv_b.log 2>&1; echo "openwlv_b exit $?"
nice -n 10 $PY $B/gate.py $B/gate_rs.jsonl $B/gate_jobs_rs.json 2 > $B/gate_rs.log 2>&1; echo "gate_rs exit $?"
nice -n 10 $PY $B/eshop.py $B/eshop2.jsonl $B/eshop2_jobs.json 2 > $B/eshop2.log 2>&1; echo "eshop2 exit $?"
echo chain3-done
