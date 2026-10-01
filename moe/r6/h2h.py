import json, sys, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r4/build/opus"); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
import rr
from concurrent.futures import ProcessPoolExecutor
C = [("haodou", "rivals9/haodou092_kaggriculture-harvest-ledger/main.py"),
     ("guru_v4", "rivals9/guruprasaathas111_kaggriculture-top-2-master-engine-v4/main.py")]
if __name__ == "__main__":
    jobs = [(c, ("C1R2", "subZ_C1R2.py"), s, 0) for c in C for s in range(9100001, 9100021)]
    with ProcessPoolExecutor(max_workers=4) as ex: res = list(ex.map(rr.job, jobs))
    json.dump(res, open("moe/r6/h2h_c1r2.json", "w"))
    for n, _ in C:
        g = [r for r in res if r["a"] == n and "err" not in r]; w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
        print(f"{n:8} vs C1R2: {w}-{l}-{len(g)-w-l}  mean {sum(r['ra']-r['rb'] for r in g)/max(1,len(g)):+.0f}  errors {sum('err' in r for r in res if r['a']==n)}", flush=True)
