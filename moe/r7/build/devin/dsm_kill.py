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
        return dict(a=na, b=nb, seed=seed, ra=float(g.reward(0)), rb=float(g.reward(1)))
    except Exception as e:
        return dict(a=na, b=nb, seed=seed, err=repr(e)[:150])
if __name__ == "__main__":
    os.nice(10)
    C = ("v8dsm", "moe/r7/build/devin/agents_v8_dsm.py")
    V8 = ("v8", "rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py")
    M30B = ("M30B", "subAB_m30b.py")
    SHEP = ("shep", "subW_shepherd.py")
    jobs = []
    for s in range(9700001, 9700021):
        jobs += [((C[0], C[1], M30B[0], M30B[1]), s),
                 ((C[0], C[1], V8[0], V8[1]), s),
                 ((C[0], C[1], SHEP[0], SHEP[1]), s),
                 ((V8[0], V8[1], SHEP[0], SHEP[1]), s)]
    with ProcessPoolExecutor(max_workers=6) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/dsm_kill.json", "w"), indent=1)
    for a, b in ((C[0], "M30B"), (C[0], "v8"), (C[0], "shep"), ("v8", "shep")):
        g = [r for r in rows if r["a"] == a and r["b"] == b and "err" not in r]
        errs = sum(1 for r in rows if r["a"] == a and r["b"] == b and "err" in r)
        w = sum(r["ra"] > r["rb"] for r in g)
        m = sum(r["ra"]-r["rb"] for r in g)/max(1,len(g))
        print(f"{a:6} vs {b:5}: {w}-{len(g)-w} mean {m:+.0f} err={errs}")
