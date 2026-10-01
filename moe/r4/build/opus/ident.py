"""Pairwise per-step unit-op / market identity between recorded seats (plan determinism + family)."""
import gzip, json, glob, sys, itertools, collections, statistics as S
def uops(a):
    if not isinstance(a, dict): return None
    return json.dumps([a.get("farmer")] + list(a.get("hands") or []))
def mk(a):
    if not isinstance(a, dict): return None
    return json.dumps(a.get("market") or [])
seats = []
for p in sorted(glob.glob(sys.argv[1] if len(sys.argv) > 1 else "mine/top10/*.json.gz")):
    d = json.load(gzip.open(p, "rt"))
    for s in range(2):
        seats.append((d["teams"][s], d["episode_id"], [uops(x[s]) for x in d["actions"]], [mk(x[s]) for x in d["actions"]]))
def ident(a, b, lo=1, hi=720):
    n = sum(1 for t in range(lo, hi) if a[t] is not None)
    return sum(1 for t in range(lo, hi) if a[t] is not None and a[t] == b[t]) / max(1, n)
def prefix(a, b):
    for t in range(1, 720):
        if a[t] != b[t]: return t
    return 720
teams = sorted({s[0] for s in seats})
res = collections.defaultdict(list)
for x, y in itertools.combinations(seats, 2):
    k = tuple(sorted([x[0], y[0]]))
    res[k].append((ident(x[2], y[2]), ident(x[3], y[3]), prefix(x[2], y[2]), prefix(x[3], y[3]), ident(x[2], y[2], 1, 240), ident(x[2], y[2], 240, 720)))
for k, v in sorted(res.items(), key=lambda kv: -S.mean(z[0] for z in kv[1])):
    if len(v) < 2 and k[0] != k[1]: pass
    print(f"{k[0][:14]:14} ~ {k[1][:14]:14} n={len(v):3d} unit={S.mean(z[0] for z in v):.2f} (d0-9 {S.mean(z[4] for z in v):.2f}, d10-29 {S.mean(z[5] for z in v):.2f}) mkt={S.mean(z[1] for z in v):.2f} upre={S.median(z[2] for z in v):.0f} mpre={S.median(z[3] for z in v):.0f}")
