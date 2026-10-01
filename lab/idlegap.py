"""How much unit-time does our live agent waste, and what do the top-10 do with theirs?

Devin's 09-18c profiling found the sharpest structural split between the public monoculture and the
private leaders: every public agent runs the same farm plan with ~540 PASS turns, while the top-10
schedulers idle **zero** units. nathanjacob's "pipe16-idle-workers" -- our current base -- is named
for attacking exactly this, so the question is how much is left.

An idle unit-turn is not automatically wasted: a unit may be walking, or standing where it will be
needed. This counts the honest categories separately:

  PASS        explicitly nothing
  MOVE        repositioning (useful or not)
  productive  PLANT/WATER/HARVEST/FEED/CARE/PICKUP/PLACE/DIG/BUILD/COLLECT/FERTILIZE/DROP

and compares our live agent against a real top-10 episode replayed from its own recording.
"""
import collections
import glob
import gzip
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

MOVES = {"NORTH", "SOUTH", "EAST", "WEST"}
OPP = "rivals/thomastschinkel_the-metav4-farm-submission-v13/main.py"


def profile_agent(path, seeds):
    tot = collections.Counter()
    unit_turns = 0
    for seed in seeds:
        def on_step(step, state, env):
            nonlocal unit_turns
            a = state[0].action or {}
            for u in [a.get("farmer")] + list(a.get("hands") or []):
                if not u:
                    continue
                unit_turns += 1
                op = u[0] if isinstance(u, list) else str(u)
                if op == "PASS":
                    tot["PASS"] += 1
                elif op in MOVES:
                    tot["MOVE"] += 1
                else:
                    tot["productive"] += 1
                    tot["op:" + op] += 1
        harness.run_episode(path, OPP, seed=seed, copy_obs=False, on_step=on_step,
                            catch_errors=True)
    return tot, unit_turns


def profile_recorded(limit=6):
    """Same counts, taken from real top-10 episodes as recorded (winner's seat)."""
    tot = collections.Counter()
    unit_turns = 0
    n = 0
    for p in sorted(glob.glob("data/tapes/tapes_*.jsonl.gz")):
        for line in gzip.open(p, "rt"):
            r = json.loads(line)
            for a in r["tape"]:
                if not isinstance(a, dict):
                    continue
                for u in [a.get("farmer")] + list(a.get("hands") or []):
                    if not u:
                        continue
                    unit_turns += 1
                    op = u[0] if isinstance(u, list) else str(u)
                    if op == "PASS":
                        tot["PASS"] += 1
                    elif op in MOVES:
                        tot["MOVE"] += 1
                    else:
                        tot["productive"] += 1
            n += 1
            if n >= limit:
                return tot, unit_turns, n
    return tot, unit_turns, n


def show(label, tot, unit_turns, games):
    if not unit_turns:
        print(f"{label:<28} no data")
        return
    p = tot["PASS"] / unit_turns
    m = tot["MOVE"] / unit_turns
    w = tot["productive"] / unit_turns
    print(f"{label:<28}{unit_turns/games:>12,.0f}{p:>10.1%}{m:>9.1%}{w:>12.1%}")


if __name__ == "__main__":
    idx = json.load(open("data/seedindex_900000_1400.json"))
    seeds = [r["seed"] for r in idx][400:406]
    print(f"{'agent':<28}{'unit-turns/gm':>12}{'PASS':>10}{'MOVE':>9}{'productive':>12}")
    for lab, path in (("pipe16 (our live base)", "subK_pipe16.py"),
                      ("metav4-v13", "subL_metav4.py"),
                      ("subJ_2945 (previous)", "subJ_2945.py")):
        if os.path.exists(path):
            tot, ut = profile_agent(path, seeds)
            show(lab, tot, ut, len(seeds))
    tot, ut, n = profile_recorded(6)
    show(f"TOP-10 recorded (n={n})", tot, ut, max(1, n))
    print("\nproductive-op mix for pipe16:")
    tot, ut = profile_agent("subK_pipe16.py", seeds[:3])
    for k, v in sorted(((k, v) for k, v in tot.items() if k.startswith("op:")),
                       key=lambda kv: -kv[1]):
        print(f"   {k[3:]:<22}{v/3:>8,.0f} per game")
