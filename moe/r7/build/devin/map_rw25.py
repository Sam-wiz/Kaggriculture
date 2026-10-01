import json, os, sys, random, io, contextlib
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r4/build/opus"); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
import rr
from concurrent.futures import ProcessPoolExecutor
ANCH = dict(shep="subW_shepherd.py", hyb="subX_hyb2965.py", f55V2="subV2_f55rec.py", sirV1="subV_sir2.py", pipe16="subK2_pipe16.py", C1="subY_C1_predict2.py")
LIVE = dict(shep=2100, hyb=1974, f55V2=1930, sirV1=1897, pipe16=1800)
SEEDS = range(9100001, 9100021)
def mapped(rows, cand):
    tmp = "moe/r4/_fit_tmp.jsonl"
    with open(tmp, "w") as f:
        for r in rows: f.write(json.dumps(r) + "\n")
    with contextlib.redirect_stdout(io.StringIO()): elo = rr.fit(tmp)
    xs = [elo[k] for k in LIVE]; ys = [LIVE[k] for k in LIVE]
    mx, my = sum(xs) / 5, sum(ys) / 5
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my + b * (elo[cand] - mx)
if __name__ == "__main__":
    os.nice(10)
    name, path = "v8rw25", "moe/r7/build/devin/agents_v8_rw25.py"
    out = "moe/r7/build/devin/map_v8rw25.jsonl"
    if not os.path.exists(out):
        jobs = [((name, path), (a, p), s, 0) for a, p in ANCH.items() for s in SEEDS]
        with ProcessPoolExecutor(max_workers=5) as ex, open(out, "w") as f:
            for r in ex.map(rr.job, jobs, chunksize=1):
                f.write(json.dumps(r) + "\n"); f.write(json.dumps(dict(r, sw=1)) + "\n")
    base = [json.loads(l) for l in open("moe/r4/build/opus/rr_retro.jsonl") if "err" not in json.loads(l)]
    cand = [json.loads(l) for l in open(out)]; cand = [r for r in cand if "err" not in r]
    errs = sum(1 for l in open(out) if "err" in json.loads(l))
    allr = base + cand
    point = mapped(allr, name); c1 = mapped(allr, "C1")
    rng = random.Random(7); bs = []
    seeds = list(SEEDS)
    for _ in range(200):
        pick = [rng.choice(seeds) for _ in seeds]
        rows = [dict(r) for s in pick for r in allr if r["seed"] == s]
        try: bs.append(mapped(rows, name))
        except Exception: pass
    bs.sort(); lo, hi = bs[int(.05*len(bs))], bs[int(.95*len(bs))-1]
    for a in ANCH:
        g = [r for r in cand if r["b"] == a and r["sw"] == 0]
        w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
        print(f"  {name} vs {a:7}: {w}-{l}-{len(g)-w-l}  mean {sum(r['ra']-r['rb'] for r in g)/max(1,len(g)):+.0f}")
    print(f"errors: {errs}")
    print(f"{name} mapped {point:.0f}  90% CI [{lo:.0f}, {hi:.0f}]")
