"""Exact replay re-simulation for Kaggriculture tapes.

Drives the OFFICIAL interpreter (kaggle_environments.envs.kaggriculture) with the
recorded action stream and the recorded seed. Verified alignment (tapefidelity.py):
replay ``steps[t].action`` is the action that PRODUCED ``steps[t].observation`` --
the action the agent submitted at game-step t-1. ``actions[0]`` is the init
placeholder (all-PASS), so the action applied at game-step s is ``actions[s+1]``.

Usage:
    from resim import load_tape, resim, resim_top10
    r = resim_top10("mine/top10/112219779.json.gz")
    r["money"]  -> [p0_final, p1_final]
"""
import gzip
import json
import os
import sys

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.path.insert(0, ROOT)

from kaggle_environments.envs.kaggriculture import kaggriculture as K  # noqa: E402

PASS = {"farmer": ["PASS"], "hands": [], "market": []}

DEFAULT_CONFIG = {
    "episodeSteps": 720,
    "actTimeout": 1,
    "runTimeout": 1200,
    "boardSize": 10,
    "startingMoney": 3000,
    "maxMarketOrdersPerTurn": 10,
    "turnsPerDay": 24,
    "shedCapacity": 100,
    "weedSpawnChance": 0.005,
    "townShopUnlockInterval": 3,
    "townShopSellInterval": 4,
    "townCenterSellInterval": 24,
    "farmHandCostMult": 1,
    "seed": None,
}


class Struct(dict):
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)


def _structify(o):
    if isinstance(o, list):
        return [_structify(v) for v in o]
    if isinstance(o, dict):
        return Struct(**{k: _structify(v) for k, v in o.items()})
    return o


class _Env:
    def __init__(self, configuration):
        self.configuration = _structify(configuration)
        self.done = False
        self.info = {}


class _AgentState:
    __slots__ = ("observation", "action", "status", "reward")

    def __init__(self, observation):
        self.observation = observation
        self.action = None
        self.status = "ACTIVE"
        self.reward = 0.0


def load_tape(path):
    """Load a reduced top10-style tape (actions only)."""
    with gzip.open(path, "rt") as f:
        return json.load(f)


def load_replay(path):
    """Load a full Kaggle replay (rawkeep-style, has steps+observations)."""
    with gzip.open(path, "rt") as f:
        return json.load(f)


def actions_from_replay(x):
    """[s] -> [p0_action, p1_action] from a full replay's steps list."""
    return [[s[0].get("action"), s[1].get("action")] for s in x["steps"]]


def resim(actions, seed, n_steps=None, on_step=None, pre_step=None, shift=1,
          configuration=None, check_first=False):
    """Replay recorded actions through the official interpreter.

    actions: list over replay index k of [action_p0, action_p1]; action applied at
             game-step s is actions[s+shift] (shift=1 for raw steps dumps).
    pre_step(step, state, env) fires after actions are assigned but BEFORE the
             interpreter call -- captures the observation the agents acted on.
    on_step(step, state, env) fires after each interpreter call (post-state).
    Returns dict(money=[p0,p1], status, state, env, first_bad) where first_bad is
    the first step a recorded unit op was un-executable under resim state, if
    check_first.
    """
    cfg = dict(DEFAULT_CONFIG)
    if configuration:
        cfg.update(configuration)
    cfg["seed"] = seed
    env = _Env(cfg)
    n = n_steps or int(cfg["episodeSteps"])

    state = [_AgentState(Struct(player=i, remainingOverageTime=60.0)) for i in range(2)]
    K.interpreter(state, env)
    state[1].observation.farms = state[0].observation.farms
    state[1].observation.market = state[0].observation.market
    state[1].observation.town = state[0].observation.town

    first_bad = None
    for step in range(n):
        obs0 = state[0].observation
        for i in range(2):
            state[i].observation.step = step
            state[i].observation.day = obs0.day
            state[i].observation.hour = obs0.hour
            if i > 0:
                state[i].observation.farms = obs0.farms
                state[i].observation.market = obs0.market
                state[i].observation.town = obs0.town
        for i in range(2):
            k = step + shift
            a = actions[k][i] if 0 <= k < len(actions) else None
            state[i].action = a if isinstance(a, dict) else dict(PASS)
        if check_first and first_bad is None:
            first_bad = find_impossible(state)
        if pre_step is not None:
            pre_step(step, state, env)
        K.interpreter(state, env)
        if on_step is not None:
            on_step(step, state, env)
        if all(s.status != "ACTIVE" for s in state):
            break

    farms = state[0].observation.farms
    return {
        "money": [float(farms[0]["money"]), float(farms[1]["money"])],
        "status": [s.status for s in state],
        "state": state,
        "env": env,
        "first_bad": first_bad,
        "seed_used": env.info.get("seed"),
    }


def resim_top10(path, **kw):
    x = load_tape(path)
    r = resim(x["actions"], x["seed"], **kw)
    r["tape"] = x
    return r


def snapshot(state):
    """Comparable snapshot of post-step state (JSON-able fields only)."""
    o = state[0].observation
    farms = o.farms
    return {
        "money": [farms[0]["money"], farms[1]["money"]],
        "farmer": [list(farms[0]["farmer"]), list(farms[1]["farmer"])],
        "hands": [[list(p) for p in farms[0]["hands"]],
                  [list(p) for p in farms[1]["hands"]]],
        "quads": [sorted(farms[0]["unlocked_quadrants"]),
                  sorted(farms[1]["unlocked_quadrants"])],
        "hires": [farms[0]["hires_today"], farms[1]["hires_today"]],
        "tiles": [farms[0]["tiles"], farms[1]["tiles"]],
        "shed": [dict(state[0].observation.private["shed"]),
                 dict(state[1].observation.private["shed"])],
        "seeds": [dict(state[0].observation.private["seeds"]),
                  dict(state[1].observation.private["seeds"])],
        "invs": [[dict(v) for v in state[0].observation.private["inventories"]],
                 [dict(v) for v in state[1].observation.private["inventories"]]],
        "m_inv": dict(o.market["inventory"]),
        "m_prices": dict(o.market["prices"]),
        "shops": list(o.town["unlocked_shops"]),
    }


