# _CA_MARGIN sweep on Harvest chassis: each variant vs bare Harvest + vs C1R2, seeds 9100001-20, seat 0.
# Kill test: a variant must beat bare Harvest materially before it deserves the full RR map.
import json, sys, os, time
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
        return dict(a=na, b=nb, seed=seed, err=repr(e)[:120])

if __name__ == "__main__":
    os.nice(10)
    V = {m: f"moe/r6/build/devin/harvest_m{m}.py" for m in ("30", "26", "18", "15")}
    seeds = range(9100001, 9100021)
    jobs = [((vn, vp, opp, op), s) for vn, vp in V.items()
            for opp, op in (("H", "subAA_harvest.py"), ("C1R2", "subZ_C1R2.py")) for s in seeds]
    with ProcessPoolExecutor(max_workers=4) as ex, open("moe/r6/build/devin/margin_sweep.jsonl", "w") as f:
        for r in ex.map(job, jobs, chunksize=1):
            f.write(json.dumps(r) + "\n"); f.flush()
    # summary
    rows = [json.loads(l) for l in open("moe/r6/build/devin/margin_sweep.jsonl")]
    for vn in V:
        for opp in ("H", "C1R2"):
            g = [r for r in rows if r["a"] == vn and r["b"] == opp and "err" not in r]
            w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
            mg = sum(r["ra"] - r["rb"] for r in g) / max(1, len(g))
            print(f"m{vn} vs {opp:5}: {w}-{l}-{len(g)-w-l}  mean {mg:+.0f}")
    print("errors:", sum(1 for r in rows if "err" in r))
