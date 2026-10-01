import json, sys, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from concurrent.futures import ProcessPoolExecutor
def job(arg):
    from run import load, act
    import kagsim
    (na, pa, nb, pb), seed, sw = arg
    try:
        a, _ = load(pa, "a"); b, _ = load(pb, "b")
        g = kagsim.Game(seed=int(seed))
        for t in range(719):
            o0, o1 = g.observe(0), g.observe(1)
            if sw == 0: g.step(act(a, o0), act(b, o1))
            else: g.step(act(b, o0), act(a, o1))
        r = [float(g.reward(0)), float(g.reward(1))]
        ra, rb = (r[0], r[1]) if sw == 0 else (r[1], r[0])
        return dict(a=na, b=nb, seed=seed, sw=sw, ra=ra, rb=rb)
    except Exception as e:
        return dict(a=na, b=nb, seed=seed, sw=sw, err=repr(e)[:150])
if __name__ == "__main__":
    os.nice(10)
    cand = ("M30B", "moe/r6/build/devin/harvest_m30_brx2.py")
    opps = [("jaxa2802", "rivals/jaxa623_2802/main.py"),
            ("melon2749", "rivals/kaggriculture-melon-threshold-squeeze-2749/main.py"),
            ("jaxa2780", "rivals/jaxa623_2780/main.py")]
    jobs = [((cand[0], cand[1], n, p), s, sw) for n, p in opps for s in range(9900001, 9900011) for sw in (0, 1)]
    with ProcessPoolExecutor(max_workers=5) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/counter_test.json", "w"), indent=1)
    for n, _ in opps:
        g = [r for r in rows if r["b"] == n and "err" not in r]
        errs = sum(1 for r in rows if r["b"] == n and "err" in r)
        w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
        print(f"M30B vs {n:10}: {w}-{l}-{len(g)-w-l} mean {sum(r['ra']-r['rb'] for r in g)/max(1,len(g)):+.0f} err={errs}")
