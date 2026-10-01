import gzip,json,glob
from collections import Counter
ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
DIR={"NORTH":(0,-1),"SOUTH":(0,1),"EAST":(1,0),"WEST":(-1,0)}
c=Counter(); n=0
for f in sorted(glob.glob(ROOT+"/mine/rawkeep/*.json.gz")):
    x=json.load(gzip.open(f,"rt")); T=x["info"]["TeamNames"]
    if "DSM" not in T: continue
    pi=T.index("DSM"); S=x["steps"]; n+=1
    for t in range(2,len(S)-1):
        a=S[t][pi].get("action") or {}; op=a.get("farmer")
        if not op: continue
        o_prev=S[t-1][pi]["observation"]["farms"][pi]; o_cur=S[t][pi]["observation"]["farms"][pi]
        if op[0] in DIR:
            dx,dy=DIR[op[0]]; p=o_prev["farmer"]; q=o_cur["farmer"]
            c["move: obs[t]==obs[t-1]+dir (action[t] already applied in obs[t])"]+= (q==[p[0]+dx,p[1]+dy])
            nx=S[t+1][pi]["observation"]["farms"][pi]["farmer"]
            c["move: obs[t+1]==obs[t]+dir"]+= (nx==[q[0]+dx,q[1]+dy]); c["moves"]+=1
        if op[0]=="WATER":
            fx,fy=o_cur["farmer"]; tl=o_cur["tiles"][fy][fx]
            c["water: tile at obs[t] already watered"]+= bool(isinstance(tl,dict) and tl.get("watered_today")); c["waters"]+=1
    if n>=3: break
print(n,"eps",dict(c))
print("step0 action:",x["steps"][0][pi].get("action"),"| step1 market:",(x["steps"][1][pi].get("action") or {}).get("market"),"| money obs0/obs1:",x["steps"][0][pi]["observation"]["farms"][pi]["money"],x["steps"][1][pi]["observation"]["farms"][pi]["money"])
