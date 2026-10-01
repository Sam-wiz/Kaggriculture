# Tighter h2h: v8p and v8p2 vs v8 on 25 fresh seeds both seats + vs m30b/shep sample.
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
    V8P2 = ("v8p2", "moe/r7/build/devin/v8p2.py")
    M30B = ("m30b", "moe/r6/build/devin/harvest_m30_brx2.py")
    SHEP = ("shep", "subW_shepherd.py")
    jobs = []
    for s in range(9700001, 9700026):
        jobs += [((V8P[0], V8P[1], V8[0], V8[1]), s), ((V8[0], V8[1], V8P[0], V8P[1]), s)]
        jobs += [((V8P2[0], V8P2[1], V8[0], V8[1]), s), ((V8[0], V8[1], V8P2[0], V8P2[1]), s)]
    for s in range(9700001, 9700011):
        jobs += [((V8P2[0], V8P2[1], M30B[0], M30B[1]), s), ((M30B[0], M30B[1], V8P2[0], V8P2[1]), s)]
        jobs += [((V8P2[0], V8P2[1], SHEP[0], SHEP[1]), s), ((SHEP[0], SHEP[1], V8P2[0], V8P2[1]), s)]
    with ProcessPoolExecutor(max_workers=6) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/gate_v8p2.json", "w"), indent=1)
    def rep(n):
        h2h = [r for r in rows if {r["a"], r["b"]} == {n, "v8"}]
        mine = [(r["ra"], r["rb"]) if r["a"] == n else (r["rb"], r["ra"]) for r in h2h]
        w = sum(a > b for a, b in mine)
        print(f"h2h {n} vs v8: {w}-{len(mine)-w} mean {sum(a for a,b in mine)/len(mine):.0f} margin {sum(a-b for a,b in mine)/len(mine):+.0f}")
        for o in ("m30b", "shep"):
            g = [r for r in rows if {r["a"], r["b"]} == {n, o}]
            mm = [(r["ra"], r["rb"]) if r["a"] == n else (r["rb"], r["ra"]) for r in g]
            if mm:
                w2 = sum(a > b for a, b in mm)
                print(f"  {n} vs {o}: {w2}-{len(mm)-w2} margin {sum(a-b for a,b in mm)/len(mm):+.0f}")
    rep("v8p"); rep("v8p2")
