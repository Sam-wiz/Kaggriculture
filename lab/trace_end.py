import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness
inner = harness.load_agent(sys.argv[1])
opp = sys.argv[2] if len(sys.argv)>2 else "starter"
seed = int(sys.argv[3]) if len(sys.argv)>3 else 1
rec=[]
def wrapped(obs):
    a = inner(obs)
    if obs.get("step",0) >= 712:
        rec.append((obs["step"], obs["hour"], dict(obs["private"]["shed"]),
                    [dict(i) for i in obs["private"]["inventories"]][:3],
                    a.get("market", []), [a.get("farmer")]+list(a.get("hands",[]))[:3]))
    return a
r = harness.run_episode(wrapped, opp, seed=seed, catch_errors=False)
for step,h,shed,invs,mkt,acts in rec:
    shed={k:v for k,v in shed.items() if v}
    print(f"step={step} h={h} shed={shed}")
    print(f"   inv0..2={invs}")
    print(f"   market={mkt}")
    print(f"   acts={acts}")
print("final", r["reward"])
