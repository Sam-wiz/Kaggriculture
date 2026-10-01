"""Sonnet r4: re-run claude-code's moe/r3/c1_indep.py claim (0.88/0.75, n=32) independently,
with max_workers=2 per the r4 machine budget. Same seeds/opponents, unmodified logic."""
import sys, os, statistics as st, math
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT)
from concurrent.futures import ProcessPoolExecutor
import harness
C1 = "moe/r3/build/opus/cand_C1_rebuilt.py"
def job(a):
    opp, s, sw = a
    x, y = (opp, C1) if sw else (C1, opp)
    r = harness.run_episode(x, y, seed=s, catch_errors=True)
    if r["status"] != ["DONE", "DONE"]: return (opp, None)
    p, q = r["reward"][::-1] if sw else r["reward"]
    return (opp, p - q)
if __name__ == "__main__":
    seeds = list(range(8800001, 8800017))
    opps = ("subW_shepherd.py", "subX_hyb2965.py")
    jobs = [(o, s, sw) for o in opps for s in seeds for sw in (0, 1)]
    with ProcessPoolExecutor(max_workers=2) as ex: res = list(ex.map(job, jobs))
    for o in opps:
        m = [r[1] for r in res if r[0] == o and r[1] is not None]
        fails = sum(1 for r in res if r[0] == o and r[1] is None)
        w = sum(1 for x in m if x > 0); l = sum(1 for x in m if x < 0); t = len(m) - w - l
        print(f"C1 vs {o}: {w}-{l}-{t} (WR {(w+.5*t)/len(m):.2f}), mean {st.mean(m):+.0f}, SE {st.stdev(m)/math.sqrt(len(m)):.0f}, n={len(m)}, fails={fails}", flush=True)
