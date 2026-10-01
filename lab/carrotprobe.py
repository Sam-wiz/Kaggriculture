"""Measure carrot scarcity across seeds under V48 mirror play:
shop draw -> min carrot inventory / max carrot price trajectory."""
import collections
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness


def kload(path):
    src = open(path).read()
    env = {}
    exec(compile(src, path, "exec"), env)  # noqa: S102
    return [v for v in env.values() if callable(v)][-1]


def job(seed):
    v48 = kload("rivals/ahmedberatozer_kaggriculture-v48-clear-the-queue/_entry.py")
    track = {"min_inv": 1e9, "max_px": 0, "pet": 0, "fm": 0}
    def on_step(step, state, env):
        o = state[0].observation
        inv = o["market"]["inventory"]["CARROT"]
        px = o["market"]["prices"]["CARROT"]
        if inv < track["min_inv"]:
            track["min_inv"] = inv
        if px > track["max_px"]:
            track["max_px"] = px
        track["shops"] = collections.Counter(o["town"]["unlocked_shops"])
    r = harness.run_episode(v48, v48, seed=seed, catch_errors=True, on_step=on_step)
    sc = track["shops"]
    return (seed, sc.get("PET_CAFE", 0), sc.get("FARMERS_MARKET", 0),
            track["min_inv"], track["max_px"], r["reward"][0])


if __name__ == "__main__":
    seeds = range(int(sys.argv[1]), int(sys.argv[1]) + int(sys.argv[2]))
    rows = list(ProcessPoolExecutor(7).map(job, seeds))
    rows.sort(key=lambda r: -r[1])
    for seed, pet, fm, mn, mx, bank in rows:
        print("seed %-5d pet=%d fm=%d | min carrot inv=%6.0f max px=%8.0f | bank=%.0f"
              % (seed, pet, fm, mn, mx, bank))
    by_pet = {}
    for _, pet, _, mn, mx, _ in rows:
        by_pet.setdefault(pet, []).append((mn, mx))
    print("\nby pet count:")
    for pet in sorted(by_pet):
        v = by_pet[pet]
        print("  pet=%d n=%d  mean min_inv=%.0f mean max_px=%.0f"
              % (pet, len(v), sum(x[0] for x in v) / len(v), sum(x[1] for x in v) / len(v)))
