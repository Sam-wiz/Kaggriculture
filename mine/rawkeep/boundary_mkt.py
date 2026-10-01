# Boundary-recovery dataset: for each turn, covariates at obs[t-1] + which market
# orders fired at action[t]. Recovers `if price<X and cash>Y` clauses as
# fire/no-fire separations across 100+ games of natural price/cash variation.
import gzip, json, glob, os, sys
from collections import Counter

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
TEAM = sys.argv[1] if len(sys.argv) > 1 else "DSM"
OUT = sys.argv[2] if len(sys.argv) > 2 else f"mine/rawkeep/bounds_{TEAM}.jsonl"
PRODUCTS = ["EGGS","WHEAT","CARROT","TOMATO","STRAWBERRY","MELON","MILK","WOOL","FERTILIZER"]
ANIMALS = ["GOOSE","COW","SHEEP"]

if os.path.exists(OUT): os.remove(OUT)

def farm_counts(me):
    n_struct = {"COOP":0,"PASTURE":0}; n_free = {"COOP":0,"PASTURE":0}
    n_anim = {a:0 for a in ANIMALS}; n_plants = Counter(); n_ripe = 0; n_dry = 0
    for row in me["tiles"]:
        for t in row:
            if isinstance(t, dict):
                k = t.get("kind")
                if k in n_struct:
                    n_struct[k] += 1
                    a = t.get("animal")
                    if a: n_anim[a] += 1
                    else: n_free[k] += 1
                elif k == "PLANT":
                    n_plants[t["crop"]] += 1
                    if (t.get("yield_units") or 0) > 0: n_ripe += 1
                    if not t.get("watered_today"): n_dry += 1
    return n_struct, n_free, n_anim, n_plants, n_ripe, n_dry

files = sorted(glob.glob(f"{ROOT}/mine/rawkeep/*.json.gz"))
nrows = 0; eps = 0
out = open(OUT, "w")
for f in files:
    try: x = json.loads(gzip.open(f).read())
    except Exception: continue
    teams = (x.get("info") or {}).get("TeamNames") or []
    if TEAM not in teams: continue
    pi = teams.index(TEAM); eps += 1
    steps = x["steps"]
    for t in range(1, len(steps)):
        if pi >= len(steps[t]): break
        act = (steps[t][pi].get("action") or {})
        obs = (steps[t-1][pi].get("observation") or {})
        if not obs or not act: continue
        me = obs["farms"][pi]; priv = obs.get("private") or {}
        shed = priv.get("shed") or {}; seeds = priv.get("seeds") or {}
        mkt = obs.get("market") or {}
        n_struct, n_free, n_anim, n_plants, n_ripe, n_dry = farm_counts(me)
        cov = {
            "t": t, "day": obs["day"], "hour": obs["hour"],
            "money": me["money"], "hires": me.get("hires_today", 0),
            "n_units": 1 + len(me.get("hands") or []),
            "quads": len(me.get("unlocked_quadrants") or []),
            "prices": {p: (mkt.get("prices") or {}).get(p) for p in PRODUCTS},
            "mk_inv": {p: (mkt.get("inventory") or {}).get(p) for p in PRODUCTS},
            "shed": dict(shed), "seeds": dict(seeds),
            "coop": n_struct["COOP"], "coop_free": n_free["COOP"],
            "past": n_struct["PASTURE"], "past_free": n_free["PASTURE"],
            "animals": n_anim, "plants": dict(n_plants),
            "n_ripe": n_ripe, "n_dry": n_dry,
        }
        fires = Counter()
        for o in (act.get("market") or []):
            if isinstance(o, list) and o:
                fires["|".join(str(s) for s in o[:2])] += 1
        cov["fires"] = dict(fires)
        out.write(json.dumps(cov) + "\n"); nrows += 1
out.close()
print(f"{TEAM}: {eps} eps, {nrows} turn-rows -> {OUT}")
