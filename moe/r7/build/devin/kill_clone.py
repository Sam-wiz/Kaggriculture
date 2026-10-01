# Kill test: clone_dsm vs opponents on paired seeds, both seats.
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
    CLONE = ("clone", "moe/r7/build/devin/clone_dsm.py")
    opps = [
        ("M30B", "moe/r6/build/devin/harvest_m30_brx2.py"),
        ("v8", "subAC_v8.py"),
        ("shep", "subW_shepherd.py"),
    ]
    jobs = [((CLONE[0], CLONE[1], o, p), s) for o, p in opps for s in range(9500001, 9500011)]
    with ProcessPoolExecutor(max_workers=5) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/kill_clone.json", "w"), indent=1)
    for o, _ in opps:
        g = [r for r in rows if r["b"] == o]
        w = sum(r["ra"] > r["rb"] for r in g)
        print(f"clone vs {o}: {w}-{len(g)-w}  mean {sum(r['ra'] for r in g)/len(g):.0f} vs {sum(r['rb'] for r in g)/len(g):.0f}  margin {sum(r['ra']-r['rb'] for r in g)/len(g):+.0f}")
