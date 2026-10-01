"""Replay a recorded action tape as an agent.

A player's own farm evolves deterministically from their own actions apart from seeded weed spawns,
so a tape recorded in one episode still drives a coherent farm in another. Only the shared market
differs, and market orders are quantity-based. Illegal actions are silent no-ops in the engine, so
drift degrades gracefully rather than crashing.
"""
import gzip, json


def load_tape(path):
    with gzip.open(path, "rt") as f:
        return json.load(f)


PASS = {"farmer": ["PASS"], "hands": [], "market": []}


def make_agent(actions):
    n = len(actions)

    def agent(obs):
        step = obs.get("step")
        if step is None:
            step = int(obs.get("day", 0)) * 24 + int(obs.get("hour", 0))
        if step < 0 or step >= n:
            return dict(PASS)
        a = actions[step]
        if not isinstance(a, dict):
            return dict(PASS)
        # the recorded hands list must match how many hands we actually have today
        hands = a.get("hands") or []
        have = len(obs["farms"][obs["player"]].get("hands", []))
        if len(hands) > have:
            hands = hands[:have]
        elif len(hands) < have:
            hands = list(hands) + [["PASS"]] * (have - len(hands))
        return {"farmer": a.get("farmer", ["PASS"]), "hands": hands,
                "market": (a.get("market") or [])[:10]}

    return agent
