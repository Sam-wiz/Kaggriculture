# Decode every team's season program from ds_*.jsonl (obs->action per turn, both seats).
# Per team: hire ramp, land days, animal windows/counts, plant windows/volumes, sell rhythm.
import json, os, collections, glob, sys

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
DIR = ROOT + "/mine/rawkeep/by_team"

def decode(path):
    eps = collections.defaultdict(lambda: collections.defaultdict(lambda: {
        "hire": 0, "land": 0, "animals": collections.Counter(), "plants": collections.Counter(),
        "sells": collections.Counter(), "sell_n": 0, "builds": collections.Counter(),
        "pickup_animal": 0, "money_end": 0}))
    epset = set()
    for line in open(path):
        r = json.loads(line)
        f = r["f"]; ep = f["ep"]; d = f["day"]
        epset.add(ep)
        E = eps[ep][d]
        E["money_end"] = max(E["money_end"], f["money"])
        for op in r["market"]:
            if not isinstance(op, list) or not op: continue
            k = op[0]
            if k == "HIRE": E["hire"] += 1
            elif k == "BUY_LAND": E["land"] += 1
            elif k == "BUY_ANIMAL": E["animals"][op[1]] += op[2]
            elif k == "BUY_SEED": pass
            elif k == "BUY_PRODUCT": pass
            elif k == "SELL": E["sells"][op[1]] += op[2]; E["sell_n"] += 1
        for u in r["uops"]:
            if not isinstance(u, list) or len(u) < 2 or not isinstance(u[1], list) or not u[1]: continue
            a = u[1][0]
            if a == "PLANT": E["plants"][u[1][1]] += 1
            elif a in ("BUILD_PASTURE", "BUILD_COOP"): E["builds"][a] += 1
    # aggregate
    days = collections.defaultdict(lambda: {"hire": 0, "land": 0, "animals": collections.Counter(),
        "plants": collections.Counter(), "sells": collections.Counter(), "eps": set()})
    for ep, dd in eps.items():
        for d, E in dd.items():
            D = days[d]; D["eps"].add(ep)
            D["hire"] += E["hire"]; D["land"] += E["land"]
            for k, v in E["animals"].items(): D["animals"][k] += v
            for k, v in E["plants"].items(): D["plants"][k] += v
            for k, v in E["sells"].items(): D["sells"][k] += v
    n_ep = len(epset)
    hires = [round(days[d]["hire"] / max(1, len(days[d]["eps"])), 1) for d in sorted(days) if days[d]["hire"] or d < 6]
    land_days = [d for d in sorted(days) if days[d]["land"] > 0]
    animals = collections.Counter(); plants = collections.Counter(); sells = collections.Counter()
    anim_days = collections.defaultdict(set); plant_days = collections.defaultdict(set)
    for d in sorted(days):
        for k, v in days[d]["animals"].items():
            animals[k] += v; anim_days[k].add(d)
        for k, v in days[d]["plants"].items():
            plants[k] += v; plant_days[k].add(d)
        for k, v in days[d]["sells"].items(): sells[k] += v
    return dict(n_ep=n_ep, hires=hires, land_days=land_days,
                animals={k: round(animals[k] / n_ep, 1) for k in animals},
                animal_windows={k: (min(anim_days[k]), max(anim_days[k])) for k in anim_days},
                plants={k: round(plants[k] / n_ep, 1) for k in plants},
                plant_windows={k: (min(plant_days[k]), max(plant_days[k])) for k in plant_days},
                sells={k: round(sells[k] / n_ep, 1) for k in sells})

def main():
    files = sorted(glob.glob(DIR + "/ds_*.jsonl"), key=lambda p: -os.path.getsize(p))
    out = {}
    for p in files[:18]:
        team = os.path.basename(p)[3:-6]
        try:
            r = decode(p)
            if r["n_ep"] < 5: continue
            out[team] = r
        except Exception as e:
            print(team, "ERR", e, file=sys.stderr)
    json.dump(out, open(ROOT + "/moe/r7/build/devin/programs.json", "w"), indent=1)
    for team, r in out.items():
        print(f"\n=== {team} ({r['n_ep']} eps) ===")
        print(f"  hires/day: {r['hires']}")
        print(f"  land days: {r['land_days']}")
        print(f"  animals/ep: {r['animals']}  windows: {r['animal_windows']}")
        print(f"  plants/ep: {r['plants']}")
        print(f"  plant windows: {r['plant_windows']}")
        print(f"  sells/ep: {r['sells']}")

if __name__ == "__main__":
    main()
