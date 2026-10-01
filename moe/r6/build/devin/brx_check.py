# BRX2-on-m30 firecheck + h2h vs m30 and bare Harvest, seeds 9100001-20, seat 0.
import json, sys, os, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from concurrent.futures import ProcessPoolExecutor

def job(arg):
    from run import load, act
    import kagsim
    (na, pa, nb, pb), seed = arg; t0 = time.time()
    a, ma = load(pa, "a"); b, mb = load(pb, "b")
    g = kagsim.Game(seed=int(seed))
    for t in range(719):
        g.step(act(a, g.observe(0)), act(b, g.observe(1)))
    return dict(a=na, b=nb, seed=seed, ra=float(g.reward(0)), rb=float(g.reward(1)),
                brx=dict(getattr(ma, "_BRX_STATS", {}) or {}), sec=round(time.time()-t0))

if __name__ == "__main__":
    os.nice(10)
    X = ("M30B", "moe/r6/build/devin/harvest_m30_brx2.py")
    seeds = range(9100001, 9100021)
    jobs = [((X[0], X[1], opp, op), s) for opp, op in
            (("m30", "moe/r6/build/devin/harvest_m30.py"), ("H", "subAA_harvest.py"), ("C1R2", "subZ_C1R2.py"))
            for s in seeds]
    with ProcessPoolExecutor(max_workers=4) as ex, open("moe/r6/build/devin/brx_check.jsonl", "w") as f:
        for r in ex.map(job, jobs, chunksize=1):
            f.write(json.dumps(r) + "\n"); f.flush()
    rows = [json.loads(l) for l in open("moe/r6/build/devin/brx_check.jsonl")]
    for opp in ("m30", "H", "C1R2"):
        g = [r for r in rows if r["b"] == opp]
        w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
        mg = sum(r["ra"] - r["rb"] for r in g) / max(1, len(g))
        print(f"M30B vs {opp:5}: {w}-{l}-{len(g)-w-l}  mean {mg:+.0f}")
    st = rows[0]["brx"]
    print("BRX turns/multi/changed/fallback/err (game 1):", st)
    tot = {}
    for r in rows:
        for k, v in r["brx"].items(): tot[k] = tot.get(k, 0) + v
    print("BRX totals:", tot)
