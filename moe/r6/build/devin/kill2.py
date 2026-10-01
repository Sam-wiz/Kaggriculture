# Kill test round 2: p324 + _CA knob variants vs M30B on fresh seeds 9400001-20, seat 0.
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
    cands = [
        ("p324", "moe/r6/build/devin/harvest_m30b_p324.py"),
        ("buf14", "moe/r6/build/devin/harvest_m30b_buf14.py"),
        ("cash300", "moe/r6/build/devin/harvest_m30b_cash300.py"),
        ("feed0", "moe/r6/build/devin/harvest_m30b_feed0.py"),
        ("from4", "moe/r6/build/devin/harvest_m30b_from4.py"),
    ]
    jobs = [((c, p, BASE[0], BASE[1]), s) for c, p in cands for s in range(9400001, 9400021)]
    with ProcessPoolExecutor(max_workers=5) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r6/build/devin/kill2.json", "w"), indent=1)
    for c, _ in cands:
        g = [r for r in rows if r["a"] == c]
        w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
        print(f"{c:8} vs M30B: {w}-{l}-{len(g)-w-l} mean {sum(r['ra']-r['rb'] for r in g)/len(g):+.0f}")
