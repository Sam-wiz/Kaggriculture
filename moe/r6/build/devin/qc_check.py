# HQc (censor-aware) vs C1R2 and HQc vs HQ, seat 0, seeds 9100001..N — telemetry + reward.
import json, sys, os, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from concurrent.futures import ProcessPoolExecutor

def job(arg):
    from run import load, act, tele
    import kagsim
    (na, pa, nb, pb), seed = arg; t0 = time.time()
    a, ma = load(pa, "a"); b, mb = load(pb, "b")
    g = kagsim.Game(seed=int(seed))
    for t in range(719):
        g.step(act(a, g.observe(0)), act(b, g.observe(1)))
    return dict(a=na, b=nb, seed=seed, ra=float(g.reward(0)), rb=float(g.reward(1)), tele=tele(ma), sec=round(time.time()-t0))

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    seeds = range(9100001, 9100001 + N)
    jobs = [(("HQc", "moe/r6/build/devin/harvest_qc.py", "C1R2", "subZ_C1R2.py"), s) for s in seeds]
    jobs += [(("HQc", "moe/r6/build/devin/harvest_qc.py", "HQ", "moe/r6/build/opus/hv/harvest_q.py"), s) for s in seeds]
    os.nice(10)
    with ProcessPoolExecutor(max_workers=4) as ex:
        for r in ex.map(job, jobs):
            print(json.dumps(r), flush=True)
