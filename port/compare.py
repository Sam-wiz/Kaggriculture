"""Action-for-action equivalence check: pure-Python port vs. the C++ reference.

Both agents are driven from the *same* observation at the *same* episode
position: a wrapper agent occupies one seat, hands each side its own deepcopy of
the observation, records both action dicts, and plays the reference's action so
the trajectory is exactly the reference's.

The native reference keeps a per-seat session inside the shared library for the
lifetime of the process, so every episode runs in a fresh subprocess.

Usage:
    ./.venv/bin/python port/compare.py                 # full sweep
    ./.venv/bin/python port/compare.py --one <seed> <seat> <opp> <mode>
"""
from __future__ import annotations

import copy
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)

REF = os.path.join(REPO, "rivals", "yhay81_the-35-0-tape-a-causal-shop-router", "main.py")
PORT = os.path.join(HERE, "main.py")

SEEDS = [1, 2, 3, 7, 42, 123, 2024, 77777]
OPPONENTS = [
    "starter",
    os.path.join(REPO, "rivals", "yhay81_the-35-0-tape-a-causal-shop-router", "main.py"),
    os.path.join(REPO, "rivals", "boatlee_v29-r1-adaptive-market-hysteresis", "main.py"),
    os.path.join(REPO, "rivals", "kaitofukami_238-238-known-streams-v58-minimax-closed-loop", "main.py"),
]


def _load(path, name):
    if not path.endswith(".py"):
        from kaggle_environments.envs.kaggriculture import kaggriculture as K
        return K.agents[path]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    for attr in ("agent", "my_agent", "act"):
        if hasattr(mod, attr):
            return getattr(mod, attr)
    raise ValueError("no agent in %s" % path)


def _force_route1(observation, seat):
    """Rewrite the observation so `choose_observed_tail` fires: the town's first
    three unlocked shops become ICE_CREAM_SHOP / FARMERS_MARKET / FARMERS_MARKET
    and the rival farm holds three goose tiles.  Both agents receive the very
    same rewritten observation, so this only steers which tape they replay."""
    shops = list(observation["town"]["unlocked_shops"])
    observation["town"]["unlocked_shops"] = (
        ["ICE_CREAM_SHOP", "FARMERS_MARKET", "FARMERS_MARKET"] + shops[3:])
    tiles = observation["farms"][1 - seat]["tiles"]
    placed = 0
    for y in range(10):
        for x in range(10):
            if placed >= 3:
                break
            tiles[y][x] = {"kind": "COOP", "animal": "GOOSE", "fed_today": True,
                           "cared_today": False, "fertilizer_available": False,
                           "consecutive_unfed": 0, "yield_units": 1,
                           "pending_care_bonus": 0, "placed_day": 5}
            placed += 1
    return observation


def run_one(seed, seat, opp, mode):
    """mode 'cmp'   -> wrapper (ref plays, port shadowed) vs opponent
       mode 'cmp1'  -> as 'cmp' but the step-216 observation is rewritten so
                       both sides take the route-1 tail (never reached naturally)
       mode 'port'  -> port alone vs opponent (independent bank check)
       mode 'ref'   -> reference alone vs opponent (independent bank check)"""
    import harness

    diffs = []
    n_steps = [0]
    route_flags = {"port_route1": False}

    if mode in ("cmp", "cmp1"):
        ref_fn = _load(REF, "cmp_ref")
        port_fn = _load(PORT, "cmp_port")
        port_mod = sys.modules["cmp_port"]

        def me(observation):
            shared = copy.deepcopy(observation)
            if mode == "cmp1" and int(shared["step"]) == 216:
                shared = _force_route1(shared, seat)
            a = ref_fn(copy.deepcopy(shared))
            b = port_fn(copy.deepcopy(shared))
            n_steps[0] += 1
            if a != b:
                diffs.append({
                    "step": int(observation["step"]),
                    "ref": a,
                    "port": b,
                })
            ctx = port_mod._SESSION_CONTEXT[seat]
            if ctx is not None and ctx.selected_route == 1:
                route_flags["port_route1"] = True
            return a
    elif mode == "port":
        me = _load(PORT, "solo_port")
    else:
        me = _load(REF, "solo_ref")

    opp_fn = opp if not opp.endswith(".py") else _load(opp, "cmp_opp")
    a_side, b_side = (me, opp_fn) if seat == 0 else (opp_fn, me)
    r = harness.run_episode(a_side, b_side, seed=seed, catch_errors=True)
    return {
        "seed": seed, "seat": seat, "opp": opp, "mode": mode,
        "bank": r["reward"][seat], "opp_bank": r["reward"][1 - seat],
        "status": r["status"], "errors": r["errors"],
        "steps_compared": n_steps[0],
        "n_diffs": len(diffs),
        "first_diff": diffs[0] if diffs else None,
        "route1": route_flags["port_route1"],
    }


