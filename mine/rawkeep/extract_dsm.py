"""Extract (state-features -> market orders) dataset for a target team from raw replays."""
import gzip, json, glob, sys
from collections import Counter

TEAM = sys.argv[1] if len(sys.argv)>1 else "DSM"
OUT = open(f"mine/rawkeep/ds_{TEAM.replace(' ','_')}.jsonl","w")

PRODS = ["WHEAT","CARROT","TOMATO","STRAWBERRY","MELON","EGG","MILK","WOOL","FERTILIZER"]
rows = 0
for f in sorted(glob.glob("mine/rawkeep/*.json.gz")):
    try: x = json.load(gzip.open(f,"rt"))
    except: continue
    teams = x["info"]["TeamNames"]
    if TEAM not in teams: continue
    pi = teams.index(TEAM)
    seed = x["info"]["seed"]
    for t, step in enumerate(x["steps"]):
        p = step[pi]
        obs = p.get("observation") or {}
        act = p.get("action") or {}
        if not obs or not act: continue
        me = obs["farms"][pi]
        animals=Counter(); structs=Counter()
        for row in me["tiles"]:
            for tile in row:
                if isinstance(tile,dict):
                    if tile.get("kind") in ("COOP","PASTURE"): structs[tile["kind"]]+=1
                    an = tile.get("animal")
                    if an: animals[an if isinstance(an,str) else an.get("kind","?")]+=1
        feat = {
            "ep": x["info"]["EpisodeId"], "t": t, "seed": seed,
            "day": obs["day"], "hour": obs["hour"],
            "money": me["money"], "hires": me["hires_today"],
            "quads": len(me["unlocked_quadrants"]),
            "shops": obs["town"]["unlocked_shops"],
            "prices": obs["market"]["prices"], "minv": obs["market"]["inventory"],
            "shed": obs["private"]["shed"], "seeds": obs["private"]["seeds"],
            "animals": dict(animals), "structs": dict(structs),
        }
        orders = [o for o in (act.get("market") or []) if isinstance(o,(list,tuple))]
        unit = Counter()
        for op in [act.get("farmer")]+list(act.get("hands") or []):
            if isinstance(op,(list,tuple)) and op: unit[op[0]]+=1
        OUT.write(json.dumps({"f":feat,"market":orders,"unit":dict(unit)})+"\n")
        rows+=1
print("rows:", rows, "->", OUT.name)
