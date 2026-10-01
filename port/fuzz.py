"""Synthetic-observation fuzz: drive the C++ reference and the Python port with
identical, deliberately adversarial observations and compare the action dicts.

Natural episodes never take the step-216 route switch (`choose_observed_tail`
needs the town to unlock ICE_CREAM_SHOP / FARMERS_MARKET / FARMERS_MARKET as its
first three shops *and* the rival to hold >1 goose tile), and they only ever
graze the budget guard's shortfall path.  This fuzz manufactures those states.

Each trial drives ascending steps starting at 0, so the native session-reset rule
(`step == 0 || step < last_step`) fires exactly once per trial, in both agents.

Usage:
    ./.venv/bin/python port/fuzz.py [n_trials_per_process] [n_processes]
    ./.venv/bin/python port/fuzz.py --one <rng_seed> <n_trials>
"""
from __future__ import annotations

import copy
import importlib.util
import json
import os
import random
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)

REF = os.path.join(REPO, "rivals", "yhay81_the-35-0-tape-a-causal-shop-router", "main.py")
PORT = os.path.join(HERE, "main.py")

ITEMS = ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG",
         "MILK", "WOOL", "FERTILIZER", "GOOSE", "COW", "SHEEP")
PRODUCTS = ITEMS[:9]
CROPS = ITEMS[:5]
SHOPS = ("BAKERY", "BRUNCH_SPOT", "FARMERS_MARKET", "ICE_CREAM_SHOP",
         "PET_CAFE", "PIZZA_SHOP", "SMOOTHIE_SHOP", "YARN_STORE")
ANIMALS = ("GOOSE", "COW", "SHEEP")
QUADRANTS = ("NW", "NE", "SW", "SE")
GUARD_STEPS = [0, 72, 144, 216, 288, 360, 432, 504, 576, 648]


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _tiles(rng, n_goose, n_other):
    grid = [[{"kind": "EMPTY"} for _ in range(10)] for _ in range(10)]
    cells = [(x, y) for y in range(10) for x in range(10)]
    rng.shuffle(cells)
    cursor = 0
    for _ in range(n_goose):
        x, y = cells[cursor]
        cursor += 1
        grid[y][x] = {"kind": rng.choice(("COOP", "PASTURE")), "animal": "GOOSE",
                      "fed_today": rng.random() < 0.5, "cared_today": False,
                      "fertilizer_available": rng.random() < 0.3,
                      "consecutive_unfed": 0, "yield_units": rng.randrange(0, 5),
                      "pending_care_bonus": 0, "placed_day": rng.randrange(0, 20)}
    for _ in range(n_other):
        x, y = cells[cursor]
        cursor += 1
        pick = rng.random()
        if pick < 0.4:
            grid[y][x] = {"kind": rng.choice(("COOP", "PASTURE")),
                          "animal": rng.choice(("COW", "SHEEP")),
                          "fed_today": False, "yield_units": 1, "placed_day": 3}
        elif pick < 0.7:
            grid[y][x] = {"kind": "PLANT", "crop": rng.choice(CROPS),
                          "watered_today": True, "consecutive_unwatered": 0,
                          "yield_units": 2, "planted_day": 4,
                          "max_lifespan_step": 400, "fertilized_until_day": -1}
        else:
            grid[y][x] = {"kind": rng.choice(("WEED", "LOCKED", "SOIL"))}
    return grid


