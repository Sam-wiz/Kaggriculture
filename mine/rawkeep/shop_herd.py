# Shop-event -> herd-size extractor (opus's sketch).
# Per episode: shops unlocked by day D -> final herd per species (placed + shed + carried).
import gzip, json, glob, sys
from collections import defaultdict, Counter

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
D = int(sys.argv[1]) if len(sys.argv) > 1 else 12
ANIMALS = ["GOOSE","COW","SHEEP"]

def herd_at(step_obs, pi):
    me = step_obs["farms"][pi]; priv = step_obs.get("private") or {}
    n = {a:0 for a in ANIMALS}
    for row in me["tiles"]:
        for t in row:
            if isinstance(t,dict) and t.get("animal") in n: n[t["animal"]] += 1
    shed = priv.get("shed") or {}
    for a in ANIMALS: n[a] += shed.get(a,0)
    for inv in (priv.get("inventories") or []):
        for a in ANIMALS:
            if isinstance(inv,dict): n[a] += inv.get(a,0)
    return n

def shops_at(step_obs):
    return list(((step_obs.get("town") or {}).get("unlocked_shops")) or [])

rows = []
for f in sorted(glob.glob(f"{ROOT}/mine/rawkeep/*.json.gz")):
    try: x = json.loads(gzip.open(f).read())
    except Exception: continue
    teams = (x.get("info") or {}).get("TeamNames") or []
    steps = x["steps"]
    for pi,team in enumerate(teams):
        shops_byD = None; final = None; herd_d12 = None
        for t,step in enumerate(steps):
            if pi >= len(step): break
            obs = step[pi].get("observation") or {}
            if not obs: continue
            if obs.get("day")==D and obs.get("hour")==0:
                shops_byD = shops_at(obs); herd_d12 = herd_at(obs, pi)
            if t == len(steps)-1 or pi >= len(steps[min(t+1,len(steps)-1)]):
                pass
        # final herd = last step's obs for this seat
        last = None
        for t in range(len(steps)-1, 0, -1):
            if pi < len(steps[t]) and steps[t][pi].get("observation"):
                last = steps[t][pi]["observation"]; break
        if not last or shops_byD is None: continue
        final = herd_at(last, pi)
        # shops by end
        end_shops = shops_at(last)
        rows.append({"team":team,"ep":(x.get('info') or {}).get('EpisodeId'),
                     "shops_d12":shops_byD,"shops_end":end_shops,
                     "herd_d12":herd_d12,"herd_end":final})

# aggregate: per shop-composition class, mean final herd
by = defaultdict(list)
for r in rows:
    key = tuple(sorted(set(r["shops_d12"])))
    by[key].append((r["team"], r["herd_end"], r["herd_d12"]))
print(f"D={D}: {len(rows)} team-episodes")
agg = defaultdict(list)
for key,v in by.items():
    for team,h,hd in v:
        for s in set(key): agg[s].append((team,h,hd))
print(f"\n{'shop-classes present by d12 (n eps)':60s} -> mean end herd C/S/G")
# per-team table: shops-d12 set -> mean herd
from collections import defaultdict as dd
tab = dd(list)
for r in rows:
    tab[r["team"]].append(r)
for team in ["DSM","Vadim Vasilenko","SpaTaro","Unknown Mother-Goose","mtmr_s1","THIRD FARM CLUB","M & M & P & Q"]:
    rs = tab.get(team,[])
    if not rs: continue
    # split by presence of each shop type
    print(f"\n--- {team} ({len(rs)} eps) ---")
    for shop in ["YARN_STORE","PIZZA_SHOP","SMOOTHIE_SHOP","BAKERY","BRUNCH_SPOT","PET_CAFE","ICE_CREAM_SHOP","FARMERS_MARKET"]:
        yes = [r for r in rs if shop in r["shops_d12"]]
        no = [r for r in rs if shop not in r["shops_d12"]]
        if len(yes)<2 and len(no)<2: continue
        def mh(v,a): return round(sum(x["herd_end"][a] for x in v)/max(len(v),1),1) if v else "-"
        print(f"  {shop:15s} n={len(yes):2d}: C{mh(yes,'COW')} S{mh(yes,'SHEEP')} G{mh(yes,'GOOSE')}  |  no n={len(no):2d}: C{mh(no,'COW')} S{mh(no,'SHEEP')} G{mh(no,'GOOSE')}")
