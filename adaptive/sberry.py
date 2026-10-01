"""Audit every ongoing-crop production event: was the plant watered? fertilized?

The engine grants +2 instead of +1 only when `was_watered AND
fertilized_until_day >= current_day` on the production day, so this pins down
exactly which of the two conditions we are failing.
"""
import collections
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness  # noqa: E402
from kaggle_environments.envs.kaggriculture import kaggriculture as K  # noqa: E402

CROPS = K.CROPS


def run(path, opp="pass", seed=1, params=None):
    if path in K.agents:
        fn = K.agents[path]
    else:
        spec = importlib.util.spec_from_file_location("sbmod", path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules["sbmod"] = mod
        spec.loader.exec_module(mod)
        if params:
            mod.P.update(params)
        fn = mod.agent

    stat = collections.defaultdict(lambda: collections.Counter())

    def on_step(step, state, env):
        pass

    # hook the daily refresh to inspect each production event before it applies
    orig = K._daily_refresh_plants
    farms_of_interest = {}

    def patched(farm, current_day, turns_per_day):
        if id(farm) in farms_of_interest:
            for row in farm["tiles"]:
                for t in row:
                    if not isinstance(t, dict) or t.get("kind") != "PLANT":
                        continue
                    cd = CROPS[t["crop"]]
                    if not cd["ongoing"]:
                        continue
                    dsf = (current_day + 1) - t["planted_day"] - cd["first_yield_day"]
                    if dsf < 0 or dsf % cd["interval"]:
                        continue
                    if dsf // cd["interval"] + 1 > cd["max_yield"]:
                        continue
                    s = stat[t["crop"]]
                    s["events"] += 1
                    w = bool(t["watered_today"])
                    f = t.get("fertilized_until_day", -1) >= current_day
                    s["watered"] += w
                    s["fertilized"] += f
                    s["BOTH(+2)"] += (w and f)
        return orig(farm, current_day, turns_per_day)

    K._daily_refresh_plants = patched

    def wrapped(obs):
        return fn(obs)

    def hook(step, state, env):
        if not farms_of_interest:
            farms_of_interest[id(state[0].observation.farms[0])] = 0

    try:
        # register farm 0 before the first end-of-day
        r = harness.run_episode(wrapped, opp, seed=seed, on_step=hook, catch_errors=False)
    finally:
        K._daily_refresh_plants = orig
    print("%s vs %s seed=%d bank=%.0f" % (path, opp, seed, r["reward"][0]))
    for crop, s in stat.items():
        e = s["events"]
        print("  %-11s production events=%d  watered=%d (%.0f%%)  fertilized=%d (%.0f%%)"
              "  BOTH(+2)=%d (%.0f%%)"
              % (crop, e, s["watered"], 100.0 * s["watered"] / max(1, e),
                 s["fertilized"], 100.0 * s["fertilized"] / max(1, e),
                 s["BOTH(+2)"], 100.0 * s["BOTH(+2)"] / max(1, e)))


if __name__ == "__main__":
    import json
    run(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "pass",
        int(sys.argv[3]) if len(sys.argv) > 3 else 1,
        json.loads(sys.argv[4]) if len(sys.argv) > 4 else None)
