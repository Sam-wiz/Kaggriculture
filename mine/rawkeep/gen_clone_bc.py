# Generate clone_bc.py — clone_dsm market/economy layer + learned BC unit dispatch.
# Weights embedded as flat lists; pure-python forward pass.
import numpy as np, json, sys

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
z = np.load(ROOT+"/moe/r7/build/opus/bc_weights_shift.npz")  # causal obs[t-1]->action[t] (leak fix)
W1=z["W1"]; b1=z["b1"]; W2=z["W2"]; b2=z["b2"]; W3=z["W3"]; b3=z["b3"]
labels=[str(s) for s in z["labels"]]

def fmt(a):
    return "["+",".join(f"{v:.5f}" for v in np.asarray(a).ravel())+"]"

agent_src = '''# clone_bc: decoded consensus economy + behavioral-cloned DSM dispatch policy.
# Unit ops chosen by a 2-layer MLP trained on 347k DSM unit-turns (bc_train.py).
# Inference = featurize -> forward -> mask illegal -> argmax, recomputed every turn.
import json as _json

DAYS=30
CENTER={(4,4),(5,4),(4,5),(5,5)}
PRODUCTS=["STRAWBERRY","MELON","MILK","WOOL","TOMATO","EGG","CARROT","WHEAT","FERTILIZER"]
CROPS={
 "WHEAT":{"seed":10,"first":2,"maxd":4,"ongoing":False},
 "CARROT":{"seed":20,"first":2,"maxd":3,"ongoing":False},
 "TOMATO":{"seed":50,"first":8,"maxd":8,"ongoing":True},
 "STRAWBERRY":{"seed":100,"first":10,"maxd":10,"ongoing":True},
 "MELON":{"seed":80,"first":10,"maxd":12,"ongoing":False}}
ANIMALS={"GOOSE":{"cost":300,"struct":"COOP"},"COW":{"cost":400,"struct":"PASTURE"},"SHEEP":{"cost":500,"struct":"PASTURE"}}
ANIMAL_STRUCT={"COW":"PASTURE","SHEEP":"PASTURE","GOOSE":"COOP"}
HIRES=[4,4,6,6,6,6,8,9,9,10]+[11]*18+[10,10]
LAND_DAYS={6:"NE",9:"SW"}
LAND_COST={"NE":1000,"SW":2000,"SE":4000}
HERD_PLAN=[(1,5,"COW",2),(1,5,"SHEEP",3),(6,11,"GOOSE",4),(6,11,"COW",9),
           (7,15,"SHEEP",5),(9,18,"COW",3),(12,21,"SHEEP",3)]
STRUCT_PLAN={0:("PASTURE",5),2:("PASTURE",9),5:("COOP",4),8:("PASTURE",16),10:("COOP",5),13:("PASTURE",20),16:("PASTURE",23)}
BARN={(x,y) for x in range(0,5) for y in range(2,7)} - CENTER
CROP_PLAN=[(0,2,"MELON",14,250),(10,16,"MELON",8,250),(2,18,"STRAWBERRY",30,400),
           (6,26,"TOMATO",15,300),(9,29,"CARROT",70,150)]

_ST={"step":-1,"assign":{}}
_LABELS=__LABELS__
_LI={c:i for i,c in enumerate(_LABELS)}
_W1=__W1__ ; _B1=__B1__ ; _W2=__W2__ ; _B2=__B2__ ; _W3=__W3__ ; _B3=__B3__
_D=__D__; _H1=__H1__; _H2=__H2__; _K=__K__

def _fwd(v):
    a1=[0.0]*_H1
    for j in range(_H1):
        s=_B1[j]; off=j
        for i in range(_D): s+=v[i]*_W1[i*_H1+off]
        a1[j]=s if s>0 else 0.0
    a2=[0.0]*_H2
    for j in range(_H2):
        s=_B2[j]
        for i in range(_H1): s+=a1[i]*_W2[i*_H2+j]
        a2[j]=s if s>0 else 0.0
    z=[0.0]*_K
    for j in range(_K):
        s=_B3[j]
        for i in range(_H2): s+=a2[i]*_W3[i*_K+j]
        z[j]=s
    return z

_MK=["water","harvest","feed","care","cfert","dig","empty","struct_free"]
_MKX=_MK+["plant","pasture_free","coop_free"]

def _masks(tiles):
    m={k:set() for k in _MKX}
    for y,row in enumerate(tiles):
        for x,t in enumerate(row):
            if t is None: m["empty"].add((x,y)); continue
            if not isinstance(t,dict): continue
            k=t.get("kind")
            if k=="WEED": m["dig"].add((x,y))
            elif k=="PLANT":
                m["plant"].add((x,y))
                if not t.get("watered_today"): m["water"].add((x,y))
                if (t.get("yield_units") or 0)>0: m["harvest"].add((x,y))
            elif k in ("COOP","PASTURE"):
                if t.get("animal"):
                    if not t.get("fed_today"): m["feed"].add((x,y))
                    if not t.get("cared_today"): m["care"].add((x,y))
                    if t.get("fertilizer_available"): m["cfert"].add((x,y))
                    if (t.get("yield_units") or 0)>0: m["harvest"].add((x,y))
                else:
                    m["struct_free"].add((x,y))
                    m["pasture_free" if k=="PASTURE" else "coop_free"].add((x,y))
    return m

def _bfs(tiles,masks,sx,sy):
    H=len(tiles); W=len(tiles[0])
    found={}; shed_dir=None
    seen={(sx,sy)}; q=[(sx,sy,0,0,0)]; qi=0
    while qi<len(q) and (len(found)<len(_MKX) or shed_dir is None):
        x,y,d,fdx,fdy=q[qi]; qi+=1
        for k in _MKX:
            if k not in found and (x,y) in masks[k]: found[k]=(d,fdx,fdy)
        if (x,y) in CENTER and shed_dir is None: shed_dir=(d,fdx,fdy)
        if len(found)==len(_MKX) and shed_dir is not None: break
        for dx,dy in ((0,-1),(1,0),(0,1),(-1,0)):
            nx,ny=x+dx,y+dy
            if 0<=nx<W and 0<=ny<H and (nx,ny) not in seen:
                seen.add((nx,ny)); q.append((nx,ny,d+1,dx if d==0 else fdx,dy if d==0 else fdy))
    return {k:found.get(k,(99,0,0)) for k in _MKX}, (shed_dir or (99,0,0))

def _feats(me,priv,masks,day,hour,money,hires,quads,shed,inv,ui,ux,uy,dists,dshed,t0):
    c={k:len(v) for k,v in masks.items()}
    on={"empty":t0 is None}
    if isinstance(t0,dict):
        k=t0.get("kind")
        on={"weed":k=="WEED","plant":k=="PLANT","animal":bool(t0.get("animal")),
            "watered":t0.get("watered_today"),"yield":t0.get("yield_units") or 0,
            "fed":t0.get("fed_today"),"cared":t0.get("cared_today"),
            "fert_av":t0.get("fertilizer_available")}
    return [
        ux/9.,uy/9.,day/29.,hour/23.,min(money,50000)/50000.,hires/10.,quads,
        min(shed.get("WHEAT",0),50)/50.,min(shed.get("FERTILIZER",0),50)/50.,
        min(sum(shed.get(a,0) for a in ANIMALS),10)/10.,
        min(c["water"],40)/40.,min(c["harvest"],40)/40.,min(c["feed"],30)/30.,
        min(c["care"],30)/30.,min(c["cfert"],30)/30.,min(c["dig"],30)/30.,
        min(c["empty"],60)/60.,min(c["struct_free"],30)/30.,
        min(dists["water"][0],20)/20.,min(dists["harvest"][0],20)/20.,min(dists["feed"][0],20)/20.,
        min(dists["care"][0],20)/20.,min(dists["cfert"][0],20)/20.,min(dists["dig"][0],20)/20.,
        min(dists["empty"][0],20)/20.,min(dists["struct_free"][0],20)/20.,
        dists["water"][1],dists["water"][2],dists["harvest"][1],dists["harvest"][2],
        dists["feed"][1],dists["feed"][2],dists["care"][1],dists["care"][2],
        dists["dig"][1],dists["dig"][2],dists["empty"][1],dists["empty"][2],
        min(dshed[0],20)/20.,dshed[1],dshed[2],
        min(inv.get("WHEAT",0),10)/10.,min(inv.get("FERTILIZER",0),10)/10.,
        min(sum(v for k,v in inv.items() if k not in ANIMALS and k not in ("WHEAT","FERTILIZER")),10)/10.,
        min(sum(inv.get(a,0) for a in ANIMALS),10)/10.,
        1 if on.get("empty") else 0,1 if on.get("weed") else 0,
        1 if on.get("plant") else 0,1 if on.get("animal") else 0,
        1 if on.get("watered") else 0,min(on.get("yield") or 0,8)/8.,
        1 if on.get("fed") else 0,1 if on.get("cared") else 0,1 if on.get("fert_av") else 0,
        min(ui,10)/10.,1.0 if ui==0 else 0.0]

def _emit(cls,ctx):
    """map predicted class -> concrete op; return None if illegal in ctx"""
    tile=ctx["tile"]; inv=ctx["inv"]; shed=ctx["shed"]; seeds=ctx["seeds"]
    at_shed=ctx["at_shed"]; day=ctx["day"]
    if cls in ("NORTH","SOUTH","EAST","WEST","PASS"): return [cls]
    if cls=="WATER":
        if isinstance(tile,dict) and tile.get("kind")=="PLANT" and not tile.get("watered_today"): return ["WATER"]
        return None
    if cls=="FERTILIZE":
        if isinstance(tile,dict) and tile.get("kind")=="PLANT" and inv.get("FERTILIZER",0)>0: return ["FERTILIZE"]
        return None
    if cls=="HARVEST":
        if isinstance(tile,dict):
            k=tile.get("kind")
            if k=="PLANT":
                cd=CROPS.get(tile.get("crop"))
                if cd and (tile.get("yield_units") or 0)>0 and day-tile.get("planted_day",0)>=cd["first"]: return ["HARVEST"]
            elif tile.get("animal") and (tile.get("yield_units") or 0)>0: return ["HARVEST"]
        return None
    if cls=="FEED":
        if isinstance(tile,dict) and tile.get("animal") and not tile.get("fed_today") and inv.get("WHEAT",0)>0: return ["FEED"]
        return None
    if cls=="CARE":
        if isinstance(tile,dict) and tile.get("animal") and not tile.get("cared_today"): return ["CARE"]
        return None
    if cls=="COLLECT_FERTILIZER":
        if isinstance(tile,dict) and tile.get("animal") and tile.get("fertilizer_available"): return ["COLLECT_FERTILIZER"]
        return None
    if cls=="DIG":
        if isinstance(tile,dict) and tile.get("kind") in ("WEED","PLANT","COOP","PASTURE") and not tile.get("animal"): return ["DIG"]
        return None
    if cls=="BUILD_COOP" or cls=="BUILD_PASTURE":
        if tile is None: return [cls]
        return None
    if cls.startswith("PLANT:"):
        c=cls.split(":")[1]
        if tile is None and seeds.get(c,0)>0: return ["PLANT",c]
        return None
    if cls.startswith("PICKUP:"):
        it=cls.split(":")[1]
        if at_shed and shed.get(it,0)>0:
            # preconditions the expert implicitly satisfies: wheat only if hungry
            # animals exist, fert only if crops exist, animals only if a home is free
            cnts=ctx["cnts"]
            if it=="WHEAT" and cnts["feed"]==0: return None
            if it=="FERTILIZER" and cnts["plant"]==0: return None
            if it in ANIMALS and cnts.get(("pasture_free" if ANIMAL_STRUCT[it]=="PASTURE" else "coop_free"),0)==0: return None
            n={"WHEAT":6,"FERTILIZER":3}.get(it,1)
            return ["PICKUP",it,min(n,shed[it])]
        return None
    if cls.startswith("PLACE:"):
        it=cls.split(":")[1]
        if it in ANIMALS:
            want=ANIMAL_STRUCT[it]
            if isinstance(tile,dict) and tile.get("kind")==want and not tile.get("animal") and inv.get(it,0)>0:
                return ["PLACE",it,1]
            return None
        if at_shed and inv.get(it,0)>0: return ["PLACE",it,inv[it]]
        return None
    if cls=="DROP":
        if at_shed and any(v>0 for v in inv.values()): return ["DROP"]
        return None
    return None

def agent(obs,config=None):
    p=int(obs.get("player") or 0)
    day=int(obs.get("day") or 0); hour=int(obs.get("hour") or 0)
    me=obs["farms"][p]; tiles=me["tiles"]; money=me["money"]
    priv=obs.get("private") or {}
    shed=priv.get("shed") or {}; seeds=priv.get("seeds") or {}
    invs=priv.get("inventories") or []

    # ---- market layer: decoded consensus program ----
    have={"COW":0,"SHEEP":0,"GOOSE":0}; structs={"PASTURE":0,"COOP":0}; free={"PASTURE":0,"COOP":0}
    crops={c:0 for c in CROPS}
    for row in tiles:
        for t in row:
            if not isinstance(t,dict): continue
            k=t.get("kind")
            if k=="PLANT":
                c=t.get("crop")
                if c in crops: crops[c]+=1
            elif k in ("COOP","PASTURE"):
                structs[k]+=1
                a=t.get("animal")
                if a:
                    a=a if isinstance(a,str) else (a or {}).get("kind")
                    if a in have: have[a]+=1
                else: free[k]+=1
    herd_n=sum(have.values())
    market=[]
    # DSM market stream (decoded): zero-float — hires burst early, animals day 0,
    # seeds trickled 1-2/turn as consumed, standing SELL-3 on every product always.
    HIRE_TGT={0:4,1:8,2:6,3:6,4:6,5:6,6:8,7:9,8:9,9:10}
    htgt=HIRE_TGT.get(day,10) if day<28 else 10
    while me["hires_today"]+sum(1 for o in market if o[0]=="HIRE")<htgt and len(market)<6:
        market.append(["HIRE"])
    if day==0:
        # the day-0 animal burst: ~2 cows + 3 sheep straight into the shed
        for sp,n in (("COW",2),("SHEEP",3)):
            for _ in range(n):
                if money>ANIMALS[sp]["cost"]+200 and len(market)<10:
                    market.append(["BUY_ANIMAL",sp,1]); money-=ANIMALS[sp]["cost"]
        if money>50 and len(market)<10: market.append(["BUY_PRODUCT","WHEAT",5]); money-=50
    # land window (d6 NE, d9 SW — median decoded)
    for d,q in sorted(LAND_DAYS.items()):
        if day>=d and q not in me["unlocked_quadrants"] and money>LAND_COST[q]+200 and len(market)<10:
            market.append(["BUY_LAND"]); money-=LAND_COST[q]
    # follow-up herd buys (d6+ cows/geese, sporadic sheep)
    ANIMAL_BUYS={6:[("COW",4),("GOOSE",2)],7:[("COW",1)],9:[("COW",2),("SHEEP",1)],
                 12:[("SHEEP",1)],15:[("SHEEP",1)],18:[("COW",1)]}
    for d,lst in ANIMAL_BUYS.items():
        if day>=d:
            for sp,n in lst:
                need=n-have[sp]-shed.get(sp,0)
                if need>0 and (d==0 or free[ANIMAL_STRUCT[sp]]+shed.get(sp,0)>0) and money>ANIMALS[sp]["cost"]+300 and len(market)<10:
                    market.append(["BUY_ANIMAL",sp,1]); money-=ANIMALS[sp]["cost"]
                    break
    # feed-wheat: trickle + bulk pulse when shed is thin vs herd
    if day>=1:
        feed_need=max(0,herd_n*2+4-shed.get("WHEAT",0))
        if feed_need>0 and money>130 and len(market)<10:
            market.append(["BUY_PRODUCT","WHEAT",min(13,feed_need)]); money-=10*min(13,feed_need)
        elif money>30 and len(market)<10:
            market.append(["BUY_PRODUCT","WHEAT",1]); money-=10
    # seed trickle: keep a small staging buffer per in-window crop (buy as consumed)
    SEED_WIN={"MELON":(0,2,2,2),"STRAWBERRY":(2,18,1,3),"WHEAT":(0,28,1,3),
              "TOMATO":(11,25,1,2),"CARROT":(16,27,6,4)}
    for c,(lo,hi,sz,buf) in SEED_WIN.items():
        if lo<=day<=hi and seeds.get(c,0)<buf and money>CROPS[c]["seed"]*sz+60 and len(market)<10:
            market.append(["BUY_SEED",c,sz]); money-=CROPS[c]["seed"]*sz
    # standing sell stream — SELL 3 on every product, every turn (no-op when empty).
    # WHEAT is feed: never sold. FERTILIZER is an input: sell the surplus over a
    # working buffer (DSM trickle-sells it for early hire money).
    for prod in PRODUCTS:
        if prod=="WHEAT": continue
        if prod=="FERTILIZER" and shed.get("FERTILIZER",0)<12: continue
        if len(market)<10:
            market.append(["SELL",prod,3])
    if day>=DAYS-1:
        market=[]
        for prod in PRODUCTS:
            if shed.get(prod,0)>0: market.append(["SELL",prod,1000])
        while me["hires_today"]+sum(1 for o in market if o[0]=="HIRE")<6 and len(market)<10:
            market.append(["HIRE"])

    # ---- learned dispatch with commitment ----
    # Each unit holds an intent (job_class, target tile) until the job completes
    # or the target goes stale — the model only re-predicts on invalidation.
    masks=_masks(tiles)
    units=[me["farmer"]]+list(me.get("hands") or [])
    # structure deficit vs plan -> claimable build sites on barn-empties
    tgt_struct={"PASTURE":0,"COOP":0}
    for d in sorted(STRUCT_PLAN):
        if day>=d: tgt_struct[STRUCT_PLAN[d][0]]=STRUCT_PLAN[d][1]
    struct_jobs=[]
    for k in ("PASTURE","COOP"):
        deficit=tgt_struct[k]-structs[k]
        if deficit>0:
            for xy in BARN:
                x,y=xy
                if 0<=y<len(tiles) and 0<=x<len(tiles[y]) and tiles[y][x] is None:
                    struct_jobs.append(("BUILD_"+k,x,y))
                    deficit-=1
                    if deficit<=0: break
    st=obs.get("step")
    if st is None: st=day*24+hour
    if st==0 or st<_ST["step"] or hour==0:
        _ST["assign"]={}   # new game, or midnight: hands despawn/re-hire -> drop intents
    _ST["step"]=st
    assign=_ST["assign"]
    cnts={k:len(v) for k,v in masks.items()}
    DIRTOMV={(0,-1):"NORTH",(1,0):"EAST",(0,1):"SOUTH",(-1,0):"WEST"}

    def step_to(ux,uy,tx,ty):
        dx,dy=tx-ux,ty-uy
        if dx==0 and dy==0: return ["PASS"]
        if abs(dx)>=abs(dy): return ["EAST" if dx>0 else "WEST"]
        return ["SOUTH" if dy>0 else "NORTH"]

    def nearest_in(maskset,ux,uy):
        best=None
        for (x,y) in maskset:
            dd=abs(ux-x)+abs(uy-y)
            if best is None or dd<best[0]: best=(dd,x,y)
        return best

    def valid(asn,ui,inv,t0):
        cl,(tx,ty)=asn
        if cl=="SHED": return (tx,ty) in CENTER or True
        if not (0<=ty<len(tiles) and 0<=tx<len(tiles[ty])): return False
        tl=tiles[ty][tx]
        if cl=="WATER": return isinstance(tl,dict) and tl.get("kind")=="PLANT" and not tl.get("watered_today")
        if cl=="HARVEST": return isinstance(tl,dict) and (tl.get("yield_units") or 0)>0
        if cl=="FEED": return isinstance(tl,dict) and tl.get("animal") and not tl.get("fed_today") and inv.get("WHEAT",0)>0
        if cl=="CARE": return isinstance(tl,dict) and tl.get("animal") and not tl.get("cared_today")
        if cl=="COLLECT_FERTILIZER": return isinstance(tl,dict) and tl.get("animal") and tl.get("fertilizer_available")
        if cl=="DIG": return isinstance(tl,dict) and tl.get("kind") in ("WEED","PLANT","COOP","PASTURE") and not tl.get("animal")
        if cl=="FERTILIZE": return isinstance(tl,dict) and tl.get("kind")=="PLANT" and inv.get("FERTILIZER",0)>0
        if cl.startswith("PLANT:"): return tl is None and seeds.get(cl.split(":")[1],0)>0
        if cl in ("BUILD_COOP","BUILD_PASTURE"): return tl is None
        if cl.startswith("PICKUP:"): return shed.get(cl.split(":")[1],0)>0
        if cl=="DROP": return any(v>0 for v in inv.values())
        if cl.startswith("PLACE:"):
            it=cl.split(":")[1]
            if it in ANIMALS:
                return inv.get(it,0)>0 and isinstance(tl,dict) and tl.get("kind")==ANIMAL_STRUCT[it] and not tl.get("animal")
            return inv.get(it,0)>0
        return False

    def emit_at(asn,ux,uy,inv,t0,at_shed):
        """unit stands on/intent resolved -> concrete op or None if it would no-op"""
        cl,(tx,ty)=asn
        if cl=="SHED": return None
        if cl in ("WATER","HARVEST","FEED","CARE","COLLECT_FERTILIZER","DIG","FERTILIZE","BUILD_COOP","BUILD_PASTURE"):
            return [cl]
        if cl.startswith("PLANT:"): return ["PLANT",cl.split(":")[1]]
        if cl.startswith("PICKUP:"):
            it=cl.split(":")[1]
            if at_shed and shed.get(it,0)>0:
                if it=="WHEAT" and cnts["feed"]==0: return None
                if it=="FERTILIZER" and cnts["plant"]==0: return None
                if it in ANIMALS and cnts.get("pasture_free" if ANIMAL_STRUCT[it]=="PASTURE" else "coop_free",0)==0: return None
                return ["PICKUP",it,min({"WHEAT":6,"FERTILIZER":3}.get(it,1),shed[it])]
            return None
        if cl=="DROP":
            if at_shed and any(v>0 for v in inv.values()): return ["DROP"]
            return None
        if cl.startswith("PLACE:"):
            it=cl.split(":")[1]
            if it in ANIMALS:
                return ["PLACE",it,1]
            if at_shed and inv.get(it,0)>0: return ["PLACE",it,inv[it]]
            return None
        return None

    def target_for(cl,ux,uy,inv):
        """(cl, (tx,ty)) intent for a predicted class; ('SHED',center) or None"""
        if cl=="FEED":
            if inv.get("WHEAT",0)>0:
                b=nearest_in(masks["feed"],ux,uy); return ("FEED",(b[1],b[2])) if b else None
            b=nearest_in(CENTER,ux,uy); return ("SHED",(b[1],b[2])) if b else None
        if cl in ("WATER","HARVEST","CARE","COLLECT_FERTILIZER","DIG"):
            mk={"WATER":"water","HARVEST":"harvest","CARE":"care","COLLECT_FERTILIZER":"cfert","DIG":"dig"}[cl]
            b=nearest_in(masks[mk],ux,uy); return (cl,(b[1],b[2])) if b else None
        if cl=="FERTILIZE":
            b=nearest_in(masks["plant"],ux,uy); return (cl,(b[1],b[2])) if b else None
        if cl.startswith("PLANT:"):
            if seeds.get(cl.split(":")[1],0)<=0: return None
            b=nearest_in(masks["empty"],ux,uy); return (cl,(b[1],b[2])) if b else None
        if cl in ("BUILD_COOP","BUILD_PASTURE"):
            sites=[(x,y) for n2,x,y in struct_jobs if n2==cl] or list(masks["empty"])
            if not sites: return None
            b=min(sites,key=lambda s:abs(ux-s[0])+abs(uy-s[1])); return (cl,(b[0],b[1]))
        if cl.startswith("PICKUP:") or cl=="DROP" or (cl.startswith("PLACE:") and cl.split(":")[1] not in ANIMALS):
            it=cl.split(":")[1] if ":" in cl else None
            if cl.startswith("PICKUP:") and it:
                if it=="WHEAT" and cnts["feed"]==0: return None
                if it=="FERTILIZER" and cnts["plant"]==0: return None
                if it in ANIMALS and cnts.get("pasture_free" if ANIMAL_STRUCT[it]=="PASTURE" else "coop_free",0)==0: return None
                if shed.get(it,0)==0: return None
            b=nearest_in(CENTER,ux,uy); return (cl,(b[1],b[2])) if b else None
        if cl.startswith("PLACE:"):
            it=cl.split(":")[1]
            ms="pasture_free" if ANIMAL_STRUCT[it]=="PASTURE" else "coop_free"
            b=nearest_in(masks[ms],ux,uy); return (cl,(b[1],b[2])) if b else None
        return None

    claimed_sites=set()
    ops_out=[]
    for ui,pos in enumerate(units):
        if not isinstance(pos,(list,tuple)) or len(pos)<2: ops_out.append(["PASS"]); continue
        ux,uy=int(pos[0]),int(pos[1])
        if not (0<=uy<len(tiles) and 0<=ux<len(tiles[uy])): ops_out.append(["PASS"]); continue
        inv=invs[ui] if ui<len(invs) else {}
        inv=inv if isinstance(inv,dict) else {}
        t0=tiles[uy][ux]
        at_shed=(ux,uy) in CENTER
        # hard precedence: cargo decides the mission (mirrors the expert's
        # structure — a loaded unit finishes its delivery, never detours)
        carried=[sp for sp in ANIMALS if inv.get(sp,0)>0]
        if carried:
            sp=carried[0]; want=ANIMAL_STRUCT[sp]
            if isinstance(t0,dict) and t0.get("kind")==want and not t0.get("animal"):
                ops_out.append(["PLACE",sp,1]); continue
            b=nearest_in(masks["pasture_free" if want=="PASTURE" else "coop_free"],ux,uy)
            if b:
                if b[0]==0: ops_out.append(["PLACE",sp,1]); continue
                ops_out.append(step_to(ux,uy,b[1],b[2])); continue
        elif inv.get("WHEAT",0)>0 and masks["feed"]:
            # carrying feed with hungry animals out -> finish the feed route
            if isinstance(t0,dict) and t0.get("animal") and not t0.get("fed_today"):
                ops_out.append(["FEED"]); continue
            b=nearest_in(masks["feed"],ux,uy)
            if b:
                if b[0]==0: ops_out.append(["FEED"]); continue
                ops_out.append(step_to(ux,uy,b[1],b[2])); continue
        elif sum(v for k2,v in inv.items() if k2 not in ANIMALS and k2 not in ("WHEAT","FERTILIZER"))>0:
            # carrying saleable product -> finish the shed run
            if at_shed:
                its=[k2 for k2,v in inv.items() if v>0 and k2 not in ANIMALS and k2 not in ("WHEAT","FERTILIZER")]
                if its: ops_out.append(["PLACE",its[0],inv[its[0]]]); continue
            b=nearest_in(CENTER,ux,uy)
            if b and b[0]>0: ops_out.append(step_to(ux,uy,b[1],b[2])); continue
        # existing intent still valid -> keep executing
        asn=assign.get(ui)
        if asn and valid(asn,ui,inv,t0):
            cl,(tx,ty)=asn
            if cl=="SHED" or (cl.split(":")[0] in ("PICKUP",) ) or cl=="DROP" or (cl.startswith("PLACE:") and cl.split(":")[1] not in ANIMALS):
                if at_shed:
                    op=emit_at(asn,ux,uy,inv,t0,True)
                    if op: ops_out.append(op); assign.pop(ui,None); continue
                    assign.pop(ui,None); asn=None
                else:
                    b=nearest_in(CENTER,ux,uy); ops_out.append(step_to(ux,uy,b[1],b[2])); continue
            elif (ux,uy)==(tx,ty):
                op=emit_at(asn,ux,uy,inv,t0,at_shed)
                ops_out.append(op); assign.pop(ui,None); continue
            else:
                ops_out.append(step_to(ux,uy,tx,ty)); continue
        # re-predict: model picks the job class, we route it
        dists,dshed=_bfs(tiles,masks,ux,uy)
        v=_feats(me,priv,masks,day,hour,money,me["hires_today"],len(me["unlocked_quadrants"]),
                 shed,inv,ui,ux,uy,dists,dshed,t0)
        z=_fwd(v)
        order=sorted(range(_K),key=lambda j:-z[j])
        op=None
        for j in order[:10]:
            cl=_LABELS[j]
            if cl in ("PASS","MOVE_IDLE"): break
            ctx={"tile":t0,"inv":inv,"shed":shed,"seeds":seeds,"at_shed":at_shed,"day":day,"cnts":cnts}
            op=_emit(cl,ctx)
            if op is not None: break
            asn2=target_for(cl,ux,uy,inv)
            if asn2:
                c2,(tx2,ty2)=asn2
                if (tx2,ty2) in claimed_sites: continue
                claimed_sites.add((tx2,ty2)); assign[ui]=asn2
                if (ux,uy)==(tx2,ty2):
                    op=emit_at(asn2,ux,uy,inv,t0,at_shed)
                    if op is None: assign.pop(ui,None); continue
                elif c2=="SHED" or asn2[0]=="SHED":
                    op=step_to(ux,uy,tx2,ty2)
                else:
                    op=step_to(ux,uy,tx2,ty2)
                break
        if op is None:
            # coverage fallback — never idle while work exists
            if len(claimed_sites)<3 and struct_jobs:
                sj=[s for s in struct_jobs if (s[1],s[2]) not in claimed_sites]
                if sj:
                    jn,jx,jy=min(sj,key=lambda s:abs(ux-s[1])+abs(uy-s[2]))
                    claimed_sites.add((jx,jy))
                    op=[jn] if (jx,jy)==(ux,uy) else step_to(ux,uy,jx,jy)
            if op is None:
                best=None
                for k in ("feed","water","harvest","care","cfert","dig"):
                    dd=nearest_in(masks[k],ux,uy)
                    if dd and (best is None or dd[0]<best[0]): best=dd
                if best: op=step_to(ux,uy,best[1],best[2]) if best[0]>0 else None
                if op is None and best and best[0]==0:
                    for k in ("feed","water","harvest","care","cfert","dig"):
                        if (ux,uy) in masks[k]: op=[{"feed":"FEED","water":"WATER","harvest":"HARVEST","care":"CARE","cfert":"COLLECT_FERTILIZER","dig":"DIG"}[k]]; break
                if op is None:
                    b=nearest_in(masks["empty"],ux,uy)
                    if b and b[0]>0: op=step_to(ux,uy,b[1],b[2])
        ops_out.append(op or ["PASS"])
    # ---- coverage floor: survival jobs get a unit even if the model looked away ----
    claimed_tiles={a2[1] for a2 in assign.values()} | claimed_sites
    urgent=[("WATER",x,y) for (x,y) in masks["water"]] + [("FEED",x,y) for (x,y) in masks["feed"]]
    for cl,x,y in urgent:
        if (x,y) in claimed_tiles: continue
        best=None
        for i,po in enumerate(units):
            if not isinstance(po,(list,tuple)) or len(po)<2: continue
            oo=ops_out[i]
            if oo and oo[0] not in ("NORTH","SOUTH","EAST","WEST","PASS"): continue
            iv=invs[i] if i<len(invs) else {}
            iv=iv if isinstance(iv,dict) else {}
            if any(iv.get(sp,0)>0 for sp in ANIMALS): continue   # don't steal animal porters
            if cl=="FEED" and iv.get("WHEAT",0)==0: continue
            dd=abs(po[0]-x)+abs(po[1]-y)
            if best is None or dd<best[0]: best=(dd,i)
        if best is None and cl=="FEED" and shed.get("WHEAT",0)>0:
            # nobody carrying wheat -> nearest idle unit fetches from shed
            for i,po in enumerate(units):
                if not isinstance(po,(list,tuple)): continue
                oo=ops_out[i]
                if oo and oo[0] not in ("NORTH","SOUTH","EAST","WEST","PASS"): continue
                iv=invs[i] if i<len(invs) else {}
                iv=iv if isinstance(iv,dict) else {}
                if any(iv.get(sp,0)>0 for sp in ANIMALS): continue
                dd=min(abs(po[0]-cx)+abs(po[1]-cy) for cx,cy in CENTER)
                if best is None or dd<best[0]: best=(dd,i,"SHED")
        if best is None: continue
        i=best[1]; po=units[i]
        if len(best)==3:
            cx,cy=min(CENTER,key=lambda c:abs(po[0]-c[0])+abs(po[1]-c[1]))
            assign[i]=("PICKUP:WHEAT",(cx,cy)); claimed_tiles.add((x,y))
            ops_out[i]=["PICKUP","WHEAT",min(6,shed.get("WHEAT",1))] if (po[0],po[1])==(cx,cy) else step_to(po[0],po[1],cx,cy)
        else:
            assign[i]=(cl,(x,y)); claimed_tiles.add((x,y))
            ops_out[i]=[cl] if (po[0],po[1])==(x,y) else step_to(po[0],po[1],x,y)
    # ---- planting floor: keep the crop pipeline full like the stream program ----
    want_crops=[c for lo,hi,c,tgt,mn in CROP_PLAN if lo<=day<=hi and crops.get(c,0)<tgt and seeds.get(c,0)>0]
    if seeds.get("WHEAT",0)>0 and day<28: want_crops.append("WHEAT")
    if want_crops:
        planted=[i for i,o in enumerate(ops_out) if o and o[0]=="PLANT"]
        cap=min(3,len(want_crops))
        for i,po in enumerate(units):
            if len(planted)>=cap or not want_crops: break
            if not isinstance(po,(list,tuple)) or len(po)<2: continue
            oo=ops_out[i]
            if oo and oo[0] not in ("NORTH","SOUTH","EAST","WEST","PASS"): continue
            iv=invs[i] if i<len(invs) else {}
            iv=iv if isinstance(iv,dict) else {}
            if any(iv.get(sp,0)>0 for sp in ANIMALS): continue
            c=want_crops[i%len(want_crops)]
            if seeds.get(c,0)<=0: continue
            if (po[0],po[1]) in CENTER: continue
            t00=tiles[po[1]][po[0]]
            if t00 is None:
                ops_out[i]=["PLANT",c]; planted.append(i); assign.pop(i,None)
            else:
                b=nearest_in(masks["empty"],po[0],po[1])
                if b and b[0]<=4:
                    assign[i]=("PLANT:"+c,(b[1],b[2])); claimed_tiles.add((b[1],b[2]))
                    ops_out[i]=step_to(po[0],po[1],b[1],b[2])
    farmer_op=ops_out[0] if ops_out else ["PASS"]
    return {"farmer":farmer_op,"hands":ops_out[1:],"market":market}
'''

D = W1.shape[0]; H1=W1.shape[1]; H2=W2.shape[1]; K=W3.shape[1]
agent_src = (agent_src
    .replace("__LABELS__", repr(labels))
    .replace("__W1__", fmt(W1)).replace("__B1__", fmt(b1))
    .replace("__W2__", fmt(W2)).replace("__B2__", fmt(b2))
    .replace("__W3__", fmt(W3)).replace("__B3__", fmt(b3))
    .replace("__D__", str(D)).replace("__H1__", str(H1))
    .replace("__H2__", str(H2)).replace("__K__", str(K)))

out = ROOT+"/moe/r7/build/devin/clone_bc.py"
open(out,"w").write(agent_src)
print("wrote", out, f"({len(agent_src)} bytes)")
