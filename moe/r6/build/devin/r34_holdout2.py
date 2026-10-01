# r34v8 vs M30B and vs Harvest on FRESH seeds 9300001-20, both seats.
import json, sys, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from concurrent.futures import ProcessPoolExecutor

def job(arg):
    from run import load, act
    import kagsim
    (na, pa, nb, pb), seed, sw = arg
    a, _ = load(pa, "a"); b, _ = load(pb, "b")
    g = kagsim.Game(seed=int(seed))
    for t in range(719):
        g.step(act(a, g.observe(0)), act(b, g.observe(1)))
    return dict(a=na, b=nb, seed=seed, sw=sw, ra=float(g.reward(0)), rb=float(g.reward(1)))

if __name__ == "__main__":
    os.nice(10)
    X = ("r34v8", "rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py")
    jobs = []
    for opp, op in (("H", "subAA_harvest.py"), ("M30B", "moe/r6/build/devin/harvest_m30_brx2.py")):
        for s in range(9300001, 9300021):
            jobs.append(((X[0], X[1], opp, op), s, 0))
            jobs.append(((opp, op, X[0], X[1]), s, 1))  # r34 in seat 1
    with ProcessPoolExecutor(max_workers=4) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r6/build/devin/r34_holdout2.json", "w"), indent=1)
    for opp in ("H", "M30B"):
        for sw in (0, 1):
            g = [r for r in rows if ((r["a"], r["b"]) == ("r34v8", opp)) == (sw == 0) and {r["a"], r["b"]} == {"r34v8", opp}]
            rw = sum((r["ra"] if sw == 0 else r["rb"]) > (r["rb"] if sw == 0 else r["ra"]) for r in g)
            rl = sum((r["ra"] if sw == 0 else r["rb"]) < (r["rb"] if sw == 0 else r["ra"]) for r in g)
            m = sum(((r["ra"] - r["rb"]) if sw == 0 else (r["rb"] - r["ra"])) for r in g) / max(1, len(g))
            print(f"r34v8(seat{sw}) vs {opp}: {rw}-{rl}-{len(g)-rw-rl} mean {m:+.0f}")
