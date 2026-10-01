"""Exact units-per-planting by crop, plus animal-days and product per animal-day."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

def run(path, opp="pass", seed=1):
    inner = harness.load_agent(path)
    plants = collections.Counter()
    prev = {}
    got = collections.Counter()
    animal_days = collections.Counter()
    def wrapped(obs):
        a = inner(obs)
        for op in [a.get("farmer",["PASS"])] + list(a.get("hands",[])):
            if op and op[0] == "PLANT" and len(op) > 1:
                plants[op[1]] += 1
        if obs["hour"] == 12:
            for row in obs["farms"][obs["player"]]["tiles"]:
                for t in row:
                    if isinstance(t, dict) and "animal" in t:
                        animal_days[t["animal"]] += 1
        return a
    def on_step(step, state, env):
        priv = state[0].observation.private
        cur = collections.Counter()
        for iv in priv["inventories"]:
            for k, v in iv.items(): cur[k] += v
        for k, v in priv["shed"].items(): cur[k] += v
        for k, v in cur.items():
            d = v - prev.get(k, 0)
            if d > 0: got[k] += d
        prev.clear(); prev.update(cur)
    r = harness.run_episode(wrapped, opp, seed=seed, on_step=on_step, catch_errors=False)
    print(f"{path}  bank={r['reward'][0]:.0f}")
    print("  PLANTED:", dict(plants))
    print("  ANIMAL-DAYS:", dict(animal_days))
    print("  HARVESTED:", {k: v for k, v in got.most_common() if k not in ("COW","SHEEP","GOOSE")})
    for c, n in plants.items():
        if n: print(f"    {c:<11} {got[c]/n:>5.2f} units/planting  ({n} plantings, {got[c]} units)")
    for a, prod in (("COW","MILK"), ("SHEEP","WOOL"), ("GOOSE","EGG")):
        if animal_days[a]:
            print(f"    {a:<11} {got[prod]/animal_days[a]:>5.2f} {prod}/animal-day  ({animal_days[a]} animal-days)")
    tot_ad = sum(animal_days.values())
    if tot_ad: print(f"    FERTILIZER  {got['FERTILIZER']/tot_ad:>5.2f} per animal-day ({tot_ad} animal-days)")

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else "pass",
        int(sys.argv[3]) if len(sys.argv)>3 else 1)
