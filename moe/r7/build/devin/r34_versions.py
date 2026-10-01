# Which public r34 artifact is strongest vs our best? v5e/v5p/v6/v7 vs M30B, fresh seeds seat 0.
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
    BASE = ("M30B", "moe/r6/build/devin/harvest_m30_brx2.py")
    cands = [(v, f"rivalsGH/r34l-rudr44_kaggriculture/agents_{v}.py")
             for v in ("v5_planner", "v6", "v7")]
    jobs = [((c, p, BASE[0], BASE[1]), s) for c, p in cands for s in range(9500001, 9500021)]
    with ProcessPoolExecutor(max_workers=4) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/r34_versions.json", "w"), indent=1)
    for c, _ in cands:
        g = [r for r in rows if r["a"] == c]
        w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
        print(f"{c:10} vs M30B: {w}-{l}-{len(g)-w-l} mean {sum(r['ra']-r['rb'] for r in g)/len(g):+.0f}")
