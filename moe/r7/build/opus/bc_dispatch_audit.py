# Audit: where does BC's 74% come from? Split held-out rows into on-tile work vs travel (move) rows;
# compare MLP vs trivial rules; test whether DSM walks toward the NEAREST instance of its job.
import json, sys, numpy as np
from collections import Counter, defaultdict
sys.argv=[sys.argv[0]]
ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
src=open(ROOT+"/mine/rawkeep/bc_train2.py").read()
exec(src.split("print(\"loading rows")[0])  # feats(), MK
w=np.load(ROOT+"/mine/rawkeep/bc_weights.npz")
labels=list(w["labels"]); li={c:i for i,c in enumerate(labels)}
rows=[json.loads(l) for l in open(ROOT+"/mine/rawkeep/bc2_DSM.jsonl")]
eps=sorted(set(r["ep"] for r in rows)); te=[r for r in rows if r["ep"] in set(eps[-5:])]
X=np.array([feats(r) for r in te],np.float32)
a=np.maximum(X@w["W1"]+w["b1"],0); a=np.maximum(a@w["W2"]+w["b2"],0); z=a@w["W3"]+w["b3"]
pred=[labels[i] for i in z.argmax(1)]
MOVES={"NORTH","SOUTH","EAST","WEST"}
JOB2K={"WATER":"water","HARVEST":"harvest","FEED":"feed","CARE":"care","COLLECT_FERTILIZER":"cfert","DIG":"dig"}
def ontile_rule(r):
    on=r["on"]
    if on.get("plant") and not on.get("watered"): return "WATER"
    if on.get("animal") and not on.get("fed"): return "FEED"
    if (on.get("yield") or 0)>0: return "HARVEST"
    if on.get("animal") and on.get("fert_av"): return "COLLECT_FERTILIZER"
    if on.get("animal") and not on.get("cared"): return "CARE"
    if on.get("weed"): return "DIG"
    return None
def nearest_rule(r):
    ks=[(r["d"][k][0],j) for j,k in JOB2K.items() if r["d"][k][0]<99]
    return min(ks)[1] if ks else "PASS"
grp=defaultdict(lambda:[0,0,0,0])
for r,p in zip(te,pred):
    g="move" if r["y"] in MOVES else ("pass" if r["y"]=="PASS" else "work")
    s=grp[g]; s[0]+=1; s[1]+=(p==r["y2"])
    if g=="work": s[2]+=(ontile_rule(r)==r["y2"])
    if g=="move": s[2]+=(nearest_rule(r)==r["y2"])
print("group n mlp_acc rule_acc")
for g,s in grp.items(): print(g,s[0],round(s[1]/s[0],3),round(s[2]/max(1,s[0]),3))
# nearest-instance test: for move rows whose job J is a BFS kind, does the unit's distance to nearest J
# drop by 1 next turn (walking to the nearest J) — and how many turns until it performs J?
idx={(r["ep"],r["t"],r["ui"]):r for r in te}
DIR={"NORTH":(0,-1),"SOUTH":(0,1),"EAST":(1,0),"WEST":(-1,0)}
c=Counter()
for r in te:
    if r["y"] not in MOVES or r["y2"] not in JOB2K: continue
    k=JOB2K[r["y2"]]; d0=r["d"][k][0]
    if d0>=99: c["no_target"]+=1; continue
    n=idx.get((r["ep"],r["t"]+1,r["ui"]))
    if not n: continue
    d1=n["d"][k][0]
    c["toward_nearest" if d1==d0-1 else ("reached/other" if d1<d0 else "away_from_nearest")]+=1
    if d0==0: c["d0_already_on_job_tile"]+=1
tot=sum(v for k,v in c.items() if k in("toward_nearest","reached/other","away_from_nearest"))
print(dict(c), "away frac", round(c["away_from_nearest"]/max(1,tot),3))
# travel share: per unit, fraction of turns spent moving; and label share
print("label share held-out:",Counter("move" if r["y"] in MOVES else r["y"] for r in te).most_common(8))
