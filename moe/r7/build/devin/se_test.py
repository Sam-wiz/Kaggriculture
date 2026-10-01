# SE-land patch eval: v8+SE vs v8-base paired on fresh seeds both seats,
# plus patched-vs-{shep,M30B} margins compared to base on the same seeds.
import json, sys, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from concurrent.futures import ProcessPoolExecutor

BASE = ("base", "subAC_v8.py")
SE = ("se", "moe/r7/build/devin/v8_se.py")
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
    # head-to-head both seats
    for s in seeds:
        jobs.append(((SE[0], SE[1], BASE[0], BASE[1]), s))
        jobs.append(((BASE[0], BASE[1], SE[0], SE[1]), s))
    # vs opponents both seats
    for o in OPP:
        for s in seeds:
            jobs.append(((SE[0], SE[1], o[0], o[1]), s))
            jobs.append(((o[0], o[1], SE[0], SE[1]), s))
            jobs.append(((BASE[0], BASE[1], o[0], o[1]), s))
            jobs.append(((o[0], o[1], BASE[0], BASE[1]), s))
    with ProcessPoolExecutor(max_workers=6) as ex:
        rows = list(ex.map(job, jobs, chunksize=1))
    json.dump(rows, open("moe/r7/build/devin/se_test.json", "w"), indent=1)

    def rep(x, o):
        g = [r for r in rows if (r["a"], r["b"]) == (x, o)]
        n = len(g)
        w = sum(r["ra"] > r["rb"] for r in g)
        mm = sum(r["ra"] - r["rb"] for r in g) / max(1, n)
        return w, n, mm
    print("== head-to-head (margin = se - base) ==")
    for (x, o) in ((SE, BASE), (BASE, SE)):
        w, n, m = rep(x[0], o[0]); print(f"  {x[0]} as seat0 vs {o[0]}: {w}-{n-w} margin {m:+.0f}")
    tot = sum(r["ra"] - r["rb"] for r in rows if r["a"] == "se" and r["b"] == "base") + \
          sum(r["rb"] - r["ra"] for r in rows if r["a"] == "base" and r["b"] == "se")
    print(f"  SE combined margin over 2 seats: {tot:+.0f} total")
    print("== vs opponents ==")
    for o in OPP:
        for x in (SE, BASE):
            g = [r for r in rows if (r["a"], r["b"]) == (x[0], o[0])] + [r for r in rows if (r["a"], r["b"]) == (o[0], x[0])]
            if not g: continue
            wm = sum((r["ra"] - r["rb"]) if r["a"] == x[0] else (r["rb"] - r["ra"]) for r in g) / len(g)
            wins = sum(((r["ra"] > r["rb"]) if r["a"] == x[0] else (r["rb"] > r["ra"])) for r in g)
            print(f"  {x[0]} vs {o[0]}: {wins}-{len(g)-wins} mean margin {wm:+.0f}")
