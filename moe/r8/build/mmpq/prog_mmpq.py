"""EXECUTED-program extraction for MMPQ from rawkeep replays (full obs).

Per episode, per day:
  - hires_executed   = max(hires_today) seen in MMPQ's own farm obs that day
  - land buys        = day + which quadrant unlocked (obs delta)
  - structures built = new COOP/PASTURE tiles appearing (day)
  - animals placed   = animal appearing on a structure tile (day, species)
  - plants           = new PLANT tiles appearing (day, crop) -- catches crops
                       later harvested/dug; dedup via (x,y) transition scan
  - sells executed   = shed bookkeeping: shed[t]-shed[t-1] minus unit-op
                       transfers (PICKUP subtracts, PLACE-adjacent/DROP adds);
                       negative residual = units sold that turn
  - money trajectory per day, plus issued-vs-executed market order stats
Writes per-ep JSON to build/mmpq/exec_MMPQ.json + aggregate stdout.
"""
import gzip, json, glob, sys
from collections import Counter, defaultdict

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
TEAM = "M & M & P & Q"
FILES = ["109508082", "109763722", "111099760", "111414755"]
CROPS = ["WHEAT","CARROT","TOMATO","STRAWBERRY","MELON"]
ANIMALS = ["GOOSE","COW","SHEEP"]
CENTERS = {(4,4),(5,4),(4,5),(5,5)}
QUADCOST = {"NE":1000,"SW":2000,"SE":4000}

def quad_of(x, y):
    return ("N" if y < 5 else "S") + ("W" if x < 5 else "E")

def farm_animals(me):
    n = Counter()
    for row in me["tiles"]:
        for t in row:
            if isinstance(t, dict) and t.get("animal") in ANIMALS:
                n[t["animal"]] += 1
    return n

def tilemap(me):
    """(x,y) -> compact tile signature for delta detection."""
    m = {}
    for y, row in enumerate(me["tiles"]):
        for x, t in enumerate(row):
            if isinstance(t, dict):
                m[(x,y)] = t
    return m

