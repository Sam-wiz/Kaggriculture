"""Paired analysis of a moe/gate.py --only-candidates --out JSON with exactly two candidates (cand, ctrl).
Rebuilds (i, j) from the deterministic job order. usage: paired.py out.json NSEEDS [pool_size=8]"""
import json, sys, itertools, statistics
res = json.load(open(sys.argv[1])); ns = int(sys.argv[2]); k = int(sys.argv[3]) if len(sys.argv) > 3 else 8
POOL = ["LIVE_f55rec_V2", "LIVE_sir_V1", "f55rec_V1", "sir_V2", "koshinm", "melon", "2802", "metav4"]
n = k + 2
pairs = [(i, j) for i, j in itertools.combinations(range(n), 2) if j >= k or i >= k]
jobs = [(i, j, s, sw) for i, j in pairs for s in range(ns) for sw in (0, 1)]
assert len(jobs) == len(res), (len(jobs), len(res))
M = {}
for (i, j, s, sw), r in zip(jobs, res):
    M[(i, j, s, sw)] = r[3]
w = lambda m: 1 if m > 0 else .5 if m == 0 else 0
print(f"{'opponent':16s}{'cand WR':>9s}{'ctrl WR':>9s}{'cand mean':>11s}{'ctrl mean':>11s}{'paired d':>10s}{'d>0':>6s}{'d<0':>6s}{'n':>5s}")
allc, allk = [], []
for i in range(k):
    c = [-M[(i, k, s, sw)] for s in range(ns) for sw in (0, 1) if M.get((i, k, s, sw)) is not None and M.get((i, k + 1, s, sw)) is not None]
    t = [-M[(i, k + 1, s, sw)] for s in range(ns) for sw in (0, 1) if M.get((i, k, s, sw)) is not None and M.get((i, k + 1, s, sw)) is not None]
    d = [a - b for a, b in zip(c, t)]
    allc += [w(x) for x in c]; allk += [w(x) for x in t]
    print(f"{POOL[i]:16s}{statistics.mean(map(w, c)):>9.3f}{statistics.mean(map(w, t)):>9.3f}{statistics.mean(c):>+11.0f}{statistics.mean(t):>+11.0f}{statistics.mean(d):>+10.0f}{sum(x > 0 for x in d):>6d}{sum(x < 0 for x in d):>6d}{len(d):>5d}")
cc = [-M[(k, k + 1, s, sw)] * -1 for s in range(ns) for sw in (0, 1) if M.get((k, k + 1, s, sw)) is not None]
# (k, k+1): margin = cand - ctrl already (row = cand)
cc = [M[(k, k + 1, s, sw)] for s in range(ns) for sw in (0, 1) if M.get((k, k + 1, s, sw)) is not None]
print(f"cand vs ctrl(sir2 copy): WR {statistics.mean(map(w, cc)):.3f}  mean {statistics.mean(cc):+.0f}  W/T/L {sum(x>0 for x in cc)}/{sum(x==0 for x in cc)}/{sum(x<0 for x in cc)}  n={len(cc)}")
print(f"mean WR vs pool (8): cand {statistics.mean(allc):.3f}  ctrl {statistics.mean(allk):.3f}")
