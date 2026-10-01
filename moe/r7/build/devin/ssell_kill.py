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
    C = ("v8ss", "moe/r7/build/devin/agents_v8_ssell.py")
    for opp in (("M30B","subAB_m30b.py"), ("v8","rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py"), ("shep","subW_shepherd.py")):
        jobs = [((C[0], C[1], opp[0], opp[1]), s) for s in range(9700001, 9700016)]
        with ProcessPoolExecutor(max_workers=6) as ex:
            rows = list(ex.map(job, jobs, chunksize=1))
        g = [r for r in rows if "err" not in r]
        w = sum(r["ra"] > r["rb"] for r in g)
        print(f"{C[0]} vs {opp[0]:5}: {w}-{len(g)-w} mean {sum(r['ra']-r['rb'] for r in g)/len(g):+.0f}", flush=True)
