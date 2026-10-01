# First-pass diff: what do v8's live-loss opponents do that v8 doesn't (and vice versa on wins)?
import gzip, json, glob, sys
from collections import Counter, defaultdict

D = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/mine/rawkeep/v8live"
LOSSES = {115108510,115047026,114954602,114932778,114930144,114903322,114884534,
          114874014,114868203,114864488,114854823,114855765,114853872}

def opcls(op):
    if not op: return "?"
    k = op[0]
    return f"{k}:{op[1]}" if k in ("PLANT","PICKUP","PLACE","BUY_SEED","BUY_ANIMAL","BUY_PRODUCT","SELL") else k

def profile(rec, seat):
    """per-day bank + cumulative op counts + composition checkpoints for `seat`."""
    days = defaultdict(lambda: {"ops": Counter(), "mkt": Counter(), "money": None})
    steps = rec["steps"]
    for t, s in enumerate(steps):
        o = s[seat].get("observation") or {}
        a = s[seat].get("action") or {}
        d = t // 24
        days[d]["money"] = (o.get("farms") or [{}])[0 if seat == 0 else 0]  # money read below properly
        obs_farms = o.get("farms") or []
        if len(obs_farms) > seat:
            days[d]["money"] = obs_farms[seat].get("money")
        for u in ([a.get("farmer")] + list(a.get("hands") or [])):
            if u: days[d]["ops"][opcls(u)] += 1
        for m in (a.get("market") or []):
            days[d]["mkt"][opcls(m)] += 1
    # final composition
    fo = (steps[-1][seat].get("observation") or {}).get("farms") or []
    comp = Counter(); tiles_used = 0
    if len(fo) > seat:
        for row in fo[seat].get("tiles") or []:
            for t in row:
                if t is None: continue
                if not isinstance(t, dict): continue
                tiles_used += 1
                k = t.get("kind")
                if k == "PLANT": comp["P:" + str(t.get("crop"))] += 1
                elif k in ("COOP","PASTURE"):
                    a = t.get("animal")
                    comp["A:" + str(a if isinstance(a, str) else (a or {}).get("kind") or ("empty"+k))] += 1
                else: comp[k] += 1
    return days, comp, fo[seat].get("unlocked_quadrants") if len(fo) > seat else []

def bank_curve(days):
    return [days[d]["money"] for d in sorted(days)]

agg_l = {"v8": Counter(), "opp": Counter()}; agg_w = {"v8": Counter(), "opp": Counter()}
print("=== LOSSES (seat col: ours=winner seat is opp) ===")
for f in sorted(glob.glob(D + "/*.json.gz")):
    rec = json.load(gzip.open(f))
    ep = rec["episode_id"]
    if ep not in LOSSES: continue
    seat = rec["teams"].index("Sam-wiz"); o = 1 - seat
    dv, cv, qv = profile(rec, seat); do, co, qo = profile(rec, o)
    for d in range(30):
        agg_l["v8"].update(dv[d]["ops"]); agg_l["opp"].update(do[d]["ops"])
    bv, bo = bank_curve(dv), bank_curve(do)
    # find first day opp bank exceeds ours and stays
    cross = next((d for d in range(30) if bo[d] and bv[d] and bo[d] > bv[d] + 2000), None)
    print(f"ep{ep} vs {rec['teams'][o][:20]:22} margin {rec['rewards'][o]-rec['rewards'][seat]:+7.0f} "
          f"cross@{cross} quads us{len(qv)}/them{len(qo)} | us {dict(cv)} | them {dict(co)}")

print("\n=== WINS ===")
for f in sorted(glob.glob(D + "/*.json.gz")):
    rec = json.load(gzip.open(f))
    ep = rec["episode_id"]
    if ep in LOSSES: continue
    seat = rec["teams"].index("Sam-wiz"); o = 1 - seat
    dv, cv, qv = profile(rec, seat); do, co, qo = profile(rec, o)
    for d in range(30):
        agg_w["v8"].update(dv[d]["ops"]); agg_w["opp"].update(do[d]["ops"])
    bv, bo = bank_curve(dv), bank_curve(do)
    cross = next((d for d in range(30) if bv[d] and bo[d] and bv[d] > bo[d] + 2000), None)
    print(f"ep{ep} vs {rec['teams'][o][:20]:22} margin {rec['rewards'][seat]-rec['rewards'][o]:+7.0f} "
          f"lead@{cross} quads us{len(qv)}/them{len(qo)} | us {dict(cv)} | them {dict(co)}")

print("\n=== op-count contrast (losses): opp minus v8 ===")
for k in sorted(set(agg_l["opp"]) | set(agg_l["v8"])):
    d = agg_l["opp"][k] - agg_l["v8"][k]
    if abs(d) > 50: print(f"  {k:24} {d:+6}")
print("=== op-count contrast (wins): v8 minus loser ===")
for k in sorted(set(agg_w["v8"]) | set(agg_w["opp"])):
    d = agg_w["v8"][k] - agg_w["opp"][k]
    if abs(d) > 50: print(f"  {k:24} {d:+6}")
