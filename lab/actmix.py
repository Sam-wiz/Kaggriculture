"""Count what the agent's units actually spend their turns on."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

def run(path, opp="starter", seed=1, phases=((0,10),(10,20),(20,30))):
    inner = harness.load_agent(path)
    counts = [collections.Counter() for _ in phases]
    mkt = [collections.Counter() for _ in phases]
    units = [0]*len(phases)
    def wrapped(obs):
        a = inner(obs)
        d = obs["day"]
        for i,(lo,hi) in enumerate(phases):
            if lo <= d < hi:
                acts = [a.get("farmer",["PASS"])] + list(a.get("hands",[]))
                units[i] += len(acts)
                for op in acts:
                    counts[i][(op[0]+":"+str(op[1])) if (op and op[0] in ("PICKUP","PLANT","PLACE")) else (op[0] if op else "NONE")] += 1
                for o in a.get("market",[]):
                    mkt[i][o[0] + (":"+str(o[1]) if len(o)>1 else "")] += 1
        return a
    r = harness.run_episode(wrapped, opp, seed=seed, catch_errors=False)
    print(f"{path} vs {opp} seed={seed}  final={r['reward']}")
    for i,(lo,hi) in enumerate(phases):
        tot = sum(counts[i].values()) or 1
        print(f"\n-- days {lo}-{hi}: {tot} unit-actions ({units[i]/max(1,(hi-lo)*24):.1f} units/turn avg)")
        for k,v in counts[i].most_common():
            print(f"     {k:<20}{v:>6} {100*v/tot:>5.1f}%")
        print("   market:", dict(mkt[i].most_common(14)))

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else "starter",
        int(sys.argv[3]) if len(sys.argv)>3 else 1)
