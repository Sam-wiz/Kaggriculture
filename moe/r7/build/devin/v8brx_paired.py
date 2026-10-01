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
    CANDS = [("v8", "rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py"), ("v8brx2", "moe/r7/build/devin/agents_v8_brx2.py")]
    M = ("M30B", "moe/r6/build/devin/harvest_m30_brx2.py")
    jobs = [((n, p, M[0], M[1]), s) for n, p in CANDS for s in range(9800001, 9800021)]
    with ProcessPoolExecutor(max_workers=5) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/v8brx_paired.json", "w"), indent=1)
    for n, _ in CANDS:
        g = [r for r in rows if r["a"] == n]
        w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
        print(f"{n:7} vs M30B: {w}-{l} mean {sum(r['ra']-r['rb'] for r in g)/len(g):+.0f} | losses: {[(r['seed'],round(r['ra']-r['rb'])) for r in g if r['ra']<r['rb']]}")
