# Walker diagnostic: every unit-turn row -> raw action label + per-direction job
# features. Gate (opus): move-row direction accuracy >= max(nearest 53.7%,
# momentum) + 10pp on held-out episodes.
# Label classes: 0=N 1=S 2=E 3=W 4=TILE_OP 5=PASS
import gzip, json, glob, sys
from collections import deque, defaultdict

ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
TEAM=sys.argv[1] if len(sys.argv)>1 else "DSM"
OUT=sys.argv[2] if len(sys.argv)>2 else f"mine/rawkeep/walkrows_{TEAM}.jsonl"
MOVES={"NORTH":0,"SOUTH":1,"EAST":2,"WEST":3}
WORK={"WATER","HARVEST","FEED","CARE","COLLECT_FERTILIZER","DIG","PLANT","FERTILIZE","BUILD_COOP","BUILD_PASTURE","PICKUP","DROP","PLACE"}
CENTERS={(4,4),(5,4),(4,5),(5,5)}
DIRS={"NORTH":(0,-1),"SOUTH":(0,1),"EAST":(1,0),"WEST":(-1,0)}

def jobtiles(tiles,day):
    """(x,y,ty,urg) for every tile with pending work (any type)."""
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
                    if (t.get("fertilized_until_day") or -1) <= day:
                        J.append((x,y,"fert",0))   # fertilizeable: also a job tile
                elif k in ("COOP","PASTURE") and t.get("animal"):
                    cu=t.get("consecutive_unfed") or 0
                    if not t.get("fed_today"): J.append((x,y,"feed",cu))
                    if not t.get("cared_today"): J.append((x,y,"care",0))
                    if (t.get("yield_units") or 0)>0: J.append((x,y,"harvest",0))
            elif t is None:
                J.append((x,y,"empty",0))
    return J

def bfs_all(sx,sy):
    q=deque([(sx,sy,0)]); D={(sx,sy):0}
    while q:
        x,y,d=q.popleft()
        for dx,dy in DIRS.values():
            nx,ny=x+dx,y+dy
            if 0<=nx<10 and 0<=ny<10 and (nx,ny) not in D:
                D[(nx,ny)]=d+1; q.append((nx,ny,d+1))
    return D

def greedy_dir(dx,dy):
    """which single move direction does a greedy step take to (dx,dy)"""
    if abs(dx)>=abs(dy):
        if dx>0: return 2
        if dx<0: return 3
    if dy>0: return 1
    if dy<0: return 0
    return -1

out=open(OUT,"w"); nrows=0; eps=0
for f in sorted(glob.glob(f"{ROOT}/mine/rawkeep/*.json.gz")):
    try: x=json.loads(gzip.open(f).read())
    except Exception: continue
    tn=(x.get("info") or {}).get("TeamNames") or []
    if TEAM not in tn: continue
    pi=tn.index(TEAM); eps+=1; steps=x["steps"]
    nsteps=len(steps); prevlab={}
    for t in range(1,nsteps):
        if pi>=len(steps[t]) or pi>=len(steps[t-1]): break
        obs=steps[t-1][pi].get("observation") or {}
        act=steps[t][pi].get("action") or {}
        if not obs or not act: continue
        me=obs["farms"][pi]; priv=obs.get("private") or {}
        pos=[me["farmer"]]+list(me.get("hands") or [])
        J=jobtiles(me["tiles"],obs["day"])
        ops=[act.get("farmer")]+list(act.get("hands") or [])
        for ui,op in enumerate(ops):
            if ui>=len(pos): continue
            ux,uy=pos[ui]
            Ju=J
            # shed legs are jobs too (opus: 15% of "distant" targets were shed)
            goods=0; wh=0
            inv0=(priv.get("inventories") or [])
            if ui<len(inv0):
                goods=sum(v for k,v in inv0[ui].items() if k not in ("WHEAT","FERTILIZER"))
                wh=inv0[ui].get("WHEAT",0)
            if goods>0 or wh==0:
                Ju=Ju+[(cx,cy,"shed",0) for cx,cy in CENTERS]
            # label
            if isinstance(op,(list,tuple)) and op:
                if op[0] in MOVES: lab=MOVES[op[0]]
                elif op[0] in WORK: lab=4
                else: lab=5
            else: lab=5
            pk=(f,ui)  # prev action of this unit this episode
            prev=prevlab.get(pk,-1); prevlab[pk]=lab
            D=bfs_all(ux,uy)
            # per-direction: mindist over job tiles whose greedy first step = dir
            fdir=[[24.0,0,0.0] for _ in range(4)]  # [mind,njobs,maxurg]
            for jx,jy,jty,urg in Ju:
                d=D.get((jx,jy),99); g=greedy_dir(jx-ux,jy-uy)
                if g<0: continue  # same tile
                fd=fdir[g]
                if d<fd[0]: fd[0]=d
                fd[1]+=1; fd[2]=max(fd[2],urg)
            # set-valued: dir is optimal iff it reduces Manhattan dist to at
            # least one job that is at the global min distance
            md = min((fd[0] for fd in fdir), default=99)
            bestdirs=[]
            if md<99:
                for jx,jy,jty,urg in Ju:
                    if (jx,jy)==(ux,uy): continue
                    if abs(jx-ux)+abs(jy-uy)!=md: continue
                    for di,(dx,dy) in enumerate(((0,-1),(0,1),(1,0),(-1,0))):
                        if abs(jx-(ux+dx))+abs(jy-(uy+dy))<md and di not in bestdirs:
                            bestdirs.append(di)
            inv=(priv.get("inventories") or [])
            uinv=inv[ui] if ui<len(inv) else {}
            dshed=min(abs(ux-cx)+abs(uy-cy) for cx,cy in CENTERS)
            here_work = 1 if any((jx,jy)==(ux,uy) for jx,jy,_,_ in J) else 0
            row={"ep":x["info"]["EpisodeId"],"t":t,"ui":ui,"y":lab,"pv":prev,
                 "best":bestdirs,
                 "f":[fdir[0],fdir[1],fdir[2],fdir[3]],
                 "g":[obs["day"],obs["hour"],dshed,uinv.get("WHEAT",0),
                      uinv.get("FERTILIZER",0),here_work,len(J)]}
            out.write(json.dumps(row)+"\n"); nrows+=1
out.close()
print(f"{TEAM}: {eps} eps, {nrows} unit-turn rows -> {OUT}")
