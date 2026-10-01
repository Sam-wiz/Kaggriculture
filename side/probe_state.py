"""What does h_over's farm look like mid-season?  Prices, shed, tiles, cash."""
import importlib.util, os, sys
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
import harness

def _load(p,n):
    s=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(s)
    sys.modules[n]=m; s.loader.exec_module(m); return m
H=_load(os.path.join(REPO,"port2","h_over.py"),"hov")
H2=_load(os.path.join(REPO,"port2","h_over.py"),"hov2")

rows=[]
def on_step(step, state, env):
    if (step+1) % 24: return
    obs=state[0].observation
    f=obs.farms[0]; pr=state[0].observation.private
    shed=sum(pr["shed"].values())
    tiles=f["tiles"]; used=0; empty=0; weed=0; locked=0
    for y in range(10):
        for x in range(10):
            t=tiles[y][x]
            if t is None: empty+=1
            elif t=="LOCKED": locked+=1
            elif t["kind"]=="WEED": weed+=1
            else: used+=1
    rows.append(dict(day=step//24, money=int(f["money"]), shed=shed, used=used,
                     empty=empty, weed=weed, locked=locked,
                     quads=len(f["unlocked_quadrants"]),
                     shops=len(obs.town["unlocked_shops"]),
                     prices={k:v for k,v in obs.market["prices"].items()},
                     inv={k:v for k,v in obs.market["inventory"].items()}))

r=harness.run_episode(H.agent, H2.agent, seed=7, on_step=on_step)
print("reward", r["reward"], "errors", r["errors"])
for row in rows:
    p=row.pop("prices"); iv=row.pop("inv")
    print(row)
    print("     prices", {k:p[k] for k in ("WHEAT","CARROT","TOMATO","STRAWBERRY","MELON","EGG","MILK","WOOL","FERTILIZER")})
    print("     inv-I0", {k:iv[k]-10000 for k in ("WHEAT","CARROT","TOMATO","STRAWBERRY","MELON","EGG","MILK","WOOL","FERTILIZER")})
