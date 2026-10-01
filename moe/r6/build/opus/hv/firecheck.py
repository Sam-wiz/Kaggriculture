# Fire check: Harvest+PREDICT2 (C1's 3-hunk Q-blob diff) vs C1R2, and bare Harvest vs C1R2, same seeds, seat 0.
import json, sys, os, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from concurrent.futures import ProcessPoolExecutor
def job(arg):
    from run import load, act, tele
    import kagsim
    (na, pa), seed = arg; t0 = time.time()
    a, ma = load(pa, "a"); b, mb = load("subZ_C1R2.py", "b")
    g = kagsim.Game(seed=int(seed))
    for t in range(719):
        g.step(act(a, g.observe(0)), act(b, g.observe(1)))
    return dict(a=na, seed=seed, ra=float(g.reward(0)), rb=float(g.reward(1)), tele=tele(ma), sec=round(time.time()-t0))
if __name__ == "__main__":
    seeds = range(9100001, 9100001 + int(sys.argv[1]))
    jobs = [(("HQ", "moe/r6/build/opus/hv/harvest_q.py"), s) for s in seeds] + [(("H", "subAA_harvest.py"), s) for s in seeds]
    os.nice(10)
    with ProcessPoolExecutor(max_workers=2) as ex:
        for r in ex.map(job, jobs):
            print(json.dumps(r), flush=True)