def _spawn(seed, seat, opp, mode):
    out = subprocess.run(
        [sys.executable, os.path.abspath(__file__), "--one",
         str(seed), str(seat), opp, mode],
        capture_output=True, text=True, cwd=REPO)
    lines = [l for l in out.stdout.splitlines() if l.startswith("RESULT ")]
    if out.returncode != 0 or not lines:
        return {"seed": seed, "seat": seat, "opp": opp, "mode": mode,
                "error": (out.stderr or out.stdout)[-1500:]}
    return json.loads(lines[-1][7:])


def main():
    import concurrent.futures as cf

    modes = ("cmp", "cmp1", "port", "ref")
    jobs = []
    for opp in OPPONENTS:
        if opp.endswith(".py") and not os.path.exists(opp):
            continue
        for seed in SEEDS:
            for seat in (0, 1):
                for mode in modes:
                    jobs.append((seed, seat, opp, mode))

    results = []
    with cf.ThreadPoolExecutor(max_workers=max(1, (os.cpu_count() or 4) - 1)) as ex:
        futs = {ex.submit(_spawn, *j): j for j in jobs}
        for i, f in enumerate(cf.as_completed(futs), 1):
            results.append(f.result())
            print("  [%3d/%3d] done" % (i, len(jobs)), end="\r", flush=True)
    print()

    by = {}
    for r in results:
        by[(r["opp"], r["seed"], r["seat"], r["mode"])] = r

    failures = []
    total_steps = 0
    n_episodes = 0
    route1_hits = []
    print("%-46s %7s %5s %9s %14s %14s %s" %
          ("opponent", "seed", "seat", "steps", "refBank", "portBank", "verdict"))
    for opp in OPPONENTS:
        if opp.endswith(".py") and not os.path.exists(opp):
            continue
        short = os.path.basename(os.path.dirname(opp))[:44] if opp.endswith(".py") else opp
        for seed in SEEDS:
            for seat in (0, 1):
                c = by.get((opp, seed, seat, "cmp"), {})
                c1 = by.get((opp, seed, seat, "cmp1"), {})
                p = by.get((opp, seed, seat, "port"), {})
                q = by.get((opp, seed, seat, "ref"), {})
                if "error" in c or "error" in c1 or "error" in p or "error" in q:
                    failures.append(("crash", opp, seed, seat,
                                     c.get("error") or c1.get("error")
                                     or p.get("error") or q.get("error")))
                    print("%-46s %7d %5d  CRASH" % (short, seed, seat))
                    continue
                ok_actions = c["n_diffs"] == 0 and c1["n_diffs"] == 0
                ok_bank = (p["bank"] == q["bank"] == c["bank"])
                ok_err = (c["errors"] == [None, None] and c1["errors"] == [None, None]
                          and p["errors"] == [None, None])
                total_steps += c["steps_compared"] + c1["steps_compared"]
                n_episodes += 2
                if c.get("route1"):
                    route1_hits.append((short, seed, seat, "natural"))
                if c1.get("route1"):
                    route1_hits.append((short, seed, seat, "forced"))
                verdict = "OK" if (ok_actions and ok_bank and ok_err) else "FAIL"
                if verdict == "FAIL":
                    failures.append(("mismatch", opp, seed, seat,
                                     c.get("first_diff") or c1.get("first_diff"),
                                     q.get("bank"), p.get("bank"), c.get("errors"),
                                     p.get("errors")))
                print("%-46s %7d %5d %9d %14.0f %14.0f %s" %
                      (short, seed, seat, c["steps_compared"], q["bank"], p["bank"], verdict))

    print()
    print("episodes compared : %d" % n_episodes)
    print("steps compared    : %d" % total_steps)
    print("route-1 selections: %d %s" % (len(route1_hits), route1_hits[:6]))
    if failures:
        print("FAILURES: %d" % len(failures))
        for f in failures[:5]:
            print(json.dumps(f, indent=2, default=str)[:4000])
        return 1
    print("ALL IDENTICAL: port == C++ reference, action-for-action, on every step.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--one":
        seed, seat, opp, mode = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
        print("RESULT " + json.dumps(run_one(seed, seat, opp, mode)))
    else:
        sys.exit(main())
