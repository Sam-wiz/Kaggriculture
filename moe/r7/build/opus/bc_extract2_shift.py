# BC dataset v2: richer per-unit features — nearest-distance to each job type.
# job types a unit might walk toward: WATER(dry plant), HARVEST(ripe), FEED(hungry animal),
# CARE(uncared animal), CFERT(fert_available animal), DIG(weed), PLANT(empty), FERT(plant w/o fert),
# SHED(4 center tiles), plus distances to nearest PICKUP source (shed) and placement targets.
import gzip, json, glob, os, sys
from collections import deque, Counter

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
TEAM = sys.argv[1] if len(sys.argv) > 1 else "DSM"
OUT = ROOT + "/moe/r7/build/opus/bc2s_DSM.jsonl"

CROPS = ["WHEAT","CARROT","TOMATO","STRAWBERRY","MELON"]
ANIMALS = ["GOOSE","COW","SHEEP"]
CENTERS = [(4,4),(5,4),(4,5),(5,5)]
DIRS = [(0,-1),(1,0),(0,1),(-1,0)]

def cls(op):
    k = op[0]
    if k in ("PLANT","PICKUP","PLACE"): return f"{k}:{op[1]}"
    return k

def tdist(tiles, kinds, start):
    """BFS from start over unlocked+empty-any tiles; returns dist to nearest tile matching `kinds` predicate set."""
    # we compute per-unit BFS to each kind lazily; simpler: BFS once per unit, record dist to each kind
    pass

MASKKEYS = ["water","harvest","feed","care","cfert","dig","empty","struct_free"]

def bfs_nearest(tiles, masks, sx, sy):
    """BFS from (sx,sy); return {kind: (dist, first-step-dx, first-step-dy)} + shed same."""
    H = len(tiles); W = len(tiles[0])
    found = {}
    shed_dir = None
    seen = [[False]*W for _ in range(H)]
    # queue holds (x,y,d,fdx,fdy) where fd* = first step from origin
    q = deque([(sx,sy,0,0,0)]); seen[sy][sx]=True
    while q and (len(found) < len(MASKKEYS) or shed_dir is None):
        x,y,d,fdx,fdy = q.popleft()
        for k in MASKKEYS:
            if k not in found and masks[k][y][x]: found[k] = (d,fdx,fdy)
        if (x,y) in CENTERS and shed_dir is None: shed_dir = (d,fdx,fdy)
        if len(found) == len(MASKKEYS) and shed_dir is not None: break
        for dx,dy in DIRS:
            nx,ny = x+dx,y+dy
            if 0<=nx<W and 0<=ny<H and not seen[ny][nx]:
                seen[ny][nx]=True
                q.append((nx,ny,d+1,dx if d==0 else fdx, dy if d==0 else fdy))
    out = {k: found.get(k,(99,0,0)) for k in MASKKEYS}
    return out, (shed_dir or (99,0,0))

def board_scan(me):
    """tile arrays + pending job sets. returns (tiles, masks)"""
    tiles = me["tiles"]; H=len(tiles); W=len(tiles[0])
    masks = {k:[[False]*W for _ in range(H)] for k in
             ["water","harvest","feed","care","cfert","dig","empty","plantable","struct_free","fertok"]}
    for y in range(H):
        for x in range(W):
            t = tiles[y][x]
            if t is None:
                masks["empty"][y][x] = masks["plantable"][y][x] = True
            elif isinstance(t,dict):
                k = t.get("kind")
                if k=="WEED": masks["dig"][y][x]=True
                elif k=="PLANT":
                    if not t.get("watered_today"): masks["water"][y][x]=True
                    if (t.get("yield_units") or 0)>0: masks["harvest"][y][x]=True
                    if not t.get("fertilized_until_day") or t.get("fertilized_until_day",0) <= 30:
                        masks["fertok"][y][x]=True  # can be fertilized (approx)
                elif k in ("COOP","PASTURE"):
                    if t.get("animal"):
                        if not t.get("fed_today"): masks["feed"][y][x]=True
                        if not t.get("cared_today"): masks["care"][y][x]=True
                        if t.get("fertilizer_available"): masks["cfert"][y][x]=True
                        if (t.get("yield_units") or 0)>0: masks["harvest"][y][x]=True
                    else:
                        masks["struct_free"][y][x]=True
    return masks

