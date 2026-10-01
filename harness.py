"""Fast local harness for Kaggriculture.

Drives the OFFICIAL interpreter from kaggle_environments (no reimplementation, so
no divergence risk) but skips the per-step schema validation / structify /
deepcopy that makes env.run slow. Verified against env.run in tests/test_harness.py.
"""

import copy
import importlib.util
import random
import sys

from kaggle_environments.envs.kaggriculture import kaggriculture as K


class Struct(dict):
    """dict with attribute access, matching kaggle_environments.utils.Struct."""

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __hash__(self):
        return hash(tuple(sorted(self.items())))


def _structify(o):
    if isinstance(o, list):
        return [_structify(v) for v in o]
    if isinstance(o, dict):
        return Struct(**{k: _structify(v) for k, v in o.items()})
    return o


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


def load_agent(spec, name=None):
    """Accept a callable, a path to a .py file with an `agent` function, or a
    built-in name ('pass' / 'random' / 'starter')."""
    if callable(spec):
        return spec
    if isinstance(spec, str) and spec in K.agents:
        return K.agents[spec]
    if isinstance(spec, str) and spec.endswith(".py"):
        mod_name = name or ("agentmod_%d" % abs(hash(spec)))
        spec_obj = importlib.util.spec_from_file_location(mod_name, spec)
        mod = importlib.util.module_from_spec(spec_obj)
        sys.modules[mod_name] = mod
        spec_obj.loader.exec_module(mod)
        for attr in ("agent", "my_agent", "act"):
            if hasattr(mod, attr):
                return getattr(mod, attr)
        raise ValueError("no agent function found in %s" % spec)
    raise ValueError("cannot load agent %r" % (spec,))


def run_episode(agent_a, agent_b, seed=None, configuration=None, copy_obs=True,
                on_step=None, catch_errors=True):
    """Run one full episode. Returns dict with rewards, status, and stats.

    copy_obs=True deep-copies each agent's observation before handing it over
    (matches the real env, where agents cannot mutate shared state). Set False
    only for trusted agents that never mutate the observation -- it is ~2x faster.
    """
    cfg = dict(DEFAULT_CONFIG)
    if configuration:
        cfg.update(configuration)
    if seed is not None:
        cfg["seed"] = seed
    env = _Env(cfg)

    agents = [load_agent(agent_a, "agent_a"), load_agent(agent_b, "agent_b")]

    state = [_AgentState(Struct(player=i, remainingOverageTime=60.0)) for i in range(2)]
    K.interpreter(state, env)  # initializes shared observation on state[0]
    for i in range(1, 2):
        state[i].observation.farms = state[0].observation.farms
        state[i].observation.market = state[0].observation.market
        state[i].observation.town = state[0].observation.town

    n_steps = int(cfg["episodeSteps"])
    errors = [None, None]
    for step in range(n_steps):
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
            if state[i].status != "ACTIVE":
                state[i].action = {"farmer": ["PASS"], "hands": [], "market": []}
                continue
            obs = copy.deepcopy(state[i].observation) if copy_obs else state[i].observation
            if catch_errors:
                try:
                    act = agents[i](obs)
                except Exception as exc:  # noqa: BLE001 - mirror env behaviour
                    errors[i] = repr(exc)
                    state[i].status = "ERROR"
                    act = {"farmer": ["PASS"], "hands": [], "market": []}
            else:
                act = agents[i](obs)
            state[i].action = act if isinstance(act, dict) else {"farmer": ["PASS"], "hands": [], "market": []}
        K.interpreter(state, env)
        if on_step is not None:
            on_step(step, state, env)
        if all(s.status != "ACTIVE" for s in state):
            break

    farms = state[0].observation.farms
    return {
        "reward": [float(farms[0]["money"]), float(farms[1]["money"])],
        "status": [s.status for s in state],
        "errors": errors,
        "seed": env.info.get("seed"),
        "state": state,
        "env": env,
    }


def play(agent_a, agent_b, seed=None, **kw):
    r = run_episode(agent_a, agent_b, seed=seed, **kw)
    a, b = r["reward"]
    if r["status"][0] == "ERROR":
        a = -1.0
    if r["status"][1] == "ERROR":
        b = -1.0
    return a, b, r


def match(agent_a, agent_b, seeds, swap=True, workers=1, **kw):
    """Play `agent_a` vs `agent_b` on each seed, both seat orders if swap.

    Returns (wins_a, wins_b, ties, records)."""
    jobs = []
    for s in seeds:
        jobs.append((agent_a, agent_b, s, False))
        if swap:
            jobs.append((agent_b, agent_a, s, True))
    records = []
    for a, b, s, swapped in jobs:
        ra, rb, r = play(a, b, seed=s, **kw)
        if swapped:
            ra, rb = rb, ra
        records.append({"seed": s, "swapped": swapped, "a": ra, "b": rb,
                        "status": r["status"], "errors": r["errors"]})
    wa = sum(1 for r in records if r["a"] > r["b"])
    wb = sum(1 for r in records if r["b"] > r["a"])
    ties = len(records) - wa - wb
    return wa, wb, ties, records
