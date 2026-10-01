# Held-out check: m30 vs bare Harvest on seeds 9200001-20 (disjoint from the 9100001-20 selection set).
import json, sys, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from concurrent.futures import ProcessPoolExecutor

def job(arg):
    from run import load, act
    import kagsim
    (na, pa, nb, pb), seed = arg
    a, _ = load(pa, "a"); b, _ = load(pb, "b")
    g = kagsim.Game(seed=int(seed))
    for t in range(719):
        g.step(act(a, g.observe(0)), act(b, g.observe(1)))
    return dict(a=na, b=nb, seed=seed, ra=float(g.reward(0)), rb=float(g.reward(1)))

if __name__ == "__main__":
    os.nice(10)
    jobs = [(("m30", "moe/r6/build/devin/harvest_m30.py", "H", "subAA_harvest.py"), s) for s in range(9200001, 9200021)]
    with ProcessPoolExecutor(max_workers=4) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r6/build/devin/m30_holdout.jsonl", "w"), indent=1)
    w = sum(r["ra"] > r["rb"] for r in rows); l = sum(r["ra"] < r["rb"] for r in rows)
    print("HELD-OUT seeds 9200001-20: m30 vs H:", w, "-", l, "-", len(rows) - w - l,
          "mean", round(sum(r["ra"] - r["rb"] for r in rows) / len(rows)))
