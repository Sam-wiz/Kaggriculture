# DSM-clone v3: territorial zone scheduler + learned DSM economy program.
# Extracted from 50 raw DSM replays (mine/rawkeep). Standalone agent.
# Engine constants copied from kaggriculture 1.32.7 (public rules).

DAYS = 30
CENTER = {(4,4),(5,4),(4,5),(5,5)}
PRODUCTS = ["STRAWBERRY","MELON","MILK","WOOL","TOMATO","EGG","CARROT","WHEAT","FERTILIZER"]

CROPS = {
 "WHEAT":     {"seed":10,  "first":2,  "maxd":4,  "harv":4,  "ongoing":False},
 "CARROT":    {"seed":20,  "first":2,  "maxd":3,  "harv":3,  "ongoing":False},
 "TOMATO":    {"seed":50,  "first":8,  "maxd":8,  "harv":8,  "ongoing":True},
 "STRAWBERRY":{"seed":100, "first":10, "maxd":10, "harv":10, "ongoing":True},
 "MELON":     {"seed":80,  "first":10, "maxd":12, "harv":10, "ongoing":False},
}
ANIMALS = {
 "GOOSE": {"cost":300, "struct":"COOP",    "first":4, "product":"EGG"},
 "COW":   {"cost":400, "struct":"PASTURE", "first":8, "product":"MILK"},
 "SHEEP": {"cost":500, "struct":"PASTURE", "first":6, "product":"WOOL"},
}
ANIMAL_STRUCT = {"COW":"PASTURE","SHEEP":"PASTURE","GOOSE":"COOP"}

HIRES = [4,4,6,6,6,6,8,9,9,10] + [11]*18 + [10,10]
LAND_DAYS = {6:"NE", 9:"SW"}
LAND_COST = {"NE":1000, "SW":2000, "SE":4000}
# herd is the income engine: animals compound via care bonus. Windows shifted
# +2d vs mined (clone cash runs a few days behind), cows first (best ROI).
# ~23 head is about the labor ceiling on top of the crop program.
HERD_PLAN = [
    (3,7,"COW",2),(6,10,"GOOSE",3),(8,13,"COW",7),
    (9,17,"SHEEP",4),(13,20,"COW",3),(16,24,"SHEEP",2),
]
STRUCT_PLAN = [(2,"PASTURE",8),(6,"COOP",3),(8,"PASTURE",14),(13,"PASTURE",20),(14,"COOP",5),(18,"PASTURE",24)]
# melon-heavy opener IS the bridge capital (harvest ~d10-12 funds land +
# strawberry mass). Strawberry window ends ~d16 so all 4 production events
# land in-season; strawberry carries a double share of plant jobs.
CROP_PLAN = [
    (0,2,"MELON",12,150),
    (2,16,"STRAWBERRY",28,150),
    (3,9,"CARROT",8,80),
    (6,26,"TOMATO",10,120),
    (10,29,"CARROT",35,80),
]

# NOTE: the BC job-priority MLP (56->128->64->31, trained on 347k DSM
# unit-turns) was ablated: plain nearest-job dispatch beat it 13-3
# head-to-head (+5.6k avg margin). Weights and featurizer removed.

FEED_BUFFER = 4
# hire cost of the n-th hire today (0-indexed): 1,1,2,3,5,8,...
_FIB=[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987]
URGENT={"WATER","FEED","HARVEST","DIG","CARE","BUILD_COOP","BUILD_PASTURE"}
# barn zone: structures go in a compact block near home; crops never planted
# there. Tightened to x0-4,y3-7 so NW row 2 stays plantable day 0; the SW
# rows hold the overflow once that quadrant is bought.
BARN = {(x,y) for x in range(0,5) for y in range(3,8)} - CENTER

def _mh(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])
def _step(pos,tgt):
    dx,dy = tgt[0]-pos[0], tgt[1]-pos[1]
    if dx==0 and dy==0: return "PASS"
    if abs(dx)>=abs(dy): return "EAST" if dx>0 else "WEST"
    return "SOUTH" if dy>0 else "NORTH"
