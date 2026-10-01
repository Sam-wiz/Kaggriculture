# Old (post-action-leaked) weights vs shifted weights, both scored on CAUSAL rows (obs[t-1] -> action[t]).
import json,sys,numpy as np
from collections import defaultdict
sys.argv=[sys.argv[0]]; ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
exec(open(ROOT+"/mine/rawkeep/bc_train2.py").read().split("print(\"loading rows")[0])
exec(open(ROOT+"/moe/r7/build/opus/bc_dispatch_audit.py").read().split("rows=[json")[0].split("w=np.load")[0])
rows=[json.loads(l) for l in open(ROOT+"/moe/r7/build/opus/bc2s_DSM.jsonl")]
eps=sorted(set(r["ep"] for r in rows)); te=[r for r in rows if r["ep"] in set(eps[-5:])]
X=np.array([feats(r) for r in te],np.float32)
MOVES={"NORTH","SOUTH","EAST","WEST"}
def ontile(r):
    on=r["on"]
    if on.get("plant") and not on.get("watered"): return "WATER"
    if on.get("animal") and not on.get("fed"): return "FEED"
    if (on.get("yield") or 0)>0: return "HARVEST"
    if on.get("animal") and on.get("fert_av"): return "COLLECT_FERTILIZER"
    if on.get("animal") and not on.get("cared"): return "CARE"
    if on.get("weed"): return "DIG"
for name in ["mine/rawkeep/bc_weights.npz","moe/r7/build/opus/bc_weights_shift.npz"]:
    w=np.load(ROOT+"/"+name); L=list(w["labels"])
    a=np.maximum(X@w["W1"]+w["b1"],0); a=np.maximum(a@w["W2"]+w["b2"],0); z=a@w["W3"]+w["b3"]
    P=[L[i] for i in z.argmax(1)]; g=defaultdict(lambda:[0,0])
    for r,p in zip(te,P):
        k="move" if r["y"] in MOVES else "work"; g[k][0]+=1; g[k][1]+=p==r["y2"]; g["all"][0]+=1; g["all"][1]+=p==r["y2"]
        if r["y2"] in ("WATER","FEED"): g["y2="+r["y2"]][0]+=1; g["y2="+r["y2"]][1]+=p==r["y2"]
    print(name.split("/")[-1],{k:(v[0],round(v[1]/v[0],3)) for k,v in g.items()})
g=defaultdict(lambda:[0,0])
for r in te:
    if r["y"] in MOVES or r["y"]=="PASS": continue
    p=ontile(r); g["cover"][0]+=1; g["cover"][1]+=p is not None
    if p: g["acc_when_fires"][0]+=1; g["acc_when_fires"][1]+=p==r["y2"]
print("hand on-tile rule, causal work rows:",{k:(v[0],round(v[1]/v[0],3)) for k,v in g.items()})