def _observation(rng, seat, step, force_route1):
    n_hands = rng.randrange(0, 13)
    if force_route1:
        shops = ["ICE_CREAM_SHOP", "FARMERS_MARKET", "FARMERS_MARKET"]
        shops += [rng.choice(SHOPS) for _ in range(rng.randrange(0, 5))]
        rival_goose = rng.randrange(2, 6)
    else:
        n_shops = rng.randrange(0, 9)
        shops = [rng.choice(SHOPS) for _ in range(n_shops)]
        rival_goose = rng.randrange(0, 3)
    # tight money on purpose: the guard only does anything when it is short.
    money = rng.choice((0.0, float(rng.randrange(0, 3000)),
                        float(rng.randrange(0, 40000)),
                        float(rng.randrange(0, 300000))))
    prices = {name: rng.choice((1, 1, rng.randrange(1, 700))) for name in PRODUCTS}
    shed = {name: rng.choice((0, 0, rng.randrange(0, 101))) for name in ITEMS}
    inventories = [{name: rng.choice((0, 0, rng.randrange(0, 40)))
                    for name in ITEMS} for _ in range(n_hands + 1)]
    if rng.random() < 0.2:                      # short inventories list
        inventories = inventories[:max(0, len(inventories) - rng.randrange(1, 4))]
    mine = {
        "money": money,
        "farmer": [rng.randrange(10), rng.randrange(10)],
        "hands": [[rng.randrange(10), rng.randrange(10)] for _ in range(n_hands)],
        "unlocked_quadrants": list(QUADRANTS[:rng.randrange(1, 5)]),
        "hires_today": rng.randrange(0, 9),
        "tiles": _tiles(rng, rng.randrange(0, 3), rng.randrange(0, 15)),
    }
    rival = {
        "money": float(rng.randrange(0, 100000)),
        "farmer": [0, 0],
        "hands": [[1, 1]] * rng.randrange(0, 6),
        "unlocked_quadrants": list(QUADRANTS[:rng.randrange(1, 5)]),
        "hires_today": rng.randrange(0, 9),
        "tiles": _tiles(rng, rival_goose, rng.randrange(0, 15)),
    }
    farms = [mine, rival] if seat == 0 else [rival, mine]
    return {
        "player": seat,
        "step": step,
        "day": step // 24,
        "hour": step % 24,
        "market": {"prices": prices,
                   "inventory": {n: rng.randrange(0, 20000) for n in PRODUCTS}},
        "town": {"unlocked_shops": shops},
        "farms": farms,
        "private": {
            "shed": shed,
            "seeds": {n: rng.randrange(0, 30) for n in CROPS},
            "inventories": inventories,
        },
        "remainingOverageTime": 60.0,
    }


def run(rng_seed, n_trials):
    ref_mod = _load(REF, "fuzz_ref")
    port_mod = _load(PORT, "fuzz_port")
    rng = random.Random(rng_seed)
    diffs = []
    stats = {"calls": 0, "route1": 0, "guard_changed": 0, "trials": n_trials}
    for _ in range(n_trials):
        seat = rng.randrange(2)
        force = rng.random() < 0.5
        steps = [0, 216] + sorted(rng.sample(GUARD_STEPS[4:], rng.randrange(1, 6)))
        steps += sorted(rng.sample(range(217, 719), 3))
        steps = sorted(set(steps))
        for step in steps:
            obs = _observation(rng, seat, step, force and step == 216)
            a = ref_mod.agent(copy.deepcopy(obs))
            b = port_mod.agent(copy.deepcopy(obs))
            stats["calls"] += 1
            ctx = port_mod._SESSION_CONTEXT[seat]
            if ctx is not None and ctx.selected_route == 1:
                stats["route1"] += 1
            if step % 72 == 0 and step < 719:
                tape = port_mod._TAPES[ctx.selected_route][step]
                if len(a["market"]) != tape[2]:
                    stats["guard_changed"] += 1
            if a != b and len(diffs) < 5:
                diffs.append({"rng_seed": rng_seed, "seat": seat, "step": step,
                              "ref": a, "port": b, "obs_digest": {
                                  "shops": obs["town"]["unlocked_shops"],
                                  "money": obs["farms"][seat]["money"],
                                  "shed": obs["private"]["shed"],
                                  "prices": obs["market"]["prices"]}})
    stats["n_diffs"] = len(diffs)
    stats["diffs"] = diffs
    return stats


def main():
    n_trials = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    n_procs = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    import concurrent.futures as cf

    def spawn(i):
        out = subprocess.run(
            [sys.executable, os.path.abspath(__file__), "--one", str(1000 + i), str(n_trials)],
            capture_output=True, text=True, cwd=REPO)
        lines = [l for l in out.stdout.splitlines() if l.startswith("RESULT ")]
        if out.returncode != 0 or not lines:
            return {"error": (out.stderr or out.stdout)[-1500:]}
        return json.loads(lines[-1][7:])

    with cf.ThreadPoolExecutor(max_workers=n_procs) as ex:
        results = list(ex.map(spawn, range(n_procs)))

    calls = route1 = guard_changed = ndiff = 0
    bad = []
    for r in results:
        if "error" in r:
            print("WORKER CRASH:", r["error"][-800:])
            return 1
        calls += r["calls"]
        route1 += r["route1"]
        guard_changed += r["guard_changed"]
        ndiff += r["n_diffs"]
        bad.extend(r["diffs"])
    print("fuzz calls            : %d" % calls)
    print("calls on route 1      : %d" % route1)
    print("guard-modified orders : %d" % guard_changed)
    print("divergences           : %d" % ndiff)
    if bad:
        print(json.dumps(bad[0], indent=2)[:4000])
        return 1
    print("ALL IDENTICAL under synthetic fuzz.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--one":
        print("RESULT " + json.dumps(run(int(sys.argv[2]), int(sys.argv[3]))))
    else:
        sys.exit(main())
