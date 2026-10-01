import json, sys, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from concurrent.futures import ProcessPoolExecutor
def job(arg):
    from run import load, act
    import kagsim
    (na, pa, nb, pb), seed = arg
    try:
        a, _ = load(pa, "a"); b, _ = load(pb, "b")
        g = kagsim.Game(seed=int(seed))
        for t in range(719):
            g.step(act(a, g.observe(0)), act(b, g.observe(1)))
        return dict(a=na, seed=seed, ra=float(g.reward(0)), rb=float(g.reward(1)))
    except Exception as e:
        return dict(a=na, seed=seed, err=repr(e)[:150])
if __name__ == "__main__":
    os.nice(10)
    BASE = ("M30B", "subAB_m30b.py")
    cands = [("hd_g1", "moe/r7/build/devin/hd_g1.py"), ("hd_g2", "moe/r7/build/devin/hd_g2.py")]
    jobs = [((n, p, BASE[0], BASE[1]), s) for n, p in cands for s in range(9990001, 9990021)]
    with ProcessPoolExecutor(max_workers=5) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/hd_kill.json", "w"), indent=1)
    for n, _ in cands:
        g = [r for r in rows if r["a"] == n and "err" not in r]
        errs = sum(1 for r in rows if r["a"] == n and "err" in r)
        w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
        print(f"{n} vs M30B: {w}-{l} mean {sum(r['ra']-r['rb'] for r in g)/max(1,len(g)):+.0f} err={errs}")
