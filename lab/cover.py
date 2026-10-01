"""Per-day maintenance coverage: how much of the required upkeep actually happens."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

def run(path, opp="starter", seed=1):
    inner = harness.load_agent(path)
    per = collections.defaultdict(lambda: dict(anim=0, fed=0, cared=0, fert_av=0,
                                               plants=0, need_water=0, units=0, turns=0,
                                               FEED=0, CARE=0, COLLECT=0, WATER=0))
    def wrapped(obs):
        a = inner(obs)
        d = obs["day"]; r = per[d]
        me = obs["player"]; farm = obs["farms"][me]
        if obs["hour"] == 23:  # snapshot near end of day: what got done
            for row in farm["tiles"]:
                for t in row:
                    if not isinstance(t, dict): continue
                    if "animal" in t:
                        r["anim"] += 1
                        r["fed"] += 1 if t["fed_today"] else 0
                        r["cared"] += 1 if t["cared_today"] else 0
                        r["fert_av"] += 1 if t["fertilizer_available"] else 0
                    elif t.get("kind") == "PLANT":
                        r["plants"] += 1
                        r["need_water"] += 0 if t["watered_today"] else 1
        acts = [a.get("farmer",["PASS"])] + list(a.get("hands",[]))
        r["units"] += len(acts); r["turns"] += 1
        for op in acts:
            if op and op[0] in ("FEED","CARE","WATER"): r[op[0]] += 1
            elif op and op[0] == "COLLECT_FERTILIZER": r["COLLECT"] += 1
        return a
    res = harness.run_episode(wrapped, opp, seed=seed, catch_errors=False)
    print(f"{path} vs {opp} seed={seed} final={res['reward']}")
    print(f"{'day':>4}{'units':>6}{'anim':>5}{'fed%':>6}{'card%':>6}{'FEED':>5}{'CARE':>5}"
          f"{'COLL':>5}{'fertLeft':>9}{'plants':>7}{'unwat':>6}{'WATER':>6}")
    for d in sorted(per):
        r = per[d]
        if not r["turns"]: continue
        a = max(1, r["anim"])
        print(f"{d:>4}{r['units']/r['turns']:>6.1f}{r['anim']:>5}{100*r['fed']/a:>6.0f}"
              f"{100*r['cared']/a:>6.0f}{r['FEED']:>5}{r['CARE']:>5}{r['COLLECT']:>5}"
              f"{r['fert_av']:>9}{r['plants']:>7}{r['need_water']:>6}{r['WATER']:>6}")

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else "starter",
        int(sys.argv[3]) if len(sys.argv)>3 else 1)
