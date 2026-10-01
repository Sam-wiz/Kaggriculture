import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness
inner = harness.load_agent(sys.argv[1])
opp = sys.argv[2]; seed = int(sys.argv[3])
def wrapped(obs):
    a = inner(obs)
    d, h = obs["day"], obs["hour"]
    if 17 <= d <= 22 and h == 6:
        shed = obs["private"]["shed"]
        carried = {}
        for iv in obs["private"]["inventories"]:
            for k,v in iv.items(): carried[k]=carried.get(k,0)+v
        anim = sum(1 for row in obs["farms"][obs["player"]]["tiles"] for t in row
                   if isinstance(t,dict) and "animal" in t)
        print(f"d{d} h{h} money={obs['farms'][obs['player']]['money']:.0f} animals={anim} "
              f"shedTotal={sum(shed.values())} shedWheat={shed.get('WHEAT',0)} "
              f"carriedWheat={carried.get('WHEAT',0)} shed={ {k:v for k,v in shed.items() if v} }")
        print(f"    orders={a.get('market')}")
    return a
r = harness.run_episode(wrapped, opp, seed=seed, catch_errors=False)
print("final", r["reward"])
