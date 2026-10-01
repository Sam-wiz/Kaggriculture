# Behavioral-clone dataset: per unit per turn, (state features -> op taken).
# Raw replays carry the player's full private obs each turn, so the features
# are exactly what their code saw at decision time.
import gzip, json, glob, os, sys
from collections import Counter

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
OUT = ROOT + "/mine/rawkeep/bc_DSM.jsonl"
TEAM = sys.argv[1] if len(sys.argv) > 1 else "DSM"
OUT = ROOT + f"/mine/rawkeep/bc_{TEAM.replace(' ','_')}.jsonl"

CROPS = ["WHEAT","CARROT","TOMATO","STRAWBERRY","MELON"]
ANIMALS = ["GOOSE","COW","SHEEP"]

def cls(op):
    """map raw op list -> class label string"""
    k = op[0]
    if k in ("PLANT","PICKUP","PLACE"): return f"{k}:{op[1]}"
    return k

def tile_feats(tiles, x, y):
    """per-tile scalar features for tile at (x,y); None if out of bounds/locked"""
    if y < 0 or y >= len(tiles) or x < 0 or x >= len(tiles[y]): return None
    t = tiles[y][x]
    if t == "LOCKED" or t is None:
        return {"locked": 1 if t == "LOCKED" else 0, "empty": 1 if t is None else 0}
    if not isinstance(t, dict): return {"locked":0,"empty":0}
    k = t.get("kind")
    f = {"locked":0,"empty":0,"weed":k=="WEED","plant":k=="PLANT","animal":0,"struct":0}
    if k == "PLANT":
        f["crop"] = t.get("crop")
        f["age"] = t.get("age") or 0
        f["watered"] = 1 if t.get("watered_today") else 0
        f["dry"] = int(t.get("consecutive_unwatered") or 0)
        f["yield"] = int(t.get("yield_units") or 0)
        f["crop_i"] = CROPS.index(f["crop"]) if f["crop"] in CROPS else -1
    elif k in ("COOP","PASTURE"):
        f["struct"] = 1
        a = t.get("animal")
        if a:
            f["animal"] = 1
            f["fed"] = 1 if t.get("fed_today") else 0
            f["cared"] = 1 if t.get("cared_today") else 0
            f["unfed"] = int(t.get("consecutive_unfed") or 0)
            f["yield"] = int(t.get("yield_units") or 0)
            f["fert_av"] = 1 if t.get("fertilizer_available") else 0
            f["an_i"] = ANIMALS.index(a) if isinstance(a,str) and a in ANIMALS else -1
    return f

def extract(x):
    teams = x["info"]["TeamNames"]
    if TEAM not in teams: return 0
    pi = teams.index(TEAM)
    seed = x["info"]["seed"]; ep = x["info"]["EpisodeId"]
    rows = 0
    out = open(OUT, "a")
    for t, step in enumerate(x["steps"]):
        if pi >= len(step): break
        p = step[pi]; obs = p.get("observation") or {}; act = p.get("action") or {}
        if not obs or not act: continue
        me = obs["farms"][pi]
        tiles = me["tiles"]; priv = obs.get("private") or {}
        shed = priv.get("shed") or {}; invs = priv.get("inventories") or []
        # global board counts (once per step)
        n_dry=n_ripe=n_hungry=n_weed=n_empty=n_crop=n_anim=n_fertav=0
        for row in tiles:
            for tl in row:
                if tl is None: n_empty+=1; continue
                if not isinstance(tl,dict): continue
                if tl.get("kind")=="WEED": n_weed+=1
                elif tl.get("kind")=="PLANT":
                    n_crop+=1
                    if not tl.get("watered_today"): n_dry+=1
                    if (tl.get("yield_units") or 0)>0: n_ripe+=1
                elif tl.get("kind") in ("COOP","PASTURE") and tl.get("animal"):
                    n_anim+=1
                    if not tl.get("fed_today"): n_hungry+=1
                    if tl.get("fertilizer_available"): n_fertav+=1
        units = [me["farmer"]]+list(me.get("hands") or [])
        ops = [act.get("farmer")]+list(act.get("hands") or [])
        G = {"day":obs["day"],"hour":obs["hour"],"money":me["money"],"hires":me["hires_today"],
             "quads":len(me["unlocked_quadrants"]),"shed_wheat":shed.get("WHEAT",0),
             "shed_fert":shed.get("FERTILIZER",0),"shed_goods":sum(v for k,v in shed.items() if k not in ANIMALS),
             "shed_animals":sum(shed.get(a,0) for a in ANIMALS),
             "n_dry":n_dry,"n_ripe":n_ripe,"n_hungry":n_hungry,"n_weed":n_weed,"n_empty":n_empty,
             "n_crop":n_crop,"n_anim":n_anim,"n_fertav":n_fertav,
             "prices":obs["market"]["prices"]}
        for ui,(pos,op) in enumerate(zip(units,ops)):
            if not isinstance(pos,(list,tuple)) or len(pos)<2: continue
            if not isinstance(op,(list,tuple)) or not op: op=["PASS"]
            ux,uy=int(pos[0]),int(pos[1])
            inv = invs[ui] if ui<len(invs) else {}
            inv = inv if isinstance(inv,dict) else {}
            on = tile_feats(tiles,ux,uy) or {}
            # radius-2 neighborhood counts
            nb={"dry":0,"ripe":0,"hungry":0,"empty":0,"weed":0,"anim":0,"fertav":0}
            for yy in range(uy-2,uy+3):
                for xx in range(ux-2,ux+3):
                    tf = tile_feats(tiles,xx,yy)
                    if not tf: continue
                    if tf.get("empty"): nb["empty"]+=1
                    if tf.get("weed"): nb["weed"]+=1
                    if tf.get("plant"):
                        if not tf.get("watered"): nb["dry"]+=1
                        if (tf.get("yield") or 0)>0: nb["ripe"]+=1
                    if tf.get("animal"):
                        nb["anim"]+=1
                        if not tf.get("fed"): nb["hungry"]+=1
                        if tf.get("fertav"): nb["fertav"]+=1
            row = {"ep":ep,"t":t,"ui":ui,"xy":[ux,uy],
                   "inv":{"WHEAT":inv.get("WHEAT",0),"FERTILIZER":inv.get("FERTILIZER",0),
                          "goods":sum(v for k,v in inv.items() if k not in ANIMALS and k not in ("WHEAT","FERTILIZER")),
                          "animals":sum(inv.get(a,0) for a in ANIMALS)},
                   "on":on,"nb":nb,"G":G,"y":cls(list(op))}
            out.write(json.dumps(row)+"\n"); rows+=1
    out.close()
    return rows

if __name__ == "__main__":
    if os.path.exists(OUT): os.remove(OUT)
    files = sorted(glob.glob(ROOT+"/mine/rawkeep/*.json.gz"))
    total = 0; eps = 0
    for f in files:
        try: x = json.load(gzip.open(f,"rt"))
        except: continue
        n = extract(x)
        if n: eps += 1; total += n
    print(f"{TEAM}: {eps} episodes, {total} unit-turn rows -> {OUT}")
