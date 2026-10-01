"""Extract (state->action) rows for EVERY player in every raw replay."""
import gzip, json, glob, os, sys
from collections import Counter

OUT_DIR = "mine/rawkeep/by_team"; os.makedirs(OUT_DIR, exist_ok=True)
outs = {}
rows_by_team = Counter()
for f in sorted(glob.glob("mine/rawkeep/*.json.gz")):
    try: x = json.load(gzip.open(f,"rt"))
    except: continue
    teams = x["info"]["TeamNames"]
    if len(teams)!=2: continue
    for pi in range(2):
        team = teams[pi]
        if team not in outs:
            outs[team] = open(os.path.join(OUT_DIR, f"ds_{team.replace(' ','_')}.jsonl"), "w")
        out = outs[team]
        seed = x["info"]["seed"]
        for t, step in enumerate(x["steps"]):
            if pi >= len(step): break
            p = step[pi]; obs = p.get("observation") or {}; act = p.get("action") or {}
            if not obs or not act: continue
            me = obs["farms"][pi]
            animals=Counter(); structs=Counter()
            for row in me["tiles"]:
                for tile in row:
                    if isinstance(tile,dict):
                        if tile.get("kind") in ("COOP","PASTURE"): structs[tile["kind"]]+=1
                        an=tile.get("animal")
                        if an: animals[an if isinstance(an,str) else an.get("kind","?")]+=1
            units=[me["farmer"]]+list(me.get("hands") or [])
            ops=[act.get("farmer")]+list(act.get("hands") or [])
            uops=[]
            for pos,op in zip(units,ops):
                if isinstance(op,(list,tuple)) and op:
                    uops.append([pos, list(op)])
            feat={"ep":x["info"]["EpisodeId"],"t":t,"seed":seed,"day":obs["day"],"hour":obs["hour"],
                  "money":me["money"],"hires":me["hires_today"],"quads":len(me["unlocked_quadrants"]),
                  "shops":obs["town"]["unlocked_shops"],"prices":obs["market"]["prices"],
                  "minv":obs["market"]["inventory"],"shed":obs["private"]["shed"],
                  "seeds":obs["private"]["seeds"],"animals":dict(animals),"structs":dict(structs)}
            orders=[o for o in (act.get("market") or []) if isinstance(o,(list,tuple))]
            out.write(json.dumps({"f":feat,"market":orders,"uops":uops})+"\n")
            rows_by_team[team]+=1
for o in outs.values(): o.close()
for t,n in rows_by_team.most_common(30): print(f"{n:6d} {t}")
