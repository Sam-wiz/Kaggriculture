#!/bin/zsh
cd /Users/samrudh/Documents/Projects/kaggle/Kaggriculture
for pair in "haodou092_kaggriculture-harvest-ledger:rivals9/haodou092_kaggriculture-harvest-ledger/main.py" "guruprasaathas111_kaggriculture-top-2-ma:rivals9/guruprasaathas111_kaggriculture-top-2-master-engine-v4/main.py" "tetsutani_demand-preserving-turn-sale-ti:rivals9/tetsutani_demand-preserving-turn-sale-timing/main.py" "lynnsakurai_farmer-john-and-the-idle-sel:rivals9/lynnsakurai_farmer-john-and-the-idle-seller/main.py"; do
  n=${pair%%:*}; p=${pair#*:}
  echo "=== $n"; nice .venv/bin/python moe/r6/screen2.py $n $p 4 2>&1 | grep -v HP_TELEM | tail -9
done
echo "=== head-to-head vs C1R2 (20 seeds, sw=0)"
.venv/bin/python - <<'PY'
import json,sys,os
sys.path.insert(0,"moe/r4/build/opus"); sys.path.insert(0,"moe/r3/build/opus")
import rr
from concurrent.futures import ProcessPoolExecutor
C=[("haodou","rivals9/haodou092_kaggriculture-harvest-ledger/main.py"),("guru_v4","rivals9/guruprasaathas111_kaggriculture-top-2-master-engine-v4/main.py"),("tetsutani","rivals9/tetsutani_demand-preserving-turn-sale-timing/main.py"),("lynn_idle","rivals9/lynnsakurai_farmer-john-and-the-idle-seller/main.py")]
if __name__=="__main__":
    jobs=[(c,("C1R2","subZ_C1R2.py"),s,0) for c in C for s in range(9100001,9100021)]
    with ProcessPoolExecutor(max_workers=4) as ex: res=list(ex.map(rr.job,jobs))
    json.dump(res,open("moe/r6/h2h_c1r2.json","w"))
    for n,_ in C:
        g=[r for r in res if r["a"]==n and "err" not in r]; w=sum(r["ra"]>r["rb"] for r in g); l=sum(r["ra"]<r["rb"] for r in g)
        print(f"{n:10} vs C1R2: {w}-{l}-{len(g)-w-l}  mean {sum(r['ra']-r['rb'] for r in g)/max(1,len(g)):+.0f}")
PY
echo "STAGE2 DONE $(date -u +%H:%M)"