def extract(x):
    teams = x["info"]["TeamNames"]
    if TEAM not in teams: return 0
    pi = teams.index(TEAM)
    seed = x["info"]["seed"]; ep = x["info"]["EpisodeId"]
    rows = 0
    out = open(OUT, "a")
    steps = x["steps"]
    # per-unit op class timeline -> next-work labels (what job is this unit pursuing?)
    nsteps = len(steps)
    unit_ops = []  # [ui][t] = op class
    max_units = 0
    for step in steps:
        if pi >= len(step): break
        p = step[pi]; act = p.get("action") or {}
        ops = [act.get("farmer")]+list(act.get("hands") or [])
        max_units = max(max_units, len(ops))
    unit_ops = [[] for _ in range(max_units)]
    for t, step in enumerate(steps):
        if pi >= len(step): break
        p = step[pi]; act = p.get("action") or {}
        ops = [act.get("farmer")]+list(act.get("hands") or [])
        for ui in range(max_units):
            op = ops[ui] if ui < len(ops) else None
            unit_ops[ui].append(cls(list(op)) if isinstance(op,(list,tuple)) and op else "ABSENT")
    MOVES = {"NORTH","SOUTH","EAST","WEST"}
    def next_work(uop, t):
        for tt in range(t, min(t+12, len(uop))):
            c = uop[tt]
            if c not in MOVES and c != "PASS" and c != "ABSENT": return c
        return None

    for t, step in enumerate(steps):
        if pi >= len(step): break
        if t == 0: continue
        p = step[pi]; act = p.get("action") or {}
        obs = steps[t-1][pi].get("observation") or {}  # SHIFT: action[t] was chosen from obs[t-1]
        if not obs or not act: continue
        me = obs["farms"][pi]
        tiles = me["tiles"]; priv = obs.get("private") or {}
        shed = priv.get("shed") or {}; invs = priv.get("inventories") or []
        masks = board_scan(me)
        counts = {k: sum(row.count(True) for row in m) for k,m in masks.items()}
        units = [me["farmer"]]+list(me.get("hands") or [])
        ops = [act.get("farmer")]+list(act.get("hands") or [])
        G = {"day":obs["day"],"hour":obs["hour"],"money":me["money"],"hires":me["hires_today"],
             "quads":len(me["unlocked_quadrants"]),
             "shed_wheat":shed.get("WHEAT",0),"shed_fert":shed.get("FERTILIZER",0),
             "shed_animals":sum(shed.get(a,0) for a in ANIMALS),
             "cnts":counts}
        for ui,(pos,op) in enumerate(zip(units,ops)):
            if not isinstance(pos,(list,tuple)) or len(pos)<2: continue
            if not isinstance(op,(list,tuple)) or not op: op=["PASS"]
            ux,uy = int(pos[0]),int(pos[1])
            dists, shed_dir = bfs_nearest(tiles, masks, ux, uy)
            inv = invs[ui] if ui<len(invs) else {}
            inv = inv if isinstance(inv,dict) else {}
            t0 = tiles[uy][ux]
            on = {"empty": t0 is None}
            if isinstance(t0,dict):
                k = t0.get("kind")
                on = {"weed":k=="WEED","plant":k=="PLANT","animal":bool(t0.get("animal")),
                      "watered":t0.get("watered_today"),"yield":t0.get("yield_units") or 0,
                      "fed":t0.get("fed_today"),"cared":t0.get("cared_today"),
                      "fert_av":t0.get("fertilizer_available")}
            y_raw = cls(list(op))
            y_job = y_raw if y_raw not in MOVES else (next_work(unit_ops[ui], t) or "MOVE_IDLE")
            row = {"ep":ep,"t":t,"ui":ui,"xy":[ux,uy],
                   "d":dists,"dshed":shed_dir,
                   "inv":{"WHEAT":inv.get("WHEAT",0),"FERTILIZER":inv.get("FERTILIZER",0),
                          "goods":sum(v for k,v in inv.items() if k not in ANIMALS and k not in ("WHEAT","FERTILIZER")),
                          "animals":sum(inv.get(a,0) for a in ANIMALS)},
                   "on":on,"G":G,"y":y_raw,"y2":y_job}
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
    print(f"{TEAM}: {eps} episodes, {total} rows -> {OUT}")
