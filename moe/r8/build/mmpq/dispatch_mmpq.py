"""Dispatch probes for MMPQ — same measurements as the DSM decode (HANDOFF 09-29g..j):
  A) % same-tile consecutive work pairs (stay-and-finish)
  B) % move turns that step toward a nearest pending job (set agreement)
  C) per-ui territory: home coords (median xy of work ops) + % work within R4 of home
  D) momentum tie-break rate on equidistant best-dir moves
  E) mission persistence: for each move-run ending in a work op, does the unit
     arrive at the tile that was nearest-job at run start? + run length stats
Also reports work/move/pass mix and per-op totals.
"""
import gzip, json, glob
from collections import Counter, defaultdict, deque
import numpy as np

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
TEAM = "M & M & P & Q"
FILES = ["109508082","109763722","111099760","111414755"]
MOVES = {"NORTH":(0,-1),"SOUTH":(0,1),"EAST":(1,0),"WEST":(-1,0)}
MOVEIDX = {"NORTH":0,"SOUTH":1,"EAST":2,"WEST":3}
WORK = {"WATER","HARVEST","FEED","CARE","COLLECT_FERTILIZER","DIG","PLANT",
        "FERTILIZE","BUILD_COOP","BUILD_PASTURE","PICKUP","DROP","PLACE"}
CENTERS = [(4,4),(5,4),(4,5),(5,5)]

def jobtiles(tiles, day):
    J=[]
    for y,row in enumerate(tiles):
        for x,t in enumerate(row):
            if isinstance(t,dict):
                k=t.get("kind")
                if k=="WEED": J.append((x,y,"dig",0))
                elif k=="PLANT":
                    cu=t.get("consecutive_unwatered") or 0
                    if not t.get("watered_today"): J.append((x,y,"water",cu))
                    if (t.get("yield_units") or 0)>0: J.append((x,y,"harvest",0))
                    if (t.get("fertilized_until_day") or -1) <= day: J.append((x,y,"fert",0))
                elif k in ("COOP","PASTURE") and t.get("animal"):
                    cu=t.get("consecutive_unfed") or 0
                    if not t.get("fed_today"): J.append((x,y,"feed",cu))
                    if not t.get("cared_today"): J.append((x,y,"care",0))
                    if (t.get("yield_units") or 0)>0: J.append((x,y,"harvest",0))
            elif t is None:
                J.append((x,y,"empty",0))
    return J

agg = {
    "work_pairs":0, "same_tile":0,
    "move_rows":0, "nearest_hit":0, "tied_rows":0, "momentum_hit":0,
    "dir_hist":Counter(), "ops":Counter(), "work_gap":Counter(),
    "ui_work_xy":defaultdict(list),   # ui -> [work-op coords]
    "missions":[],                    # (start_xy, end_xy, len, hit_nearest_at_start)
    "nopend_moves":0,
}

