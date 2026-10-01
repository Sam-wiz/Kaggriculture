"""First-two-shop pair per seed (pass agents, kagsim, to step 150). usage: pairs.py out.json seed..."""
import sys, os, json, time
ROOT="/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; sys.path.insert(0, ROOT+"/kaggriculture-cppsim")
import kagsim
P={"farmer":["PASS"],"hands":[],"market":[]}
def pair(seed):
    g=kagsim.Game(seed=int(seed))
    for t in range(150): g.step(P,P)
    return tuple(g.observe(0)["town"]["unlocked_shops"][:2])
if __name__=="__main__":
    t0=time.time(); out={s:pair(s) for s in sys.argv[2:]}
    json.dump(out,open(sys.argv[1],"w")); print(len(out),"seeds",round(time.time()-t0,2),"s")
