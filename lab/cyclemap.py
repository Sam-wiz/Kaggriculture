"""Precompute which PLANT actions sit on SHORT cycles.

The tape recycles wheat every 2-4 days, but wheat only reaches its full 6 units on day 4; carrot
reaches its full 4 units on day 3 and sells for more. So a wheat planting that the tape harvests in
<=3 days is being sold short, and carrot would fit that slot better.

Actions are unit-indexed, so simulate once to learn which tile each unit is standing on, then link
each PLANT to the next HARVEST on that same tile. Emits the (step, unit) list to convert.
"""
import sys, json, collections
sys.path.insert(0, ".")
from harness import load_agent, run_episode

def cycle_map(agent_path="port3/newtape_impact.py", seed=50000):
    base = load_agent(agent_path)
    tile_ops = collections.defaultdict(list)
    def probe(obs, cfg=None):
        a = base(obs)
        step = int(obs.get("step") or 0)
        farm = obs["farms"][obs["player"]]
        units = [tuple(farm["farmer"])] + [tuple(h) for h in (farm.get("hands") or [])]
        acts = [a.get("farmer", ["PASS"])] + list(a.get("hands") or [])
        for u, (pos, act) in enumerate(zip(units, acts)):
            if act and act[0] in ("PLANT", "HARVEST"):
                tile_ops[pos].append((step, u, act[0], act[1] if len(act) > 1 else None))
        return a
    run_episode(probe, load_agent(agent_path), seed=seed)
    out = []
    for pos, ops in tile_ops.items():
        ops.sort()
        for i, o in enumerate(ops):
            if o[2] != "PLANT" or o[3] != "WHEAT":
                continue
            nxt = next((x for x in ops[i+1:] if x[2] == "HARVEST"), None)
            if not nxt:
                continue
            days = (nxt[0] - o[0]) / 24.0
            out.append(dict(step=o[0], unit=o[1], days=round(days, 2),
                            harvest_step=nxt[0], tile=list(pos)))
    return out

if __name__ == "__main__":
    m = cycle_map()
    short = [c for c in m if c["days"] <= 3.0]
    print(f"{len(m)} wheat cycles; {len(short)} are <= 3.0 days (carrot's full-yield point)")
    hist = collections.Counter(int(c["days"]) for c in m)
    print("cycle-length histogram:", dict(sorted(hist.items())))
    json.dump(m, open("cycle_map.json", "w"))
    print("wrote cycle_map.json")
    for c in short[:5]:
        print(f"   PLANT step {c['step']:>3} unit {c['unit']:>2} tile {c['tile']} "
              f"-> HARVEST {c['harvest_step']:>3}  ({c['days']} days)")
