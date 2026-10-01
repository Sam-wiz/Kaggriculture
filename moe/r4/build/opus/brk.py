"""Diagnose tape breakage: recorded game vs (candidate in seat s) with shops pinned. Tracks the OPPONENT tape's
money, herd, shed per product and failed orders along the game."""
import sys, os, json, gzip
ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0,ROOT); sys.path.insert(0,ROOT+"/moe/r3/build/opus")
from run import load, act, PASS
import kagsim
ep, seat, cand = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
d = json.load(gzip.open(f"mine/top10/{ep}.json.gz","rt")); A = d["actions"]; o = 1-seat
def tape(i,t): x=A[t+1][i]; return x if isinstance(x,dict) else PASS
def herd(ob, i):
    c={}
    for row in ob["farms"][i]["tiles"]:
        for t in row:
            if isinstance(t,dict):
                k=t.get("animal") or (("P_"+t["crop"]) if t.get("kind")=="PLANT" else t.get("kind")); c[k]=c.get(k,0)+1
    return c
fn = None if cand=="REC" else (lambda o_: {"farmer":["PASS"],"hands":[],"market":[]}) if cand=="PASS" else load(cand,"b")[0]
g1 = kagsim.Game(seed=int(d["seed"]), shops=list(d["shops"])); g2 = kagsim.Game(seed=int(d["seed"]), shops=list(d["shops"]))
first=None
for t in range(719):
    ob1=g1.observe(o); ob2=g2.observe(o)
    if t%24==0 or (first is None and ob1["farms"][o]["money"]!=ob2["farms"][o]["money"]):
        h1,h2=herd(ob1,o),herd(ob2,o)
        m1,m2=ob1["farms"][o]["money"],ob2["farms"][o]["money"]
        sh1,sh2=ob1["private"]["shed"],ob2["private"]["shed"]
        dsh={k:(sh1.get(k,0),sh2.get(k,0)) for k in set(sh1)|set(sh2) if sh1.get(k,0)!=sh2.get(k,0)}
        dh={k:(h1.get(k,0),h2.get(k,0)) for k in set(h1)|set(h2) if h1.get(k,0)!=h2.get(k,0)}
        if first is None and m1!=m2: first=t
        if t%24==0 and (m1!=m2 or dh or dsh): print(t//24, "money",m1,m2,m2-m1,"herd",dh,"shed",dsh)
    a2 = act(fn, g2.observe(seat)) if fn else tape(seat,t)
    g1.step(tape(0,t),tape(1,t))
    g2.step(*((a2,tape(o,t)) if seat==0 else (tape(o,t),a2)))
print("first money divergence step", first, "final opp", g1.reward(o), g2.reward(o), g2.reward(o)-g1.reward(o), "| cand", g2.reward(seat), "rec", g1.reward(seat))
