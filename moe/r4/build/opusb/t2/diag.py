"""V219/CXTB tomato layer in C1: does it fire, what gates it, what is it worth. Closed-loop kagsim.
Job: seed, us, o (opp name), minrev (C1 _CXTB_MIN_REVENUE; 9000 = production), f (candidate file, default C1).
usage: diag.py OUT.jsonl JOBS.json WORKERS"""
import json, os, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from run import load, act
import kagsim
OPP = {"shep": "subW_shepherd.py", "hyb": "subX_hyb2965.py"}
def job(j):
    t0 = time.time()
    try:
        a, ma = load(j.get("f", "subY_C1_predict2.py"), "x"); b, mb = load(OPP[j["o"]], "o")
        ma._CXTB_MIN_REVENUE = j["minrev"]
        g = kagsim.Game(seed=int(j["seed"])); us = j["us"]; sh = None
        for t in range(720):
            o0, o1 = g.observe(0), g.observe(1)
            if t == 719: sh = o0["town"]["unlocked_shops"]
            A, B = (a, b) if us == 0 else (b, a)
            g.step(act(A, o0), act(B, o1))
        r = [float(g.reward(0)), float(g.reward(1))]
        v = {k: v for k, v in ma._V219_REPORT.items() if isinstance(v, (int, float))}
        return dict(j, m=r[us] - r[1 - us], me=r[us], opp=r[1 - us], v219=v,
                    cx=[f for f in ma._CXTB_REPORT["cxtb_features"]], shops=sh, s=round(time.time() - t0, 1))
    except Exception as e:
        return dict(j, err=repr(e)[:300])
if __name__ == "__main__":
    out, jobs, W = sys.argv[1], json.load(open(sys.argv[2])), int(sys.argv[3])
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=W) as ex, open(out, "a") as f:
        for r in ex.map(job, jobs, chunksize=1):
            f.write(json.dumps(r) + "\n"); f.flush()
