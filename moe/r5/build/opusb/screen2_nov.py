"""moe/r4/screen2.py, verbatim fit/bootstrap/mapping, with all writes redirected to moe/r5/build/opusb/ (opusb's
write sandbox). Stage-1 rows (candidate vs C1, seeds 9100001..20, sw=0) are produced here instead of being read from
moe/r4/screen1.jsonl, via the same rr.job. Also prints which RR seeds the candidate changed vs C1's own rows.
usage: screen2_nov.py NAME PATH [WORKERS]"""
import json, os, sys, random, io, contextlib
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
B = "moe/r5/build/opusb"
sys.path.insert(0, ROOT + "/moe/r4/build/opus"); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
import rr
from concurrent.futures import ProcessPoolExecutor
ANCH = dict(shep="subW_shepherd.py", hyb="subX_hyb2965.py", f55V2="subV2_f55rec.py", sirV1="subV_sir2.py", pipe16="subK2_pipe16.py")
LIVE = dict(shep=2100, hyb=1974, f55V2=1930, sirV1=1897, pipe16=1800)
SEEDS = range(9100001, 9100021)

def mapped(rows, cand):
    tmp = B + "/_fit_tmp.jsonl"
    with open(tmp, "w") as f:
        for r in rows: f.write(json.dumps(r) + "\n")
    with contextlib.redirect_stdout(io.StringIO()): elo = rr.fit(tmp)
    xs = [elo[k] for k in LIVE]; ys = [LIVE[k] for k in LIVE]
    mx, my = sum(xs) / 5, sum(ys) / 5
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my + b * (elo[cand] - mx)

if __name__ == "__main__":
    os.nice(10)
    name, path = sys.argv[1], sys.argv[2]; W = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    out = f"{B}/screen2_{name}.jsonl"
    done = {(r["b"], r["seed"]) for r in map(json.loads, open(out))} if os.path.exists(out) else set()
    jobs = [((name, path), (a, p), s, 0) for a, p in ANCH.items() for s in SEEDS]
    jobs += [((name, path), ("C1", "subY_C1_predict2.py"), s, 0) for s in SEEDS]   # stage-1 rows
    jobs = [j for j in jobs if (j[1][0], j[2]) not in done]
    if jobs:
        with ProcessPoolExecutor(max_workers=W) as ex, open(out, "a") as f:
            for r in ex.map(rr.job, jobs, chunksize=1):
                f.write(json.dumps(r) + "\n"); r2 = dict(r, sw=1); f.write(json.dumps(r2) + "\n"); f.flush()
    base = [json.loads(l) for l in open("moe/r4/build/opus/rr_retro.jsonl")]
    base = [r for r in base if "err" not in r]
    cand = [json.loads(l) for l in open(out)]; cand = [r for r in cand if "err" not in r]
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
    # paired vs C1's own rows in the base RR (same seeds, same anchors, sw=0)
    c1rows = {}
    for r in base:
        if r["sw"] == 0 and "C1" in (r["a"], r["b"]):
            opp = r["b"] if r["a"] == "C1" else r["a"]
            me, th = (r["ra"], r["rb"]) if r["a"] == "C1" else (r["rb"], r["ra"])
            c1rows[(opp, r["seed"])] = (me, th)
    changed = {}
    for a in ANCH:
        g = [r for r in cand if r["b"] == a and r["sw"] == 0]
        w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
        ch = [(r["seed"], r["ra"] - c1rows[(a, r["seed"])][0], (r["ra"] - r["rb"]) - (c1rows[(a, r["seed"])][0] - c1rows[(a, r["seed"])][1]),
               (c1rows[(a, r["seed"])][0] > c1rows[(a, r["seed"])][1]) - (c1rows[(a, r["seed"])][0] < c1rows[(a, r["seed"])][1]),
               (r["ra"] > r["rb"]) - (r["ra"] < r["rb"]))
              for r in g if (a, r["seed"]) in c1rows and (r["ra"], r["rb"]) != c1rows[(a, r["seed"])]]
        changed[a] = ch
        print(f"  {name} vs {a:7}: {w}-{l}-{len(g)-w-l}  mean {sum(r['ra']-r['rb'] for r in g)/max(1,len(g)):+.0f}"
              f"   changed vs C1's row: {len(ch)}/{len(g)}  (seed, dbank, dmargin, C1 result, cand result) {ch}")
    g = [r for r in cand if r["b"] == "C1" and r["sw"] == 0]
    w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
    print(f"  {name} vs C1     : {w}-{l}-{len(g)-w-l}  mean {sum(r['ra']-r['rb'] for r in g)/max(1,len(g)):+.0f}   non-tied seeds "
          f"{[(r['seed'], r['ra'] - r['rb']) for r in g if r['ra'] != r['rb']]}")
    print(f"errors: {errs}")
    print(f"C1  mapped {c1:.0f}  90% CI [{bc[int(.05*len(bc))]:.0f}, {bc[int(.95*len(bc))-1]:.0f}]")
    print(f"{name} mapped {point:.0f}  90% CI [{lo:.0f}, {hi:.0f}]  -> GATE (lb > 2148): {'PASS' if lo > 2148 else 'FAIL'}")
    d = sorted(x - y for x, y in zip(bs, bc))
    print(f"{name} - C1 mapped (paired bootstrap) {point - c1:+.0f}  90% CI [{d[int(.05*len(d))]:+.0f}, {d[int(.95*len(d))-1]:+.0f}]")
