# Confirmatory h2h: v8p vs v8 on 30 MORE fresh seeds (both seats) + solo baseline delta.
import sys, os, json
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
    V8 = ("v8", "subAC_v8.py")
    V8P = ("v8p", "moe/r7/build/devin/v8p.py")
    jobs = []
    for s in range(9800001, 9800031):
        jobs += [((V8P[0], V8P[1], V8[0], V8[1]), s), ((V8[0], V8[1], V8P[0], V8P[1]), s)]
    with ProcessPoolExecutor(max_workers=6) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/gate_v8p3.json", "w"), indent=1)
    mine = [(r["ra"], r["rb"]) if r["a"] == "v8p" else (r["rb"], r["ra"]) for r in rows]
    w = sum(a > b for a, b in mine)
    print(f"h2h v8p vs v8 (fresh 30x2): {w}-{len(mine)-w} margin {sum(a-b for a,b in mine)/len(mine):+.0f}")
    print("v8p wins by seed:", [r["seed"] for r in rows if (r["ra"] > r["rb"]) == (r["a"] == "v8p")])
