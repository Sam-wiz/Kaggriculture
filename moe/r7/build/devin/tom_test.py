# TOM patch eval: v8_tom vs v8-base paired on fresh seeds both seats,
# plus patched-vs-{shep,M30B} margins compared to base on the same seeds.
import json, sys, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from concurrent.futures import ProcessPoolExecutor

BASE = ("base", "subAC_v8.py")
TOM = ("tom", "moe/r7/build/devin/v8_tom.py")
OPP = [("shep", "subW_shepherd.py"), ("m30b", "moe/r6/build/devin/harvest_m30_brx2.py")]

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
    seeds = list(range(9500101, 9500121))
    jobs = []
    for s in seeds:
        jobs.append(((TOM[0], TOM[1], BASE[0], BASE[1]), s))
        jobs.append(((BASE[0], BASE[1], TOM[0], TOM[1]), s))
    for o in OPP:
        for s in seeds:
            jobs.append(((TOM[0], TOM[1], o[0], o[1]), s))
            jobs.append(((o[0], o[1], TOM[0], TOM[1]), s))
            jobs.append(((BASE[0], BASE[1], o[0], o[1]), s))
            jobs.append(((o[0], o[1], BASE[0], BASE[1]), s))
    with ProcessPoolExecutor(max_workers=6) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/tom_test.json", "w"), indent=1)

    print("== head-to-head (tom vs base) ==")
    for (x, o) in ((TOM, BASE), (BASE, TOM)):
        g = [r for r in rows if (r["a"], r["b"]) == (x[0], o[0])]
        w = sum(r["ra"] > r["rb"] for r in g)
        m = sum(r["ra"] - r["rb"] for r in g) / max(1, len(g))
        print(f"  {x[0]} seat0 vs {o[0]}: {w}-{len(g)-w} margin {m:+.0f}")
    w_tot = sum(r["ra"] > r["rb"] for r in rows if r["a"] == "tom" and r["b"] == "base") + \
            sum(r["rb"] > r["ra"] for r in rows if r["a"] == "base" and r["b"] == "tom")
    m_tot = sum(r["ra"] - r["rb"] for r in rows if r["a"] == "tom" and r["b"] == "base") + \
            sum(r["rb"] - r["ra"] for r in rows if r["a"] == "base" and r["b"] == "tom")
    print(f"  TOM overall: {w_tot}-{40 - w_tot} wins, total margin {m_tot:+.0f}")
    print("== vs opponents (x's margin) ==")
    for o in OPP:
        for x in (TOM, BASE):
            g = [r for r in rows if (r["a"], r["b"]) == (x[0], o[0])] + [r for r in rows if (r["a"], r["b"]) == (o[0], x[0])]
            wm = sum((r["ra"] - r["rb"]) if r["a"] == x[0] else (r["rb"] - r["ra"]) for r in g) / len(g)
            wins = sum(((r["ra"] > r["rb"]) if r["a"] == x[0] else (r["rb"] > r["ra"])) for r in g)
            print(f"  {x[0]} vs {o[0]}: {wins}-{len(g)-wins} mean margin {wm:+.0f}")
