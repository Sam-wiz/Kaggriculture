"""Stage-2 (Claude Code): add a candidate to opus's pre-registered lineage RR (rr_retro.jsonl: 5 anchors + C1,
seeds 9100001..20, both sw rows), map BT->live on the anchors, bootstrap by SEED. sw=0 is played and
duplicated as sw=1 (bit-identical in kagsim) so weighting matches rr_retro. Gate: 90% CI lower bound > 2148."""
import json, os, sys, random, io, contextlib
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r4/build/opus"); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
import rr
from concurrent.futures import ProcessPoolExecutor
ANCH = dict(shep="subW_shepherd.py", hyb="subX_hyb2965.py", f55V2="subV2_f55rec.py", sirV1="subV_sir2.py", pipe16="subK2_pipe16.py")
LIVE = dict(shep=2100, hyb=1974, f55V2=1930, sirV1=1897, pipe16=1800)
SEEDS = range(9100001, 9100021)

def mapped(rows, cand):
    tmp = "moe/r6/build/opus/hv/_fit_tmp.jsonl"
    with open(tmp, "w") as f:
        for r in rows: f.write(json.dumps(r) + "\n")
    with contextlib.redirect_stdout(io.StringIO()): elo = rr.fit(tmp)
    xs = [elo[k] for k in LIVE]; ys = [LIVE[k] for k in LIVE]
    mx, my = sum(xs) / 5, sum(ys) / 5
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my + b * (elo[cand] - mx)

if __name__ == "__main__":
    os.nice(10)
    name, path = sys.argv[1], sys.argv[2]; W = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    out = f"moe/r6/build/opus/hv/screen2_{name}.jsonl"
    if not os.path.exists(out):
        jobs = [((name, path), (a, p), s, 0) for a, p in list(ANCH.items()) + [("C1", "subY_C1_predict2.py"), ("C1R2", "subZ_C1R2.py")] for s in SEEDS]
        with ProcessPoolExecutor(max_workers=W) as ex, open(out, "w") as f:
            for r in ex.map(rr.job, jobs, chunksize=1):
                f.write(json.dumps(r) + "\n"); r2 = dict(r, sw=1); f.write(json.dumps(r2) + "\n")
    base = [json.loads(l) for l in open("moe/r4/build/opus/rr_retro.jsonl")]
    base = [r for r in base if "err" not in r]
    cand = [json.loads(l) for l in open(out)]; cand = [r for r in cand if "err" not in r]; h2h = [r for r in cand if r["b"] == "C1R2" and r["sw"] == 0]; cand = [r for r in cand if r["b"] != "C1R2"]
    errs = sum(1 for l in open(out) if "err" in json.loads(l))
    allr = base + cand
    point = mapped(allr, name); c1 = mapped(allr, "C1")
    rng = random.Random(7); bs = []; bc = []
    seeds = list(SEEDS)
    for _ in range(200):
        pick = [rng.choice(seeds) for _ in seeds]
        rows = [dict(r) for s in pick for r in allr if r["seed"] == s]
        try: bs.append(mapped(rows, name)); bc.append(mapped(rows, "C1"))
        except Exception: pass
    bs.sort(); bc.sort(); lo, hi = bs[int(.05 * len(bs))], bs[int(.95 * len(bs)) - 1]
    for a in ANCH:
        g = [r for r in cand if r["b"] == a and r["sw"] == 0]
        w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
        print(f"  {name} vs {a:7}: {w}-{l}-{len(g)-w-l}  mean {sum(r['ra']-r['rb'] for r in g)/max(1,len(g)):+.0f}")
    for a in ("C1", "C1R2"):
        g = [r for r in (cand + h2h) if r["b"] == a and r["sw"] == 0]; w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
        print(f"  {name} vs {a:7}: {w}-{l}-{len(g)-w-l}  mean {sum(r['ra']-r['rb'] for r in g)/max(1,len(g)):+.0f}")
    print(f"errors: {errs}")
    print(f"C1  mapped {c1:.0f}  90% CI [{bc[int(.05*len(bc))]:.0f}, {bc[int(.95*len(bc))-1]:.0f}]")
    print(f"{name} mapped {point:.0f}  90% CI [{lo:.0f}, {hi:.0f}]  -> GATE (lb > 2148): {'PASS' if lo > 2148 else 'FAIL'}")
