# Tile-level INIT extractor v2 — per-candidate economic features + corrected labels.
# Fixes per astra/opus audit: EGG naming ok but PRICES were seed costs -> now BASE
# sell prices; BUILD_* -> "build" on empty tiles (was mislabeled struct_free);
# animal PLACE -> "struct_free" (standing on empty structure), item PLACE ->
# "shed"; added wbon (in-window watering bonus), row slack/units/seeds/uinv for
# cargo feasibility masks in the fitter.
import gzip, json, glob, sys
from collections import deque, defaultdict

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
TEAM = sys.argv[1] if len(sys.argv) > 1 else "DSM"
OUT = sys.argv[2] if len(sys.argv) > 2 else f"mine/rawkeep/tilerows_{TEAM}.jsonl"
CENTERS = {(4,4),(5,4),(4,5),(5,5)}
MOVES = {"NORTH","SOUTH","EAST","WEST"}
TYPES = ["water","harvest","feed","care","cfert","dig","plant","build","fert","struct_free","shed"]
TI = {t:i for i,t in enumerate(TYPES)}
# BASE SELL prices (README price table), not seed costs
PRICES = {"WHEAT":25,"CARROT":35,"TOMATO":60,"STRAWBERRY":120,"MELON":250,
          "EGG":50,"MILK":160,"WOOL":200,"FERTILIZER":100}
ANIMALS = {"GOOSE":{"cost":300,"product":"EGG"},"COW":{"cost":400,"product":"MILK"},
           "SHEEP":{"cost":500,"product":"WOOL"}}
# one-time crops: bonus window starts at ceil(max_yield_day/2) age
ONETIME_MYD = {"WHEAT":4,"CARROT":3,"MELON":10}

