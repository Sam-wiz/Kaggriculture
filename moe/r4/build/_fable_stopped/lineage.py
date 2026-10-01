"""Cluster dump seats into lineages by (land-buy days, hires/day d0-11) and map teams to the LB snapshot."""
import json, gzip, glob, collections, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from farmplan import summarize
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
lb = json.load(open(f"{ROOT}/moe/r3/lb_0926_0500.json"))
files = sorted(glob.glob(f"{ROOT}/mine/top10/*.json.gz"))
sig = collections.defaultdict(list); team_sig = collections.defaultdict(collections.Counter)
for p in files:
    d = json.load(gzip.open(p, "rt"))
    for s in (0, 1):
        o = summarize(d, s)
        k = (tuple(o["land"]), tuple(o["hires_by_day"][:12]))
        sig[k].append((o["team"], o["bank"])); team_sig[o["team"]][k] += 1
print(len(files), "episodes;", len(sig), "signatures")
for k, v in sorted(sig.items(), key=lambda kv: -len(kv[1])):
    teams = collections.Counter(t for t, _ in v)
    print(f"n={len(v):3d} land={k[0]} hires0-11={k[1]}  teams={dict(teams.most_common(6))}")
print("\nteam -> rating, #seats, #signatures")
for t, c in sorted(team_sig.items(), key=lambda kv: -lb.get(kv[0], 0)):
    print(f"  {t:28s} {lb.get(t, 0):6.0f} seats={sum(c.values()):3d} sigs={len(c)}")
