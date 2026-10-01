#!/bin/zsh
cd /Users/samrudh/Documents/Projects/kaggle/Kaggriculture
while ps -p 76033 >/dev/null; do sleep 10; done
B=moe/r4/build/opusb
OW_HOLD=1 nice -n 10 .venv/bin/python $B/openwlv_b.py $B/openwlv_b_hold.json C1=subY_C1_predict2.py C1R2=$B/cand_C1R2.py C1RS=$B/cand_C1RS.py > $B/openwlv_b_hold.log 2>&1
echo chain4-done