eps_out = []
for fid in FILES:
    x = json.loads(gzip.open(f"{ROOT}/mine/rawkeep/{fid}.json.gz").read())
    teams = x["info"]["TeamNames"]; pi = teams.index(TEAM)
    seed = x["info"]["seed"]; ep = x["info"]["EpisodeId"]
    steps = x["steps"]

    hires_by_day   = defaultdict(int)
    quads_by_day   = {}
    prev_quads     = None
    land_buys      = []           # (day, quadrant)
    structs        = []           # (day, kind, x, y)
    animals_placed = []           # (day, species, x, y)
    plants         = []           # (day, crop, x, y)
    digs           = []           # (day, removed_kind, x, y) approx via disappearance
    prev_map       = None
    money_eod      = {}           # day -> money at last obs of day
    shed_sold      = Counter()    # product -> units leaving shed not via pickup
    shed_in        = Counter()    # product -> units entering shed unexplained (buys)
    shed_prev      = None
    prev_invs      = None
    prev_act       = None
    prev_me        = None
    issued         = Counter()    # issued market order kinds
    issued_qty     = Counter()
    sell_price_seen = defaultdict(list)   # product -> price at issue turn
    hire_fire_hours = defaultdict(list)   # day -> hours where HIRE order issued
    buy_animal_issued = Counter()
    buy_animal_hours  = defaultdict(list)

    for t, step in enumerate(steps):
        if pi >= len(step): break
        p = step[pi]
        obs = p.get("observation") or {}
        act = p.get("action") or {}
        if not obs: continue
        me = obs["farms"][pi]
        day, hour = obs["day"], obs["hour"]
        money_eod[day] = me["money"]
        hires_by_day[day] = max(hires_by_day[day], me.get("hires_today") or 0)

        quads = set(me.get("unlocked_quadrants") or [])
        if prev_quads is not None and len(quads) > len(prev_quads):
            for q in quads - prev_quads:
                land_buys.append((day, q))
        prev_quads = quads

        tm = tilemap(me)
        if prev_map is not None:
            for (tx,ty), cur in tm.items():
                old = prev_map.get((tx,ty))
                ok = old.get("kind") if isinstance(old,dict) else old
                ck = cur.get("kind")
                if ck == "PLANT" and ok != "PLANT":
                    plants.append((day, cur.get("crop"), tx, ty))
                if ck in ("COOP","PASTURE") and ok != ck:
                    structs.append((day, ck, tx, ty))
                if ck in ("COOP","PASTURE"):
                    a, oa = cur.get("animal"), (old or {}).get("animal") if isinstance(old,dict) else None
                    if a and not oa:
                        animals_placed.append((day, a, tx, ty))
        prev_map = tm

        # market orders issued
        for o in (act.get("market") or []):
            if not isinstance(o, (list,tuple)) or not o: continue
            k = o[0]; issued[k] += 1
            if k == "HIRE": hire_fire_hours[day].append(hour)
            elif k == "BUY_ANIMAL":
                buy_animal_issued[o[1]] += 1; buy_animal_hours[o[1]].append((day,hour))
            elif k == "SELL":
                issued_qty[f"SELL:{o[1]}"] += (o[2] if len(o)>2 else 1)
                pr = (obs.get("market") or {}).get("prices") or {}
                if o[1] in pr: sell_price_seen[o[1]].append(pr[o[1]])
            elif k == "BUY_SEED": issued_qty[f"SEED:{o[1]}"] += (o[2] if len(o)>2 else 1)
            elif k == "BUY_PRODUCT": issued_qty[f"BUYPR:{o[1]}"] += (o[2] if len(o)>2 else 1)

        # executed sells via shed bookkeeping. obs[t] is POST-action[t]
        # (verified: act[3] pickups already absent from obs[3].shed), so
        # delta shed[t]-shed[t-1] is caused by THIS step's ops + SELL fills.
        priv = obs.get("private") or {}
        shed = priv.get("shed") or {}
        units = [me["farmer"]] + list(me.get("hands") or [])
        if shed_prev is not None and prev_act is not None:
            delta = Counter()
            for k,v in shed.items(): delta[k] += v
            for k,v in shed_prev.items(): delta[k] -= v
            ops = [act.get("farmer")] + list(act.get("hands") or [])
            for ui,op in enumerate(ops):
                if not isinstance(op,(list,tuple)) or not op: continue
                pos = units[ui] if ui < len(units) else None
                on_center = isinstance(pos,(list,tuple)) and (int(pos[0]),int(pos[1])) in CENTERS
                if op[0] == "PICKUP" and len(op)>1:
                    n = op[2] if len(op)>2 else 1
                    delta[op[1]] += n          # shed lost n -> undo
                elif op[0] == "DROP" and on_center and prev_invs and ui < len(prev_invs):
                    for k,v in (prev_invs[ui] or {}).items():
                        delta[k] -= v          # shed gained inv -> undo
                elif op[0] == "PLACE" and len(op)>1 and on_center:
                    n = op[2] if len(op)>2 else 1
                    t0 = prev_me["tiles"][int(pos[1])][int(pos[0])]
                    # animal onto matching empty structure: from inv, no shed
                    # delta. Otherwise (incl. bare center tile) -> shed deposit.
                    on_struct = isinstance(t0,dict) and t0.get("kind") in ("COOP","PASTURE") and not t0.get("animal")
                    if not (op[1] in ANIMALS and on_struct):
                        delta[op[1]] -= n
            # day rollover: dismissed hands' inventories auto-deposit to shed
            if obs["hour"] == 0 and prev_invs:
                for ui,inv in enumerate(prev_invs):
                    if ui == 0: continue        # farmer survives
                    if not isinstance(inv, dict): continue
                    # unit may still exist (unlikely) — deposit applies to hands
                    for k,v in inv.items():
                        delta[k] -= v
            for k,v in delta.items():
                if v < 0:
                    if k not in ANIMALS:       # no SELL-animal orders exist;
                        shed_sold[k] += -v     # animal residuals are artifacts
                elif v > 0: shed_in[k] += v    # unexplained gain = market buy fill
        shed_prev = dict(shed)
        prev_invs = priv.get("inventories") or []
        prev_act = act
        prev_me = me

    # aggregates
    plants_by_crop = Counter(p[1] for p in plants)
    plant_days = defaultdict(list)
    for d,c,_,_ in plants: plant_days[c].append(d)
    anim_by_sp = Counter(a[1] for a in animals_placed)
    anim_days = defaultdict(list)
    for d,a,_,_ in animals_placed: anim_days[a].append(d)
    struct_by_kind = Counter(s[1] for s in structs)
    struct_days = defaultdict(list)
    for d,k,_,_ in structs: struct_days[k].append(d)

    eps_out.append({
        "ep": ep, "seed": seed, "opp": teams[1-pi],
        "reward": x["rewards"][pi], "opp_reward": x["rewards"][1-pi],
        "hires": {d: hires_by_day[d] for d in sorted(hires_by_day)},
        "land_buys": land_buys,
        "structs": [(d,k) for d,k,_,_ in structs],
        "animals_placed": [(d,a) for d,a,_,_ in animals_placed],
        "plants": [(d,c) for d,c,_,_ in plants],
        "money_eod": money_eod,
        "shed_sold": dict(shed_sold), "shed_in": dict(shed_in),
        "issued": dict(issued), "issued_qty": dict(issued_qty),
        "hire_fire_hours": {d: sorted(set(h)) for d,h in sorted(hire_fire_hours.items())},
        "buy_animal_hours": {a: v for a,v in buy_animal_hours.items()},
        "sell_price_seen": {k: v for k,v in sell_price_seen.items()},
    })

json.dump(eps_out, open(f"{ROOT}/moe/r8/build/mmpq/exec_MMPQ.json","w"), indent=1)

# ---- aggregate print ----
print(f"=== MMPQ executed program over {len(eps_out)} eps ===")
for e in eps_out:
    print(f"\n--- ep {e['ep']} vs {e['opp']}  reward {e['reward']:.0f} vs {e['opp_reward']:.0f} ---")
    print(" hires/day:", [e["hires"].get(d,0) for d in range(30)])
    print(" land:", e["land_buys"], " structs:", Counter(k for _,k in e["structs"]))
    print(" animals placed:", Counter(a for _,a in e["animals_placed"]))
    ad = defaultdict(list)
    for d,a in e["animals_placed"]: ad[a].append(d)
    print("   animal days:", {a:(min(v),max(v)) for a,v in ad.items()})
    pc = Counter(c for _,c in e["plants"])
    pd = defaultdict(list)
    for d,c in e["plants"]: pd[c].append(d)
    print(" plants:", dict(pc))
    print("   plant day windows:", {c:(min(v),max(v)) for c,v in pd.items()})
    print(" shed_sold:", e["shed_sold"])
    print(" shed_in(buys):", e["shed_in"])
    print(" issued:", e["issued"])
    print(" money d0,5,10,15,20,25,29:", [round(e["money_eod"].get(d,0)) for d in [0,5,10,15,20,25,29]])
