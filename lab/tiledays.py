"""Where the binding resource -- tile-days -- actually goes, and what each yields."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

def run(me, opp="pass", seed=1):
    td = collections.Counter()
    byday = collections.defaultdict(collections.Counter)
    def on_step(step, state, env):
        if step % 24 != 12:
            return
        obs0 = state[0].observation
        band = "d0-9" if obs0.day < 10 else ("d10-19" if obs0.day < 20 else
               ("d20-25" if obs0.day < 26 else "d26-29"))
        for row in obs0.farms[0]["tiles"]:
            for t in row:
                if t is None: k = "EMPTY"
                elif t == "LOCKED": k = "LOCKED"
                elif t["kind"] == "WEED": k = "WEED"
                elif t["kind"] == "PLANT": k = t["crop"]
                elif "animal" in t: k = t["animal"]
                else: k = "DEAD_STRUCT"
                td[k] += 1
                if k in ("EMPTY", "WEED", "DEAD_STRUCT", "LOCKED"):
                    byday[band][k] += 1
    r = harness.run_episode(me, opp, seed=seed, on_step=on_step, catch_errors=False)
    owned = sum(v for k, v in td.items() if k != "LOCKED")
    print(f"{me} vs {opp} seed={seed}  bank={r['reward'][0]:.0f}")
    print(f"owned tile-days: {owned}   (locked {td['LOCKED']})")
    waste = 0
    for k, v in td.most_common():
        if k == "LOCKED": continue
        flag = ""
        if k in ("EMPTY", "WEED", "DEAD_STRUCT"):
            waste += v; flag = "   <-- unproductive"
        print(f"   {k:<12}{v:>6}  {100*v/owned:>5.1f}%{flag}")
    print(f"   WASTED      {waste:>6}  {100*waste/owned:>5.1f}%")
    print(f"   revenue per productive tile-day: ${r['reward'][0]/max(1,owned-waste):,.1f}")
    print("   waste by phase:")
    for band in ("d0-9", "d10-19", "d20-25", "d26-29"):
        c = byday[band]
        print(f"     {band:<8} EMPTY {c['EMPTY']:>4}  WEED {c['WEED']:>4}  "
              f"DEAD_STRUCT {c['DEAD_STRUCT']:>4}  LOCKED {c['LOCKED']:>4}")

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else "pass",
        int(sys.argv[3]) if len(sys.argv)>3 else 1)