def recorded_snapshot(step_entry):
    """Snapshot from a raw replay's steps[t] (post-action observation)."""
    o = step_entry[0].get("observation") or {}
    farms = o.get("farms") or []
    privs = []
    for p in step_entry:
        privs.append((p.get("observation") or {}).get("private") or {})
    if len(farms) < 2:
        return None
    return {
        "money": [farms[0].get("money"), farms[1].get("money")],
        "farmer": [farms[0].get("farmer"), farms[1].get("farmer")],
        "hands": [farms[0].get("hands") or [], farms[1].get("hands") or []],
        "quads": [sorted(farms[0].get("unlocked_quadrants") or []),
                  sorted(farms[1].get("unlocked_quadrants") or [])],
        "hires": [farms[0].get("hires_today"), farms[1].get("hires_today")],
        "tiles": [farms[0].get("tiles"), farms[1].get("tiles")],
        "shed": [dict(privs[0].get("shed") or {}), dict(privs[1].get("shed") or {})],
        "seeds": [dict(privs[0].get("seeds") or {}), dict(privs[1].get("seeds") or {})],
        "invs": [[dict(v) for v in (privs[0].get("inventories") or [])],
                 [dict(v) for v in (privs[1].get("inventories") or [])]],
        "m_inv": dict((o.get("market") or {}).get("inventory") or {}),
        "m_prices": dict((o.get("market") or {}).get("prices") or {}),
        "shops": list((o.get("town") or {}).get("unlocked_shops") or []),
    }


def diff_snap(rec, got):
    """Return list of (field, recorded, replayed) differences, tiles diffed per-cell."""
    out = []
    for k in rec:
        r, g = rec[k], got[k]
        if k == "tiles":
            for pi in range(2):
                rt, gt = r[pi], g[pi]
                if rt is None:
                    continue
                diffs = []
                for y in range(len(rt)):
                    for x in range(len(rt[y])):
                        if rt[y][x] != gt[y][x]:
                            diffs.append(((x, y), rt[y][x], gt[y][x]))
                if diffs:
                    out.append((f"tiles[{pi}]", diffs[:4], f"{len(diffs)} cells differ"))
            continue
        if r != g:
            out.append((k, r, g))
    return out


def find_impossible(state):
    """Check the about-to-be-applied unit ops for obvious impossibility under the
    current resim state. Returns (step, player, unit_idx, op, reason) or None.

    This flags ops that the interpreter will silently no-op -- a divergence hint,
    not proof (live may have had the same no-op if states matched).
    """
    obs0 = state[0].observation
    step = obs0.step
    day = step // 24
    for pi, s in enumerate(state):
        a = s.action if isinstance(s.action, dict) else {}
        farm = obs0.farms[pi]
        priv = s.observation.private
        ops = [a.get("farmer")] + list(a.get("hands") or [])
        for ui, op in enumerate(ops):
            if not isinstance(op, list) or not op:
                continue
            name = op[0]
            if name in ("NORTH", "SOUTH", "EAST", "WEST", "PASS"):
                continue
            pos = farm["farmer"] if ui == 0 else (
                farm["hands"][ui - 1] if ui - 1 < len(farm["hands"]) else None)
            if pos is None:
                return (step, pi, ui, op, "no such unit (hand not hired)")
            x, y = pos
            tile = farm["tiles"][y][x]
            locked = tile == "LOCKED"
            if name == "PLANT":
                crop = op[1] if len(op) > 1 else None
                if locked or tile is not None:
                    return (step, pi, ui, op, "tile occupied/locked")
                if (priv["seeds"].get(crop, 0) or 0) <= 0:
                    return (step, pi, ui, op, "no seeds")
            elif name == "WATER":
                if not (isinstance(tile, dict) and tile.get("kind") == "PLANT" and not tile.get("watered_today")):
                    return (step, pi, ui, op, "no unwatered plant here")
            elif name == "HARVEST":
                if not (isinstance(tile, dict) and (tile.get("yield_units") or 0) > 0):
                    return (step, pi, ui, op, "nothing to harvest")
            elif name == "FEED":
                ok = isinstance(tile, dict) and "animal" in tile and not tile.get("fed_today")
                if not ok:
                    return (step, pi, ui, op, "no unfed animal here")
                inv = priv["inventories"][ui] if ui < len(priv["inventories"]) else {}
                if (inv.get("WHEAT", 0) or 0) <= 0:
                    return (step, pi, ui, op, "no WHEAT in inventory")
            elif name == "PICKUP":
                item = op[1] if len(op) > 1 else None
                if (priv["shed"].get(item, 0) or 0) <= 0:
                    return (step, pi, ui, op, "item not in shed")
            elif name == "CARE":
                if not (isinstance(tile, dict) and "animal" in tile and not tile.get("cared_today")):
                    return (step, pi, ui, op, "no uncared animal here")
            elif name == "COLLECT_FERTILIZER":
                if not (isinstance(tile, dict) and "animal" in tile and tile.get("fertilizer_available")):
                    return (step, pi, ui, op, "no fertilizer available")
    return None
