# Graft the learned job-priority model into clone_dsm: nearest-first pick ->
# argmax over model logits per job class + distance tiebreak.
import numpy as np

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
z = np.load(ROOT+"/moe/r7/build/opus/bc_weights_shift.npz")  # causal obs[t-1]->action[t] (leak fix)
W1,b1,W2,b2,W3,b3 = z["W1"],z["b1"],z["W2"],z["b2"],z["W3"],z["b3"]
labels=[str(s) for s in z["labels"]]

def fmt(a): return "["+",".join(f"{v:.5f}" for v in np.asarray(a).ravel())+"]"

src = open(ROOT+"/moe/r7/build/devin/clone_dsm.py").read()

model_code = '''
# --- BC job-priority model (trained on 347k DSM unit-turns) ---
_LABELS=__LABELS__
_LI={c:i for i,c in enumerate(_LABELS)}
_W1=__W1__;_B1=__B1__;_W2=__W2__;_B2=__B2__;_W3=__W3__;_B3=__B3__
_D=__D__;_H1=__H1__;_H2=__H2__;_K=__K__
_MKEYS=["water","harvest","feed","care","cfert","dig","empty","struct_free","plant","pasture_free","coop_free"]

def _fwd(v):
    a1=[0.0]*_H1
    for j in range(_H1):
        s=_B1[j]
        for i in range(_D): s+=v[i]*_W1[i*_H1+j]
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

def _masks_of(tiles):
    m={k:set() for k in _MKEYS}
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

def _nears(tiles,masks,sx,sy):
    H=len(tiles);W=len(tiles[0]);found={};sd=None
    seen={(sx,sy)};q=[(sx,sy,0,0,0)];qi=0
    while qi<len(q) and (len(found)<len(_MKEYS) or sd is None):
        x,y,d,fdx,fdy=q[qi];qi+=1
        for k in _MKEYS:
            if k not in found and (x,y) in masks[k]: found[k]=(d,fdx,fdy)
        if (x,y) in CENTER and sd is None: sd=(d,fdx,fdy)
        if len(found)==len(_MKEYS) and sd is not None: break
        for dx,dy in ((0,-1),(1,0),(0,1),(-1,0)):
            nx,ny=x+dx,y+dy
            if 0<=nx<W and 0<=ny<H and (nx,ny) not in seen:
                seen.add((nx,ny));q.append((nx,ny,d+1,dx if d==0 else fdx,dy if d==0 else fdy))
    return {k:found.get(k,(99,0,0)) for k in _MKEYS}, (sd if sd is not None else (99,0,0))

def _feats_of(day,hour,money,hires,quads,shed,inv,ui,ux,uy,cnts,dists,dshed,t0):
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
        min(cnts["water"],40)/40.,min(cnts["harvest"],40)/40.,min(cnts["feed"],30)/30.,
        min(cnts["care"],30)/30.,min(cnts["cfert"],30)/30.,min(cnts["dig"],30)/30.,
        min(cnts["empty"],60)/60.,min(cnts["struct_free"],30)/30.,
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
'''

D=W1.shape[0];H1=W1.shape[1];H2=W2.shape[1];K=W3.shape[1]
model_code = (model_code
    .replace("__LABELS__",repr(labels))
    .replace("__W1__",fmt(W1)).replace("__B1__",fmt(b1))
    .replace("__W2__",fmt(W2)).replace("__B2__",fmt(b2))
    .replace("__W3__",fmt(W3)).replace("__B3__",fmt(b3))
    .replace("__D__",str(D)).replace("__H1__",str(H1))
    .replace("__H2__",str(H2)).replace("__K__",str(K)))

src = src.replace("FEED_BUFFER = 4", model_code + "\nFEED_BUFFER = 4")

# compute masks+counts once per turn, before the unit loop
src = src.replace(
    "    units=[me[\"farmer\"]]+list(me.get(\"hands\") or [])\n    n=len(units); claimed=set()",
    "    units=[me[\"farmer\"]]+list(me.get(\"hands\") or [])\n    n=len(units); claimed=set()\n"
    "    _masks=_masks_of(tiles)\n"
    "    _cnts={k:len(v) for k,v in _masks.items()}")

# replace the nearest-first pick with model-scored pick
old_pick = """            if pool:
                bx,by,bj=min(pool,key=lambda j:_mh(pos,j))
                claimed.add((bx,by,bj))"""
new_pick = """            if pool:
                dists,dshed=_nears(tiles,_masks,px,py)
                v=_feats_of(day,hour,money,me["hires_today"],len(me["unlocked_quadrants"]),
                            shed,inv,ui,px,py,_cnts,dists,dshed,tile)
                z=_fwd(v)
                best=None
                for j in pool:
                    jj=j[2]
                    if jj=="PLANT" and len(j)>3: jj="PLANT:"+j[3]
                    if jj not in _LI: continue
                    sc=z[_LI[jj]]-0.6*_mh(pos,(j[0],j[1]))
                    if best is None or sc>best[0]: best=(sc,j)
                bx,by,bj=(best[1] if best else min(pool,key=lambda j:_mh(pos,j)))
                claimed.add((bx,by,bj))"""
assert old_pick in src, "pick block not found"
src = src.replace(old_pick, new_pick)

out = ROOT+"/moe/r7/build/devin/clone_dsm_bc.py"
open(out,"w").write(src)
print("wrote",out,len(src),"bytes")
