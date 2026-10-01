#!/bin/zsh
# runs after chain 1 (E-shop -> load checks -> C1-RS gate); sequential, 2 workers max
cd /Users/samrudh/Documents/Projects/kaggle/Kaggriculture
while ps -p 58651 >/dev/null; do sleep 5; done
nice -n 10 .venv/bin/python moe/r4/build/opusb/openwlv_b.py moe/r4/build/opusb/openwlv_b.json C1=subY_C1_predict2.py C1R2=moe/r4/build/opusb/cand_C1R2.py C1RS=moe/r4/build/opusb/cand_C1RS.py > moe/r4/build/opusb/openwlv_b.log 2>&1
nice -n 10 .venv/bin/python moe/r4/build/opusb/eshop.py moe/r4/build/opusb/eshop2.jsonl moe/r4/build/opusb/eshop2_jobs.json 2 > moe/r4/build/opusb/eshop2.log 2>&1
echo chain2-done
