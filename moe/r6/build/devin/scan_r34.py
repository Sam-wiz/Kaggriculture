# Scan mine/top10 episodes for r34v8's day-0 signature:
# step-0 market has >=3 HIRE, BUY_ANIMAL COW >=2, BUY_ANIMAL SHEEP >=3, BUY_SEED MELON >=4
import gzip, json, os, sys
from collections import Counter, defaultdict

D = "mine/top10"
files = sorted(os.listdir(D))
teams_hit = Counter(); hits = []; n = 0
for fn in files:
    try:
        d = json.load(gzip.open(os.path.join(D, fn)))
    except Exception:
        continue
    n += 1
    acts = d.get("actions") or []
    if not acts:
        continue
    for seat in (0, 1):
        try:
            m0 = acts[0][seat].get("market") or []
        except Exception:
            continue
        hires = sum(1 for o in m0 if o and o[0] == "HIRE")
        cow = sum(int(o[2]) for o in m0 if o and o[0] == "BUY_ANIMAL" and o[1] == "COW")
        sheep = sum(int(o[2]) for o in m0 if o and o[0] == "BUY_ANIMAL" and o[1] == "SHEEP")
        melon = sum(int(o[2]) for o in m0 if o and o[0] == "BUY_SEED" and o[1] == "MELON")
        if hires >= 3 and cow >= 2 and sheep >= 3 and melon >= 4:
            t = d["teams"][seat]
            teams_hit[t] += 1
            hits.append((d["episode_id"], d["date"], t, seat, hires, cow, sheep, melon))
print("episodes scanned:", n, "| hits:", len(hits))
for t, c in teams_hit.most_common():
    print(f"  {t}: {c}")
for h in hits[:15]:
    print(h)
