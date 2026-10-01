"""Reverse-engineer the scheduler: for each unit, each turn — what job did it pick,
what jobs were available, and which features predict the choice.
Work ops act on the unit's CURRENT tile. Move ops: trace ahead to the first work op —
that tile's need is the travel target."""
import gzip, json, glob
from collections import Counter, defaultdict

WORK = {"WATER","HARVEST","PLANT","FEED","CARE","COLLECT_FERTILIZER","DIG","BUILD_COOP","BUILD_PASTURE","PICKUP","PLACE","DROP","FERTILIZE"}
MOVE = {"NORTH","SOUTH","EAST","WEST"}

def tile_needs(tile, day):
    """Jobs a tile needs right now, from its obs dict."""
    if tile is None: return {"empty":1}
    if not isinstance(tile,dict): return {}
    k = tile.get("kind")
    if k=="WEED": return {"DIG":1}
    if k=="PLANT":
        d={}
        if not tile.get("watered_today"): d["WATER"]=1
        if tile.get("yield_units",0)>0: d["HARVEST"]=1
        return d
    if k in ("COOP","PASTURE"):
        d={}
        if tile.get("animal"):
            if not tile.get("fed_today"): d["FEED"]=1
            if not tile.get("cared_today"): d["CARE"]=1
            if tile.get("fertilizer_available"): d["COLLECT_FERTILIZER"]=1
            if tile.get("yield_units",0)>0: d["COLLECT_PRODUCT"]=1
        else: d["empty_struct"]=1
        return d
    return {}

out = open("mine/rawkeep/jobs_DSM.jsonl","w")
n=0
for f in sorted(glob.glob("mine/rawkeep/*.json.gz"))[:50]:
    try: x=json.load(gzip.open(f,"rt"))
    except: continue
    teams=x["info"]["TeamNames"]
    if "DSM" not in teams: continue
    pi=teams.index("DSM"); ep=x["info"]["EpisodeId"]
    steps=x["steps"]
    # precompute unit trajectories: positions per unit per turn
    traj=[]
    for t,step in enumerate(steps):
        p=step[pi]; obs=p.get("observation") or {}
        me=obs["farms"][pi]; act=p.get("action") or {}
        units=[me["farmer"]]+list(me.get("hands") or [])
        ops=[act.get("farmer")]+list(act.get("hands") or [])
        traj.append((obs,units,ops))
    for t,(obs,units,ops) in enumerate(traj):
        tiles=obs["farms"][pi]["tiles"]
        pending=[]
        for y,row in enumerate(tiles):
            for xx,tile in enumerate(row):
                for j in tile_needs(tile, obs["day"]): pending.append((xx,y,j))
        for ui,(pos,op) in enumerate(zip(units,ops)):
            if not isinstance(pos,(list,tuple)) or not (isinstance(op,(list,tuple)) and op): continue
            opp=op[0]
            if opp in WORK:
                chosen=(pos[0],pos[1],opp)
            elif opp in MOVE:
                chosen=None
                tt,pp=t+1,tuple(pos)
                while tt<min(t+12,len(traj)):
                    _,u2,o2=traj[tt]
                    if ui<len(u2) and ui<len(o2):
                        p2,o3=u2[ui],o2[ui]
                        if isinstance(o3,(list,tuple)) and o3:
                            if o3[0] in WORK and isinstance(p2,(list,tuple)):
                                chosen=(p2[0],p2[1],o3[0]); break
                            if o3[0] in MOVE and isinstance(p2,(list,tuple)): pp=tuple(p2)
                            elif o3[0]=="PASS": break
                    tt+=1
                if chosen is None: continue
            else: continue
            # was the chosen job among pending? distance + type
            d=abs(pos[0]-chosen[0])+abs(pos[1]-chosen[1])
            rec={"ep":ep,"t":t,"day":obs["day"],"hour":obs["hour"],"unit":ui,
                 "pos":list(pos),"job":chosen[2],"jx":chosen[0],"jy":chosen[1],"dist":d,
                 "npending":len(pending)}
            out.write(json.dumps(rec)+"\n"); n+=1
print("job-attribution rows:",n)