def _animal(t):
    a=t.get("animal"); return a if isinstance(a,str) else (a or {}).get("kind")

def agent(obs, config=None):
    p = int(obs.get("player") or 0)
    day = int(obs.get("day") or 0)
    hour = int(obs.get("hour") or 0)
    me = obs["farms"][p]
    tiles = me["tiles"]
    money = me["money"]
    priv = obs.get("private") or {}
    shed = priv.get("shed") or {}
    seeds = priv.get("seeds") or {}
    invs = priv.get("inventories") or []

    jobs=[]; empties=[]; barn_empty=[]; free={"PASTURE":[],"COOP":[]}
    carried_wheat=sum(i.get("WHEAT",0) for i in invs if isinstance(i,dict))
    have={"COW":0,"SHEEP":0,"GOOSE":0}; structs={"PASTURE":0,"COOP":0}
    crops={c:0 for c in CROPS}; ripe=[]
    for y,row in enumerate(tiles):
        for x,t in enumerate(row):
            if t=="LOCKED": continue
            if t is None:
                if (x,y) in BARN: barn_empty.append((x,y))
                else: empties.append((x,y))
                continue
            if not isinstance(t,dict): continue
            k=t["kind"]
            if k=="WEED": jobs.append((x,y,"DIG"))
            elif k=="PLANT":
                c=t.get("crop")
                if c in crops: crops[c]+=1
                cd = CROPS.get(c)
                age = day-t.get("planted_day",0)
                # ongoing crops accumulate up to max_yield=4 on the tile —
                # harvesting at 1-2 units doubles the trip count for nothing,
                # but a decaying tile drains yield so grab whatever is there
                decaying = t.get("max_lifespan_step",-1)>0 and (day*24+hour)>=t["max_lifespan_step"]
                ready = cd and t.get("yield_units",0)>0 and (age>=cd["harv"] or (cd["ongoing"] and age>=cd["first"] and (t.get("yield_units",0)>=3 or decaying)))
                if ready: jobs.append((x,y,"HARVEST"))
                elif not t.get("watered_today"): jobs.append((x,y,"WATER"))
            elif k in ("COOP","PASTURE"):
                structs[k]+=1
                a=_animal(t)
                if a:
                    if a in have: have[a]+=1
                    if not t.get("fed_today") and (shed.get("WHEAT",0)>0 or carried_wheat>0): jobs.append((x,y,"FEED"))
                    if t.get("yield_units",0)>=3: jobs.append((x,y,"HARVEST"))
                    if not t.get("cared_today"): jobs.append((x,y,"CARE"))
                    if t.get("fertilizer_available"): jobs.append((x,y,"COLLECT_FERTILIZER"))
                else: free[k].append((x,y))
    herd_n=sum(have.values())

    market=[]
    if day>=DAYS-1:
        for prod in PRODUCTS:
            if shed.get(prod,0)>0: market.append(["SELL",prod,1000])
        # day 29 still wants harvest labor
        want=6
        while me["hires_today"]+sum(1 for o in market if o[0]=="HIRE")<want and len(market)<10:
            market.append(["HIRE"])
    else:
        want=HIRES[min(day,len(HIRES)-1)]
        nh=me["hires_today"]
        while nh<want and len(market)<6:
            market.append(["HIRE"]); money-=_FIB[min(nh,len(_FIB)-1)]; nh+=1
        # sells right after hires so the 10-order cap can't starve them;
        # drain full stock, but never sell fertilizer (production input)
        # or the wheat feed reserve
        keep_w=herd_n*2+8
        for prod in PRODUCTS:
            if prod=="FERTILIZER": continue
            # metered drain: orders commit one unit at a time at re-quoted
            # prices, so dumping a deep stack sells into its own glut
            q=min(shed.get(prod,0)-(keep_w if prod=="WHEAT" else 0),12)
            if q>0 and len(market)<10:
                market.append(["SELL",prod,q])
        for q in ("NE","SW"):
            if q not in me["unlocked_quadrants"] and money>LAND_COST[q]+100 and len(market)<10:
                market.append(["BUY_LAND"]); money-=LAND_COST[q]
        # feed first — keep the herd alive before growing it
        need=herd_n*2+8-shed.get("WHEAT",0)-carried_wheat
        if day>=2 and need>0 and money>120 and len(market)<10:
            market.append(["BUY_PRODUCT","WHEAT",min(9,need)]); money-=10*min(9,need)
        # herd: one animal per turn, only when a free home exists right now
        # and no same-species animal is parked in the shed awaiting placement
        if shed.get("WHEAT",0)>=herd_n+2:
            for lo,hi,sp,tgt in HERD_PLAN:
                need=tgt-have[sp]-shed.get(sp,0)
                if lo<=day<=hi and need>0:
                    k=ANIMAL_STRUCT[sp]
                    if free[k] and shed.get(sp,0)<2 and money>ANIMALS[sp]["cost"]+300 and len(market)<10:
                        market.append(["BUY_ANIMAL",sp,1]); money-=ANIMALS[sp]["cost"]
                        break
        # seeds: buy toward the day's crop window, partial buys when cash is
        # thin; strawberry is the compounding engine so it stocks deeper
        for lo,hi,c,tgt,minc in CROP_PLAN:
            cap=12 if c=="STRAWBERRY" else 8
            if lo<=day<=hi and crops[c]<tgt and seeds.get(c,0)<cap and len(market)<10:
                n2=min(6 if c=="STRAWBERRY" else 4,int((money-minc)/CROPS[c]["seed"]))
                if n2>0:
                    market.append(["BUY_SEED",c,n2]); money-=CROPS[c]["seed"]*n2
        if seeds.get("WHEAT",0)<8 and money>150 and len(market)<10:
            market.append(["BUY_SEED","WHEAT",4]); money-=40

    units=[me["farmer"]]+list(me.get("hands") or [])
    n=len(units); claimed=set()
    want=[c for lo,hi,c,tgt,mn in CROP_PLAN if lo<=day<=hi and crops[c]<tgt and seeds.get(c,0)>0]
    wheat_tgt=min(20,max(8,herd_n+6))
    if seeds.get("WHEAT",0)>0 and day<29 and crops["WHEAT"]<wheat_tgt: want.append("WHEAT")
    # strawberry carries the midgame economy — give it a double share of tiles
    if "STRAWBERRY" in want: want.append("STRAWBERRY")
    # spread planting across all wanted crops, assigned round-robin per tile.
    # these MUST live in `jobs` — a separate list dispatched after the job pool
    # is unreachable whenever any job exists, which is what starved planting.
    plant_jobs=[(x,y,"PLANT",want[(x+y)%len(want)]) for (x,y) in empties] if want else []
    jobs+=plant_jobs

    tgt_struct={}
    for d,k,tg in STRUCT_PLAN:
        if day>=d: tgt_struct[k]=tg
    # placing animals is a dedicated center->structure errand, not a shared job:
    # units with nothing else to do run it via the PICKUP/deliver branches in work().
    for k,tg in tgt_struct.items():
        deficit=tg-structs[k]-sum(1 for j in jobs if j[2]=="BUILD_"+k)
        # build on actual demand: unhoused animals waiting, or the herd plan
        # wants more of this kind than housed+spare capacity (keep ~2 spare)
        unhoused=shed.get("GOOSE",0) if k=="COOP" else shed.get("COW",0)+shed.get("SHEEP",0)
        housed=sum(have[a] for a,s in ANIMAL_STRUCT.items() if s==k)
        planned=sum(tgt for lo,hi,sp,tgt in HERD_PLAN if ANIMAL_STRUCT[sp]==k and lo<=day)
        if deficit>0 and (unhoused>0 or (len(free[k])<3 and housed+len(free[k])<min(planned,tg))):
            for (x,y) in barn_empty[:min(deficit,3)]:
                jobs.append((x,y,"BUILD_"+k))

    unhoused_all=sum(shed.get(sp,0) for sp in ANIMALS)
    def work(pos,ui):
        px,py=pos
        if not (0<=py<len(tiles) and 0<=px<len(tiles[py])): return ["PASS"]
        tile=tiles[py][px]
        inv=invs[ui] if ui<len(invs) else {}
        inv=inv if isinstance(inv,dict) else {}
        animals_inv=[sp for sp in ANIMALS if inv.get(sp,0)>0]
        goods=sum(v or 0 for k2,v in inv.items() if k2 not in ANIMALS and k2 not in ("WHEAT","FERTILIZER"))
        # carrying animals -> deliver to free structure
        if animals_inv:
            sp=animals_inv[0]; k=ANIMAL_STRUCT[sp]
            if free[k]:
                tgt=min(free[k],key=lambda s:_mh(pos,s))
                if (px,py)==tgt: return ["PLACE",sp,1]
                return [_step(pos,tgt)]
        # carrying wheat while animals are hungry -> run the feed route
        if inv.get("WHEAT",0)>0 and any(j[2]=="FEED" for j in jobs):
            fj=[j for j in jobs if j[2]=="FEED" and (j[0],j[1],"FEED") not in claimed]
            if fj:
                bx,by,bj=min(fj,key=lambda j:_mh(pos,j))
                claimed.add((bx,by,bj))
                if (bx,by)==(px,py): return ["FEED"]
                return [_step(pos,(bx,by))]
        # carrying goods -> shed run only when loaded or passing by;
        # anything still carried is auto-dropped into the shed at end of day
        if goods>0:
            if (px,py) in CENTER: return ["DROP"]
            if goods>=8 or min(_mh(pos,c) for c in CENTER)<=3:
                return [_step(pos,min(CENTER,key=lambda c:_mh(pos,c)))]
        # own tile work — claim the (x,y,op) job so the pool below dedups it;
        # plant/weed tiles take one op, so also mark the tile serviced
        if isinstance(tile,dict) and (px,py) not in claimed:
            k=tile["kind"]
            if k=="PLANT":
                c=tile.get("crop"); cd=CROPS.get(c)
                if cd and tile.get("yield_units",0)>0 and (day-tile.get("planted_day",0)>=cd["harv"] or (cd["ongoing"] and day-tile.get("planted_day",0)>=cd["first"])):
                    claimed.add((px,py)); claimed.add((px,py,"HARVEST")); return ["HARVEST"]
                if not tile.get("watered_today"):
                    claimed.add((px,py)); claimed.add((px,py,"WATER")); return ["WATER"]
                if not cd["ongoing"] and day-tile.get("planted_day",0)>cd["maxd"]:
                    claimed.add((px,py)); claimed.add((px,py,"DIG")); return ["DIG"]
                # fertilize crops inside their growth window
                if inv.get("FERTILIZER",0)>0 and tile.get("fertilized_until_day",-1)<day and day-tile.get("planted_day",0)<cd["harv"]:
                    claimed.add((px,py)); return ["FERTILIZE"]
            elif k=="WEED": claimed.add((px,py)); claimed.add((px,py,"DIG")); return ["DIG"]
            elif k in ("COOP","PASTURE") and _animal(tile):
                # animal tiles need up to 4 ops/day — claim per-op so others can help
                # FEED consumes wheat from the UNIT's inventory, not the shed
                if not tile.get("fed_today") and inv.get("WHEAT",0)>0 and (px,py,"FEED") not in claimed:
                    claimed.add((px,py,"FEED")); return ["FEED"]
                # HARVEST collects the tile's accumulated product into inventory
                if tile.get("yield_units",0)>0 and (px,py,"HARVEST") not in claimed:
                    claimed.add((px,py,"HARVEST")); return ["HARVEST"]
                if not tile.get("cared_today") and (px,py,"CARE") not in claimed:
                    claimed.add((px,py,"CARE")); return ["CARE"]
                if tile.get("fertilizer_available") and (px,py,"COLLECT_FERTILIZER") not in claimed:
                    claimed.add((px,py,"COLLECT_FERTILIZER")); return ["COLLECT_FERTILIZER"]
        if tile is None:
            # if this tile has a pending job (build or assigned plant), do it
            pending_here=[j for j in jobs if j[0]==px and j[1]==py]
            if pending_here:
                bj=pending_here[0]
                if bj[2].startswith("BUILD_"):
                    claimed.add((px,py,bj[2])); return [bj[2]]
                if bj[2]=="PLANT":
                    c=bj[3] if len(bj)>3 else (want[0] if want else None)
                    if c and seeds.get(c,0)>0:
                        claimed.add((px,py,"PLANT")); return ["PLANT",c]
            elif (px,py) not in BARN and (px,py) not in CENTER and (px,py,"PLANT") not in claimed:
                c=want[0] if want else None
                if c and seeds.get(c,0)>0:
                    claimed.add((px,py,"PLANT")); return ["PLANT",c]
        # at shed: load wheat if animals are hungry, else grab a homeless animal
        if (px,py) in CENTER:
            hungry=any(j[2]=="FEED" for j in jobs)
            if hungry and inv.get("WHEAT",0)==0 and shed.get("WHEAT",0)>0:
                return ["PICKUP","WHEAT",min(6,shed["WHEAT"])]
            if inv.get("FERTILIZER",0)==0 and shed.get("FERTILIZER",0)>0:
                return ["PICKUP","FERTILIZER",min(3,shed["FERTILIZER"])]
            for sp in ("GOOSE","COW","SHEEP"):
                if shed.get(sp,0)>0 and free[ANIMAL_STRUCT[sp]]:
                    claimed.add(("FETCH",sp,ui)); return ["PICKUP",sp,1]
        # hungry animals: any wheat-less unit heads to the shed to load up
        if inv.get("WHEAT",0)==0 and any(j[2]=="FEED" for j in jobs) and shed.get("WHEAT",0)>0:
            if (px,py) in CENTER: return ["PICKUP","WHEAT",min(6,shed["WHEAT"])]
            return [_step(pos,min(CENTER,key=lambda c:_mh(pos,c)))]
        # shed-parked animals: one courier per species runs the fetch whenever
        # a home is free — buys are gated on capacity so the backlog stays
        # shallow, but it must clear even on busy days or herd buys stall
        for sp in ANIMALS:
            if shed.get(sp,0)>0 and free[ANIMAL_STRUCT[sp]] and ("FETCH",sp) not in claimed:
                claimed.add(("FETCH",sp))
                if (px,py) in CENTER: return ["PICKUP",sp,1]
                return [_step(pos,min(CENTER,key=lambda c:_mh(pos,c)))]
        # pending jobs — urgent (water/feed/harvest/dig/care) first, then the
        # BC model ranks the rest (plant/build/collect) by class minus distance.
        # FEED jobs only actionable by units already carrying wheat
        if jobs:
            pool=[j for j in jobs if (j[0],j[1],j[2]) not in claimed and not (j[2]=="FEED" and inv.get("WHEAT",0)==0)]
            urg=[j for j in pool if j[2] in URGENT or (unhoused_all>0 and j[2].startswith("BUILD_"))]
            pool=urg or pool
            if pool:
                bj_job=min(pool,key=lambda j:_mh(pos,(j[0],j[1])))
                bx,by,bj=bj_job[0],bj_job[1],bj_job[2]
                claimed.add((bx,by,bj))
                if (bx,by)==(px,py):
                    if bj.startswith("PLACE:"):
                        sp=bj.split(":")[1]
                        if inv.get(sp,0)>0: return ["PLACE",sp,1]
                        return ["PASS"]
                    if bj.startswith("BUILD_"): return [bj]
                    if bj=="PLANT":
                        c=bj_job[3] if len(bj_job)>3 else (want[0] if want else None)
                        if c and seeds.get(c,0)>0: return ["PLANT",c]
                        return ["PASS"]
                    return [bj]
                return [_step(pos,(bx,by))]
        return ["PASS"]

    farmer_op=work(units[0],0)
    hands=[work(units[i],i) for i in range(1,n)]
    return {"farmer":farmer_op,"hands":hands,"market":market}
