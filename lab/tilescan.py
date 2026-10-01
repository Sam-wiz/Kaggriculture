"""Where does the tape never go, and what is free there?

A micro-farm only avoids the positional coupling that killed every previous production change if it
lives on tiles the base program never references. BUILD_PASTURE costs nothing (it only requires an
empty tile), so the binding questions are: how many tiles stay empty, are any of them adjacent to
each other and reachable, and does any unit ever stand on them.

Reports, over a full episode: the set of tiles occupied by the route at any point, the set any unit
ever stands on, and the tiles that are empty AND never visited -- the candidate plot.
"""
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

AGENT = "bench_frozen/A_router.py"
OPP = "rivals/leoprovorov_kaggriculture-v65/main.py"


def scan(seed, agent=AGENT):
    visited = collections.Counter()
    ever_used = set()
    empty_at = {}
    unlocked = [None]

    def on_step(step, state, env):
        farm = state[0].observation.farms[0]
        for p in [tuple(farm["farmer"])] + [tuple(h) for h in farm["hands"]]:
            visited[p] += 1
        tiles = farm["tiles"]
        empty = set()
        for y, row in enumerate(tiles):
            for x, cell in enumerate(row):
                if cell == "LOCKED":
                    continue
                if cell is None:
                    empty.add((x, y))
                else:
                    ever_used.add((x, y))
        empty_at[step] = empty
        unlocked[0] = list(farm.get("unlocked_quadrants") or [])

    harness.run_episode(agent, OPP, seed=seed, copy_obs=False, on_step=on_step,
                        catch_errors=True)
    return visited, ever_used, empty_at, unlocked[0]


if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 900009
    visited, ever_used, empty_at, quads = scan(seed)
    steps = sorted(empty_at)
    late = [s for s in steps if 150 <= s <= 700]
    always_empty = set.intersection(*[empty_at[s] for s in late]) if late else set()
    never_visited = {p for p in always_empty if visited.get(p, 0) == 0}
    print(f"seed {seed}   unlocked quadrants: {quads}")
    print(f"tiles ever holding something (plant/structure/weed): {len(ever_used)}")
    print(f"tiles empty at EVERY step from 150 on:               {len(always_empty)}")
    print(f"   of those, never stood on by any unit:             {len(never_visited)}")
    print(f"\ncandidate plot (empty all game, never visited): {sorted(never_visited)[:24]}")
    # shed-adjacent tiles matter: PICKUP requires shed adjacency
    print(f"\nvisited-tile heat (top 12): {visited.most_common(12)}")
    ne = sorted(always_empty)
    print(f"\nempty-all-game tiles, sorted: {ne[:30]}")
    if ne:
        rows = collections.Counter(y for _, y in ne)
        print(f"   by row: {dict(sorted(rows.items()))}")
