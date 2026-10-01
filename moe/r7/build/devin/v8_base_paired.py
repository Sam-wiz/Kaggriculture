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
    jobs = [(("v8", "rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py", "M30B", "moe/r6/build/devin/harvest_m30_brx2.py"), s) for s in range(9700001, 9700021)]
    with ProcessPoolExecutor(max_workers=5) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/v8_base97.json", "w"), indent=1)
    w = sum(r["ra"] > r["rb"] for r in rows); l = sum(r["ra"] < r["rb"] for r in rows)
    print(f"v8 vs M30B (97-seeds): {w}-{l}-{len(rows)-w-l} mean {sum(r['ra']-r['rb'] for r in rows)/len(rows):+.0f}")
    print("losses:", [(r["seed"], round(r["ra"]-r["rb"])) for r in rows if r["ra"]<r["rb"]])
