"""Shop-matched tape router over a top-10 team's own library."""

import json
from pathlib import Path

PASS = {"farmer": ["PASS"], "hands": [], "market": []}
MAX_ORDERS = 10


def _read(obs, key, default=None):
    try:
        if isinstance(obs, dict):
            return obs.get(key, default)
        return getattr(obs, key, default)
    except Exception:
        return default


def _score(observed, recorded):
    """How well a recorded draw matches what actually unlocked: order first, then multiset."""
    if list(observed) == list(recorded):
        return 100
    a, b = sorted(observed), sorted(recorded)
    if a == b:
        return 90
    return sum(1 for s in observed if s in recorded) * 10


class Router:
    def __init__(self, folder):
        blob = json.loads((Path(folder) / "library.json").read_text())
        self.tapes = blob["tapes"]
        self.draws = blob["draws"]
        self.banks = blob["banks"]
        self.switch = int(blob["switch"])
        if not self.tapes or any(len(t) < 700 for t in self.tapes):
            raise ValueError("library requires complete tapes")
        self.active = 0
        self.decided = False

    def act(self, obs):
        step = _read(obs, "step")
        if step is None:
            step = int(_read(obs, "day", 0) or 0) * 24 + int(_read(obs, "hour", 0) or 0)
        step = int(step)
        if step == 0:
            self.active = 0
            self.decided = False
        if not self.decided and step >= self.switch:
            shops = list((_read(obs, "town", {}) or {}).get("unlocked_shops") or [])
            best, best_key = 0, None
            for i, rec in enumerate(self.draws):
                key = (_score(shops, rec), self.banks[i])
                if best_key is None or key > best_key:
                    best, best_key = i, key
            self.active = best
            self.decided = True
        tape = self.tapes[self.active]
        if 0 <= step < len(tape):
            a = tape[step]
            if isinstance(a, dict):
                farms = _read(obs, "farms") or []
                seat = int(_read(obs, "player", 0) or 0)
                have = len(((farms[seat] if seat < len(farms) else {}) or {}).get("hands") or [])
                hands = list(a.get("hands") or [])[:have]
                hands += [["PASS"]] * (have - len(hands))
                return {"farmer": a.get("farmer", ["PASS"]), "hands": hands,
                        "market": list(a.get("market") or [])[:MAX_ORDERS]}
        return dict(PASS)


_ROUTER = None


def agent(observation, configuration=None):
    """A crash here forfeits the game, so any failure degrades to a legal PASS."""
    global _ROUTER
    try:
        if _ROUTER is None:
            # Kaggle's source loader omits __file__ but preserves the code filename.
            _ROUTER = Router(Path(agent.__code__.co_filename).resolve().parent)
        return _ROUTER.act(observation)
    except Exception:
        try:
            farms = observation["farms"]
            hands = farms[int(observation.get("player", 0))].get("hands") or []
        except Exception:
            hands = []
        return {"farmer": ["PASS"], "hands": [["PASS"] for _ in hands], "market": []}
