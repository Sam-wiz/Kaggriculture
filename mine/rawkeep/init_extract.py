# INIT-row extractor (opus's design): for each unit's mission-START turn,
# emit per-job-type candidate stats from obs[t-1] (CAUSAL) + the class of the
# work op that eventually ends the mission (label, hindsight ok).
import gzip, json, glob, sys
from collections import deque, defaultdict

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
TEAM = sys.argv[1] if len(sys.argv) > 1 else "DSM"
OUT = sys.argv[2] if len(sys.argv) > 2 else f"mine/rawkeep/init_{TEAM}.jsonl"
CENTERS = {(4,4),(5,4),(4,5),(5,5)}
MOVES = {"NORTH","SOUTH","EAST","WEST"}
TYPES = ["water","harvest","feed","care","cfert","dig","plant","fert","struct_free","shed"]

def masks(tiles):
    J = {k: [] for k in TYPES}
    for y,row in enumerate(tiles):
        for x,t in enumerate(row):
            if t is None:
                J["plant"].append((x,y,0))
            elif isinstance(t,dict):
                k = t.get("kind")
                if k=="WEED": J["dig"].append((x,y,0))
                elif k=="PLANT":
                    if not t.get("watered_today"):
                        J["water"].append((x,y,t.get("consecutive_unwatered") or 0))
                    if not t.get("fertilized_today"):
                        J["fert"].append((x,y,(t.get("yield_units") or 0)))
                    if (t.get("yield_units") or 0)>0:
                        J["harvest"].append((x,y,t["yield_units"]))
                elif k in ("COOP","PASTURE"):
                    if t.get("animal"):
                        if not t.get("fed_today"):
                            J["feed"].append((x,y,t.get("consecutive_unfed") or 0))
                        if not t.get("cared_today"): J["care"].append((x,y,0))
                        if t.get("fertilizer_available"): J["cfert"].append((x,y,0))
                        if (t.get("yield_units") or 0)>0:
                            J["harvest"].append((x,y,t["yield_units"]))
                    else: J["struct_free"].append((x,y,0))
    return J

def bfs(tiles, sx, sy, J, k=2):
    """min & 2nd-min dist to each type + shed"""
    q = deque([(sx,sy,0)]); seen={(sx,sy)}
    found = {t:[] for t in TYPES}; found["shed"]=[]
    while q:
        x,y,d = q.popleft()
        if (x,y) in CENTERS and len(found["shed"])<k: found["shed"].append(d)
        for t,lst in J.items():
            for (tx,ty,u) in lst:
                if (tx,ty)==(x,y) and len(found[t])<k: found[t].append(d)
        if all(len(found[t])>=k for t in TYPES if J.get(t) or t=="shed"): break
        for dx,dy in ((0,-1),(1,0),(0,1),(-1,0)):
            nx,ny=x+dx,y+dy
            if 0<=nx<10 and 0<=ny<10 and (nx,ny) not in seen:
                seen.add((nx,ny)); q.append((nx,ny,d+1))
    return found

# label: class of the work op that ends the mission (first non-move after moves)
def work2type(op):
    if not isinstance(op,(list,tuple)) or not op: return None
    k=op[0]
    return {"WATER":"water","HARVEST":"harvest","FEED":"feed","CARE":"care",
            "COLLECT_FERTILIZER":"cfert","DIG":"dig","PLANT":"plant",
            "BUILD_COOP":"struct_free","BUILD_PASTURE":"struct_free",
            "PICKUP":"shed","PLACE":"shed","DROP":"shed","FERTILIZE":"fert"}.get(k)

out = open(OUT,"w"); nrows=0; eps=0
for f in sorted(glob.glob(f"{ROOT}/mine/rawkeep/*.json.gz")):
    try: x = json.loads(gzip.open(f).read())
    except Exception: continue
    teams = (x.get("info") or {}).get("TeamNames") or []
    if TEAM not in teams: continue
    pi = teams.index(TEAM); eps+=1; steps=x["steps"]
    # per-unit emitted ops
    ops_by_u = defaultdict(list)
    for t,step in enumerate(steps):
        if pi>=len(step): break
        act = step[pi].get("action") or {}
        ops = [act.get("farmer")]+list(act.get("hands") or [])
        for ui,op in enumerate(ops):
            ops_by_u[ui].append((t,op))
    for ui,seq in ops_by_u.items():
        in_mission = False
        for i,(t,op) in enumerate(seq):
            is_move = isinstance(op,(list,tuple)) and op and op[0] in MOVES
            if is_move and not in_mission:
                # mission start at t -> look ahead for ending work op
                end_cls=None
                for j in range(i+1, min(i+13, len(seq))):
                    oc = work2type(seq[j][1])
                    if oc: end_cls=oc; break
                    if not (isinstance(seq[j][1],(list,tuple)) and seq[j][1] and seq[j][1][0] in MOVES):
                        break
                if t-1<0 or pi>=len(steps[t-1]): in_mission=True; continue
                obs = steps[t-1][pi].get("observation") or {}
                if not obs: in_mission=True; continue
                me=obs["farms"][pi]; priv=obs.get("private") or {}
                pos=[me["farmer"]]+list(me.get("hands") or [])
                if ui>=len(pos): in_mission=True; continue
                ux,uy=pos[ui]
                J = masks(me["tiles"]); found = bfs(me["tiles"],ux,uy,J)
                shed=priv.get("shed") or {}; invs=priv.get("inventories") or []
                uinv = invs[ui] if ui<len(invs) else {}
                row={"ep":x["info"]["EpisodeId"],"t":t,"ui":ui,"xy":[ux,uy],
                     "G":{"day":obs["day"],"hour":obs["hour"],"money":me["money"]},
                     "inv":uinv,"types":{}}
                for ty,lst in J.items():
                    urg = [u for _,_,u in lst]
                    row["types"][ty] = {"n":len(lst),"d":found[ty][:2],
                                       "urg":max(urg) if urg else 0,
                                       "urg2":sorted(urg)[-2] if len(urg)>1 else 0,
                                       "urg_sum":sum(urg)}
                row["types"]["shed"]={"n":1,"d":found["shed"][:2],"urg":0}
                row["label"]=end_cls
                out.write(json.dumps(row)+"\n"); nrows+=1
                in_mission = True
            elif not is_move:
                in_mission = False
out.close()
print(f"{TEAM}: {eps} eps, {nrows} INIT rows -> {OUT}")
