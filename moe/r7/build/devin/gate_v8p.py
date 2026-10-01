# Closed-loop gate: v8p vs v8 (h2h), and both vs M30B + shepherd anchors. Both seats.
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
    M30B = ("m30b", "moe/r6/build/devin/harvest_m30_brx2.py")
    SHEP = ("shep", "subW_shepherd.py")
    seeds = list(range(9600001, 9600016))
    jobs = []
    for s in seeds:
        jobs += [((V8P[0], V8P[1], V8[0], V8[1]), s), ((V8[0], V8[1], V8P[0], V8P[1]), s)]
    for s in seeds[:10]:
        jobs += [((V8P[0], V8P[1], M30B[0], M30B[1]), s), ((M30B[0], M30B[1], V8P[0], V8P[1]), s)]
        jobs += [((V8[0], V8[1], M30B[0], M30B[1]), s), ((M30B[0], M30B[1], V8[0], V8[1]), s)]
        jobs += [((V8P[0], V8P[1], SHEP[0], SHEP[1]), s), ((SHEP[0], SHEP[1], V8P[0], V8P[1]), s)]
        jobs += [((V8[0], V8[1], SHEP[0], SHEP[1]), s), ((SHEP[0], SHEP[1], V8[0], V8[1]), s)]
    with ProcessPoolExecutor(max_workers=6) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/gate_v8p.json", "w"), indent=1)
    from collections import defaultdict
    gg = defaultdict(list)
    for r in rows:
        gg[tuple(sorted((r["a"], r["b"])))].append(r)
    for pair, rs in gg.items():
        for n in pair:
            o = [x for x in rs if x["a"] == n]
            w = sum(x["ra"] > x["rb"] for x in o)
            m = sum(x["ra"] - x["rb"] for x in o) / len(o)
            print(f"{n} as A: {w}-{len(o)-w} margin {m:+.0f} | ", end="")
        print()
    for n in ("v8", "v8p"):
        h2h = [r for r in rows if {r["a"], r["b"]} == {"v8", "v8p"}]
        mine = [(r["ra"], r["rb"]) if r["a"] == n else (r["rb"], r["ra"]) for r in h2h]
        w = sum(a > b for a, b in mine)
        print(f"h2h {n}: {w}-{len(mine)-w} mean {sum(a for a,b in mine)/len(mine):.0f} margin {sum(a-b for a,b in mine)/len(mine):+.0f}")
