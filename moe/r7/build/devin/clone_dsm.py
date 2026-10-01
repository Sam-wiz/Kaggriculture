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
HERD_PLAN = [
    (1,5,"COW",2),(1,5,"SHEEP",3),
    (6,11,"GOOSE",4),(6,11,"COW",9),
    (7,15,"SHEEP",5),(9,18,"COW",3),(12,21,"SHEEP",3),
]
STRUCT_PLAN = [(0,"PASTURE",5),(2,"PASTURE",9),(5,"COOP",4),(8,"PASTURE",16),(10,"COOP",5),(13,"PASTURE",20),(16,"PASTURE",23)]
CROP_PLAN = [
    (0,2,"MELON",14,250),
    (10,16,"MELON",8,250),
    (2,18,"STRAWBERRY",30,400),
    (6,26,"TOMATO",15,300),
    (9,29,"CARROT",70,150),
]
FEED_BUFFER = 4
# barn zone: structures go in a compact block near home; crops never planted there
BARN = {(x,y) for x in range(0,5) for y in range(2,7)} - CENTER

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
                # one-time crops harvest at peak (maxd), ongoing at any yield
                ready = cd and t.get("yield_units",0)>0 and (age>=cd["harv"] or (cd["ongoing"] and age>=cd["first"]))
                if ready: jobs.append((x,y,"HARVEST"))
                elif not t.get("watered_today"): jobs.append((x,y,"WATER"))
            elif k in ("COOP","PASTURE"):
                structs[k]+=1
                a=_animal(t)
                if a:
                    if a in have: have[a]+=1
                    if not t.get("fed_today") and (shed.get("WHEAT",0)>0 or carried_wheat>0): jobs.append((x,y,"FEED"))
                    if t.get("yield_units",0)>0: jobs.append((x,y,"HARVEST"))
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
        while me["hires_today"]+sum(1 for o in market if o[0]=="HIRE")<want and len(market)<6:
            market.append(["HIRE"]); money-=12
        for d,q in sorted(LAND_DAYS.items()):
            if day>=d and q not in me["unlocked_quadrants"] and money>LAND_COST[q] and len(market)<10:
                market.append(["BUY_LAND"]); money-=LAND_COST[q]
        # feed first — keep the herd alive before growing it
        need=herd_n*2+8-shed.get("WHEAT",0)
        if day>=2 and need>0 and money>120 and len(market)<10:
            market.append(["BUY_PRODUCT","WHEAT",min(9,need)]); money-=10*min(9,need)
        # herd: one animal per turn, gated on free home AND stocked feed runway
        if shed.get("WHEAT",0)>=herd_n+2:
            for lo,hi,sp,tgt in HERD_PLAN:
                need=tgt-have[sp]-shed.get(sp,0)
                if lo<=day<=hi and need>0:
                    k=ANIMAL_STRUCT[sp]
                    if len(free[k])+shed.get(sp,0)>0 and money>ANIMALS[sp]["cost"]+500 and len(market)<10:
                        market.append(["BUY_ANIMAL",sp,1]); money-=ANIMALS[sp]["cost"]
                        break
        # seeds: buy toward the day's crop window, money-gated
        for lo,hi,c,tgt,minc in CROP_PLAN:
            if lo<=day<=hi and crops[c]<tgt and seeds.get(c,0)<5 and money>minc+CROPS[c]["seed"]*4 and len(market)<10:
                market.append(["BUY_SEED",c,4]); money-=CROPS[c]["seed"]*4
        if seeds.get("WHEAT",0)<6 and money>200 and len(market)<10:
            market.append(["BUY_SEED","WHEAT",4]); money-=40
        # standing sells — fertilizer is a production input, never sell it
        for prod in PRODUCTS:
            if prod=="FERTILIZER": continue
            if shed.get(prod,0)>=3 and len(market)<10:
                market.append(["SELL",prod,3])

    units=[me["farmer"]]+list(me.get("hands") or [])
    n=len(units); claimed=set()

    want=[c for lo,hi,c,tgt,mn in CROP_PLAN if lo<=day<=hi and crops[c]<tgt and seeds.get(c,0)>0]
    if seeds.get("WHEAT",0)>0 and day<29: want.append("WHEAT")
    # spread planting across all wanted crops, assigned round-robin per tile
    plant_jobs=[(x,y,"PLANT",want[(x+y)%len(want)]) for (x,y) in empties] if want else []

    tgt_struct={}
    for d,k,tg in STRUCT_PLAN:
        if day>=d: tgt_struct[k]=tg
    # placing animals is a dedicated center->structure errand, not a shared job:
    # units with nothing else to do run it via the PICKUP/deliver branches in work().
    for k,tg in tgt_struct.items():
        deficit=tg-structs[k]-sum(1 for j in jobs if j[2]=="BUILD_"+k)
        # build only when unhoused animals exist or free capacity is exhausted
        # and the herd plan still wants more of that kind
        unhoused=shed.get("GOOSE",0) if k=="COOP" else shed.get("COW",0)+shed.get("SHEEP",0)
        housed=sum(have[a] for a,s in ANIMAL_STRUCT.items() if s==k)
        planned=sum(tgt for lo,hi,sp,tgt in HERD_PLAN if ANIMAL_STRUCT[sp]==k and lo<=day)
        if deficit>0 and (unhoused>0 or housed+unhoused+len(free[k])<min(planned,tg)):
            for (x,y) in barn_empty[:min(deficit,2)]:
                jobs.append((x,y,"BUILD_"+k))

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
        # carrying goods -> shed run
        if goods>0:
            if (px,py) in CENTER: return ["DROP"]
            return [_step(pos,min(CENTER,key=lambda c:_mh(pos,c)))]
        # own tile work — first unit on the tile services it; others move on
        if isinstance(tile,dict) and (px,py) not in claimed:
            k=tile["kind"]
            if k=="PLANT":
                c=tile.get("crop"); cd=CROPS.get(c)
                if cd and tile.get("yield_units",0)>0 and (day-tile.get("planted_day",0)>=cd["harv"] or (cd["ongoing"] and day-tile.get("planted_day",0)>=cd["first"])):
                    claimed.add((px,py)); return ["HARVEST"]
                if not tile.get("watered_today"):
                    claimed.add((px,py)); return ["WATER"]
                if not cd["ongoing"] and day-tile.get("planted_day",0)>cd["maxd"]:
                    claimed.add((px,py)); return ["DIG"]
                # fertilize crops inside their growth window
                if inv.get("FERTILIZER",0)>0 and tile.get("fertilized_until_day",-1)<day and day-tile.get("planted_day",0)<cd["harv"]:
                    return ["FERTILIZE"]
            elif k=="WEED": claimed.add((px,py)); return ["DIG"]
            elif k in ("COOP","PASTURE") and _animal(tile):
                # animal tiles need up to 3 ops/day — claim per-op so others can help
                # FEED consumes wheat from the UNIT's inventory, not the shed
                if not tile.get("fed_today") and inv.get("WHEAT",0)>0 and (px,py,"F") not in claimed:
                    claimed.add((px,py,"F")); return ["FEED"]
                # HARVEST collects the tile's accumulated product into inventory
                if tile.get("yield_units",0)>0 and (px,py,"H") not in claimed:
                    claimed.add((px,py,"H")); return ["HARVEST"]
                if not tile.get("cared_today") and (px,py,"C") not in claimed:
                    claimed.add((px,py,"C")); return ["CARE"]
                if tile.get("fertilizer_available") and (px,py,"L") not in claimed:
                    claimed.add((px,py,"L")); return ["COLLECT_FERTILIZER"]
        if tile is None:
            # if this tile is a pending build or place target, do that job first
            pending_here=[j[2] for j in jobs if j[0]==px and j[1]==py]
            if pending_here:
                bj=pending_here[0]
                if bj.startswith("BUILD_"): return [bj]
            elif (px,py) not in BARN and (px,py) not in CENTER and (px,py) not in claimed:
                c=want[0] if want else None
                if c and seeds.get(c,0)>0:
                    claimed.add((px,py)); return ["PLANT",c]
        # at shed: load wheat if animals are hungry, else grab a homeless animal
        if (px,py) in CENTER:
            hungry=any(j[2]=="FEED" for j in jobs)
            if hungry and inv.get("WHEAT",0)==0 and shed.get("WHEAT",0)>0:
                return ["PICKUP","WHEAT",min(6,shed["WHEAT"])]
            if inv.get("FERTILIZER",0)==0 and shed.get("FERTILIZER",0)>0:
                return ["PICKUP","FERTILIZER",min(3,shed["FERTILIZER"])]
            for sp in ("GOOSE","COW","SHEEP"):
                if shed.get(sp,0)>0 and free[ANIMAL_STRUCT[sp]]: return ["PICKUP",sp,1]
        # hungry animals: any wheat-less unit heads to the shed to load up
        if inv.get("WHEAT",0)==0 and any(j[2]=="FEED" for j in jobs) and shed.get("WHEAT",0)>0:
            if (px,py) in CENTER: return ["PICKUP","WHEAT",min(6,shed["WHEAT"])]
            return [_step(pos,min(CENTER,key=lambda c:_mh(pos,c)))]
        # nearest pending job — urgent (water/feed/harvest/dig) beats chores (builds)
        # FEED jobs only actionable by units already carrying wheat
        if jobs:
            pool=[j for j in jobs if (j[0],j[1],j[2]) not in claimed and not (j[2]=="FEED" and inv.get("WHEAT",0)==0)]
            urg=[j for j in pool if j[2] in ("WATER","FEED","HARVEST","DIG","CARE")]
            pool=urg or [j for j in pool if not j[2].startswith("BUILD_")] or pool
            if pool:
                bx,by,bj=min(pool,key=lambda j:_mh(pos,j))
                claimed.add((bx,by,bj))
                if (bx,by)==(px,py):
                    if bj.startswith("PLACE:"):
                        sp=bj.split(":")[1]
                        if inv.get(sp,0)>0: return ["PLACE",sp,1]
                        return ["PASS"]
                    if bj.startswith("BUILD_"): return [bj]
                    return [bj]
                return [_step(pos,(bx,by))]
        # fill empty tiles
        if plant_jobs:
            pj=[j for j in plant_jobs if (j[0],j[1],"PLANT") not in claimed]
            if pj:
                bx,by,bj,bc=min(pj,key=lambda j:_mh(pos,j))
                claimed.add((bx,by,"PLANT"))
                if (bx,by)==(px,py) and seeds.get(bc,0)>0: return ["PLANT",bc]
                return [_step(pos,(bx,by))]
        # if shed has animals and free structs but we're not adjacent, head to center
        if any(shed.get(sp,0)>0 and free[ANIMAL_STRUCT[sp]] for sp in ANIMALS):
            return [_step(pos,min(CENTER,key=lambda c:_mh(pos,c)))]
        return ["PASS"]

    farmer_op=work(units[0],0)
    hands=[work(units[i],i) for i in range(1,n)]
    return {"farmer":farmer_op,"hands":hands,"market":market}