def candidates(tiles, mkt_prices, day):
    C = []
    for y,row in enumerate(tiles):
        for x,t in enumerate(row):
            if t is None:
                C.append({"ty":"plant","x":x,"y":y,"urg":0,"yld":0,"val":0,"dl":99,"wbon":0})
                C.append({"ty":"build","x":x,"y":y,"urg":0,"yld":0,"val":0,"dl":99,"wbon":0})
            elif isinstance(t,dict):
                k = t.get("kind")
                if k=="WEED":
                    C.append({"ty":"dig","x":x,"y":y,"urg":0,"yld":0,"val":0,"dl":99,"wbon":0})
                elif k=="PLANT":
                    crop=t.get("crop"); pr=mkt_prices.get(crop) or PRICES.get(crop,10)
                    cu = t.get("consecutive_unwatered") or 0
                    yld = t.get("yield_units") or 0
                    life = (t.get("max_lifespan_step") or 720) - day*24
                    fert = (t.get("fertilized_until_day") or -1) > day
                    age = day - (t.get("planted_day") or day)
                    # in-window watering bonus: one-time crops past half of max yield day
                    wbon = 0
                    if crop in ONETIME_MYD and age >= -(-ONETIME_MYD[crop]//2):
                        wbon = round(pr*(2 if fert else 1),1)
                    elif fert:  # ongoing crop: fert+water doubles the scheduled unit
                        wbon = round(pr,1)
                    if not t.get("watered_today"):
                        C.append({"ty":"water","x":x,"y":y,"urg":cu,"yld":yld,
                                  "val":round(yld*pr,1),"dl":min(life,(2-cu)*24),"wbon":wbon})
                    if yld>0:
                        C.append({"ty":"harvest","x":x,"y":y,"urg":0,"yld":yld,
                                  "val":round(yld*pr,1),"dl":life,"wbon":0})
                    if not fert:
                        C.append({"ty":"fert","x":x,"y":y,"urg":0,"yld":yld,
                                  "val":round(yld*pr,1),"dl":life,"wbon":0})
                elif k in ("COOP","PASTURE"):
                    a = t.get("animal")
                    if a:
                        pr = mkt_prices.get(ANIMALS[a]["product"]) or PRICES.get(ANIMALS[a]["product"],50)
                        cu = t.get("consecutive_unfed") or 0
                        yld = t.get("yield_units") or 0
                        aval = ANIMALS[a]["cost"]
                        if not t.get("fed_today"):
                            C.append({"ty":"feed","x":x,"y":y,"urg":cu,"yld":yld,
                                      "val":aval,"dl":(2-cu)*24,"wbon":0})
                        if not t.get("cared_today"):
                            C.append({"ty":"care","x":x,"y":y,"urg":0,"yld":t.get("pending_care_bonus") or 0,
                                      "val":round(pr,1),"dl":24,"wbon":0})
                        if t.get("fertilizer_available"):
                            C.append({"ty":"cfert","x":x,"y":y,"urg":0,"yld":0,"val":PRICES["FERTILIZER"],"dl":24,"wbon":0})
                        if yld>0:
                            C.append({"ty":"harvest","x":x,"y":y,"urg":0,"yld":yld,
                                      "val":round(yld*pr,1),"dl":99,"wbon":0})
                    else:
                        C.append({"ty":"struct_free","x":x,"y":y,"urg":0,"yld":0,"val":0,"dl":99,"wbon":0})
    for cx,cy in CENTERS:
        C.append({"ty":"shed","x":cx,"y":cy,"urg":0,"yld":0,"val":0,"dl":99,"wbon":0})
    return C

def bfs_all(tiles, sx, sy):
    q=deque([(sx,sy,0)]); D={(sx,sy):0}
    while q:
        x,y,d=q.popleft()
        for dx,dy in ((0,-1),(1,0),(0,1),(-1,0)):
            nx,ny=x+dx,y+dy
            if 0<=nx<10 and 0<=ny<10 and (nx,ny) not in D:
                D[(nx,ny)]=d+1; q.append((nx,ny,d+1))
    return D

def op2type(op):
    if not isinstance(op,(list,tuple)) or not op: return None
    o = op[0]
    if o=="PLACE":  # animal PLACE lands on its empty structure; item PLACE is shed-adjacent
        return "struct_free" if len(op)>1 and op[1] in ANIMALS else "shed"
    return {"WATER":"water","HARVEST":"harvest","FEED":"feed","CARE":"care",
            "COLLECT_FERTILIZER":"cfert","DIG":"dig","PLANT":"plant","FERTILIZE":"fert",
            "BUILD_COOP":"build","BUILD_PASTURE":"build",
            "PICKUP":"shed","DROP":"shed"}.get(o)

out=open(OUT,"w");nrows=0;eps=0
for f in sorted(glob.glob(f"{ROOT}/mine/rawkeep/*.json.gz")):
    try: x=json.loads(gzip.open(f).read())
    except Exception: continue
    teams=(x.get("info") or {}).get("TeamNames") or []
    if TEAM not in teams: continue
    pi=teams.index(TEAM);eps+=1;steps=x["steps"]
    ops_by_u=defaultdict(list)
    for t,step in enumerate(steps):
        if pi>=len(step): break
        act=step[pi].get("action") or {}
        ops=[act.get("farmer")]+list(act.get("hands") or [])
        for ui,op in enumerate(ops): ops_by_u[ui].append((t,op))
    # unit positions per turn (for worked-tile centroid -> zone feature)
    pos_t={}
    for t,step in enumerate(steps):
        if pi>=len(step): break
        o=step[pi].get("observation") or {}
        if not o: continue
        me0=o["farms"][pi]
        pos_t[t]=[me0["farmer"]]+list(me0.get("hands") or [])
    for ui,seq in ops_by_u.items():
        in_m=False; worked=[]; last_day=-1
        for i,(t,op) in enumerate(seq):
            is_mv=isinstance(op,(list,tuple)) and op and op[0] in MOVES
            if t//24!=last_day: worked=[];last_day=t//24
            if not is_mv and op2type(op) and t in pos_t and ui<len(pos_t[t]):
                worked.append(tuple(pos_t[t][ui]))   # causal zone evidence
            if is_mv and not in_m:
                end=None
                for j in range(i+1,min(i+13,len(seq))):
                    tt,oo=seq[j]; oc=op2type(oo)
                    if oc:
                        if tt<len(steps) and pi<len(steps[tt]):
                            o2=steps[tt][pi].get("observation") or {}
                            me2=o2["farms"][pi]
                            pos=[me2["farmer"]]+list(me2.get("hands") or [])
                            if ui<len(pos): end=(oc,tuple(pos[ui]))
                        break
                    if not (isinstance(oo,(list,tuple)) and oo and oo[0] in MOVES): break
                if t-1<0 or pi>=len(steps[t-1]): in_m=True;continue
                obs=steps[t-1][pi].get("observation") or {}
                if not obs: in_m=True;continue
                me=obs["farms"][pi];priv=obs.get("private") or {}
                pos=[me["farmer"]]+list(me.get("hands") or [])
                if ui>=len(pos): in_m=True;continue
                ux,uy=pos[ui]
                zc = (sum(p[0] for p in worked)/len(worked),
                      sum(p[1] for p in worked)/len(worked)) if worked else None
                C=candidates(me["tiles"],(obs.get("market") or {}).get("prices") or {},obs["day"])
                D=bfs_all(me["tiles"],ux,uy)
                for c in C:
                    c["d"]=D.get((c["x"],c["y"]),99)
                    c["zd"] = round(((c["x"]-zc[0])**2+(c["y"]-zc[1])**2)**.5,1) if zc else -1
                inv=(priv.get("inventories") or [])
                uinv=inv[ui] if ui<len(inv) else {}
                seeds=priv.get("seeds") or {}
                hour=obs["hour"]; units=len(pos)
                dem=sum(min(c["d"],24)+1 for c in C if c["ty"] in ("water","feed","harvest"))
                slack=units*(24-hour)-dem
                row={"ep":x["info"]["EpisodeId"],"t":t,"ui":ui,
                     "G":{"day":obs["day"],"hour":hour,"money":me["money"],
                          "hires":me.get("hires_today",0),"slack":slack},
                     "units":units,"seeds_tot":sum(seeds.values()),
                     "inv":{k:uinv.get(k,0) for k in ("WHEAT","FERTILIZER","COW","SHEEP","GOOSE")},
                     "cands":C}
                if end: row["label"]={"ty":end[0],"xy":list(end[1])}
                out.write(json.dumps(row)+"\n");nrows+=1
                in_m=True
            elif not is_mv: in_m=False
out.close()
print(f"{TEAM}: {eps} eps, {nrows} INIT rows -> {OUT}")
