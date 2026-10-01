"""Does the premium-sell layer leak on low-premium-demand draws?

Pairs (f55rec, f55rec-noprem) x (V1, V2) against a fixed field opponent on the
same seeds, records the shop draw, and splits the margin delta by draw class.
low = fewer than 2 premium-consuming shops among the first 6 unlocked.
"""
import os, sys, collections
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

PREM_SHOPS = {"YARN_STORE", "PIZZA_SHOP", "ICE_CREAM_SHOP", "SMOOTHIE_SHOP",
              "BRUNCH_SPOT", "FARMERS_MARKET"}

CACHE = {}

def kload(path):
    if path not in CACHE:
        src = open(path).read()
        env = {"__file__": os.path.abspath(path)}
        exec(compile(src, path, "exec"), env)  # noqa: S102
        CACHE[path] = [v for v in env.values() if callable(v)][-1]
    return CACHE[path]

def job(a):
    cand, opp, s, sw = a
    ca, oa = kload(cand), kload(opp)
    x, y = (oa, ca) if sw else (ca, oa)
    r = harness.run_episode(x, y, seed=s, catch_errors=True)
    p, q = r["reward"][::-1] if sw else r["reward"]
    shops = list(r["state"][0].observation.town.get("unlocked_shops") or [])
    return cand, s, sw, p - q, shops[:6]

if __name__ == "__main__":
    opp = sys.argv[1] if len(sys.argv) > 1 else "rivals/koshinm_kaggriculture-local-best-2026-09-21/main.py"
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 6000
    nseeds = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    pairs = [
        ("subV_f55rec.py", "subV_f55rec_np.py"),
        ("subV2_f55rec.py", "subV2_f55rec_np.py"),
    ]
    jobs = [(c, opp, s, sw) for pair in pairs for c in pair
            for s in range(start, start + nseeds) for sw in (0, 1)]
    res = collections.defaultdict(dict)   # res[(cand)][(s,sw)] = (margin, shops6)
    with ProcessPoolExecutor(7) as ex:
        for cand, s, sw, m, shops6 in ex.map(job, jobs, chunksize=2):
            res[cand][(s, sw)] = (m, shops6)
    import json
    json.dump({c: {f"{s}_{w}": v for (s, w), v in d.items()} for c, d in res.items()},
              open("/tmp/prem_rows.json", "w"))
    for base, np_ in pairs:
        for thr in (2, 3, 4):
            rows = []
            for key, (m0, shops6) in res[base].items():
                m1, _ = res[np_][key]
                prem_ct = sum(1 for sh in shops6 if sh in PREM_SHOPS)
                rows.append((m1 - m0, prem_ct < thr))
            lo = [d for d, low in rows if low]
            hi = [d for d, low in rows if not low]
            def rep(v):
                w = sum(1 for x in v if x > 0)
                return f"n={len(v)} mean={sum(v)/len(v):+.0f} np-wins={w}" if v else "n=0"
            print(f"{base} thr<{thr}:  LOW {rep(lo)}   OTHER {rep(hi)}")