for fid in FILES:
    x = json.loads(gzip.open(f"{ROOT}/mine/rawkeep/{fid}.json.gz").read())
    pi = x["info"]["TeamNames"].index(TEAM)
    steps = x["steps"]
    # per-unit (pos[t], op[t], day[t]) aligned on post-action obs
    seq = []   # t -> (obs, units, ops)
    for t,s in enumerate(steps):
        if pi>=len(s): break
        obs=s[pi].get("observation") or {}; act=s[pi].get("action") or {}
        if not obs: continue
        me=obs["farms"][pi]
        units=[me["farmer"]]+list(me.get("hands") or [])
        ops=[act.get("farmer")]+list(act.get("hands") or [])
        seq.append((obs,units,ops))
    # per unit trajectories
    maxu=max(len(u) for _,u,_ in seq)
    for ui in range(maxu):
        prev_work_xy=None; prev_dir=None; run=None
        prev_pos=None; prev_Ju=None; prev_day=0
        for t,(obs,units,ops) in enumerate(seq):
            if ui>=len(units) or ui>=len(ops): continue
            pos=units[ui]; op=ops[ui]
            if not isinstance(pos,(list,tuple)) or not isinstance(op,(list,tuple)) or not op:
                continue
            ux,uy=int(pos[0]),int(pos[1]); k=op[0]   # pos is POST-action[t]
            if obs["hour"]==0:  # day boundary: hands dismissed/respawned
                prev_pos=None; run=None; prev_dir=None; prev_work_xy=None
            agg["ops"][k]+=1
            if k in MOVES:
                agg["dir_hist"][k]+=1
                # move at t started from prev_pos; decided on prev obs tiles
                ox,oy = prev_pos if prev_pos is not None else (ux,uy)
                Ju = prev_Ju or []
                dists=[(abs(jx-ox)+abs(jy-oy),jx,jy) for jx,jy,_,_ in Ju if (jx,jy)!=(ox,oy)]
                if dists:
                    md=min(d for d,_,_ in dists)
                    bestdirs=set()
                    for d,jx,jy in dists:
                        if d!=md: continue
                        for di,(ddx,ddy) in enumerate(((0,-1),(0,1),(1,0),(-1,0))):
                            if abs(jx-(ox+ddx))+abs(jy-(oy+ddy))<md: bestdirs.add(di)
                    agg["move_rows"]+=1
                    if MOVEIDX[k] in bestdirs: agg["nearest_hit"]+=1
                    if len(bestdirs)>1:
                        agg["tied_rows"]+=1
                        if prev_dir is not None and MOVEIDX[k]==prev_dir:
                            agg["momentum_hit"]+=1
                else: agg["nopend_moves"]+=1
                # mission bookkeeping: extend run
                if run is None:
                    run={"start":(ox,oy),"len":0,
                         "start_md":(min(d for d,_,_ in dists) if dists else None),
                         "start_jobs":[(jx,jy) for d,jx,jy in dists if dists and d==min(dd for dd,_,_ in dists)]}
                run["len"]+=1; run["last"]=(ux,uy)
                prev_dir=MOVEIDX[k]
            elif k in WORK:
                if prev_work_xy is not None:
                    agg["work_pairs"]+=1
                    d01=abs(ux-prev_work_xy[0])+abs(uy-prev_work_xy[1])
                    agg["work_gap"][d01]+=1
                    if d01==0: agg["same_tile"]+=1
                prev_work_xy=(ux,uy)
                agg["ui_work_xy"][ui].append((ux,uy))
                if run is not None:
                    hit=(ux,uy) in run.get("start_jobs",[])
                    agg["missions"].append((run["len"],hit,run.get("start_md")))
                    run=None
                prev_dir=None
            else:  # PASS (keep prev_work_xy: PASS doesn't break a chain probe)
                if run is not None:
                    agg["missions"].append((run["len"],False,run.get("start_md")))
                    run=None
                prev_dir=None
            # stash post-action state = pre-state for act[t+1]
            prev_pos=(ux,uy)
            J=jobtiles(obs["farms"][pi]["tiles"],obs["day"])
            inv=((obs.get("private") or {}).get("inventories") or [])
            if ui<len(inv) and isinstance(inv[ui],dict):
                inv0=inv[ui]
                goods=sum(v for kk,v in inv0.items() if kk not in ("WHEAT","FERTILIZER"))
                wh=inv0.get("WHEAT",0)
                if goods>0 or wh==0: J=J+[(cx,cy,"shed",0) for cx,cy in CENTERS]
            prev_Ju=J; prev_day=obs["day"]

W=agg["work_pairs"]; S=agg["same_tile"]
gaps=sorted(agg["work_gap"].items())
print(f"A) consec work-work pairs: {W}, same-tile {S} = {100*S/max(W,1):.1f}%  (DSM 51.7%)")
print("   tile-gap histogram (top):",gaps[:8])
M=agg["move_rows"]; H=agg["nearest_hit"]
print(f"B) move rows {M}, toward-nearest {H} = {100*H/max(M,1):.1f}%  (DSM 91.9%) | no-pending moves {agg['nopend_moves']}")
T=agg["tied_rows"]; MH=agg["momentum_hit"]
print(f"D) equidistant-tie rows {T}, momentum(=prev dir) {MH} = {100*MH/max(T,1):.1f}%  (DSM 60.6%)")
print("   dir histogram:",dict(agg["dir_hist"]))
print("C) territory map (per-ui median work xy; % work within R4):")
for ui in sorted(agg["ui_work_xy"]):
    pts=np.array(agg["ui_work_xy"][ui])
    if len(pts)<5: continue
    home=np.median(pts,axis=0)
    r4=np.mean(np.abs(pts-home).sum(1)<=4)
    print(f"   ui{ui}: n={len(pts)} home=({home[0]:.0f},{home[1]:.0f}) R4={100*r4:.0f}%")
ml=[m[0] for m in agg["missions"]]; hits=[m[1] for m in agg["missions"]]
print(f"E) missions ending in work: {len(ml)}, len median {np.median(ml):.0f} mean {np.mean(ml):.1f}")
print(f"   arrived at a start-of-mission nearest job tile: {100*np.mean(hits):.1f}%")
print("   ops mix:",dict(agg["ops"]))
