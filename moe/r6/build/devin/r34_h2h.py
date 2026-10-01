# r34v8 vs Harvest and vs M30B on the map seeds 9100001-20 (seat 0), to complete its RR picture.
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
    X = ("r34v8", "rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py")
    jobs = [((X[0], X[1], opp, op), s) for opp, op in
            (("H", "subAA_harvest.py"), ("M30B", "moe/r6/build/devin/harvest_m30_brx2.py"))
            for s in range(9100001, 9100021)]
    with ProcessPoolExecutor(max_workers=4) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r6/build/devin/r34_h2h.jsonl", "w"), indent=1)
    for opp in ("H", "M30B"):
        g = [r for r in rows if r["b"] == opp]
        w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
        print(f"r34v8 vs {opp}: {w}-{l}-{len(g)-w-l} mean {sum(r['ra']-r['rb'] for r in g)/len(g):+.0f}")
