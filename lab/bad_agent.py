
from kaggle_environments.envs.kaggriculture.kaggriculture import agents as _builtin
_starter = _builtin["starter"]

def agent(obs, configuration=None):          # v1 stub, bound FIRST
    return {"farmer": ["PASS"], "hands": [], "market": []}

def _first_shop(obs):                        # a helper, bound AFTER `agent`
    return ((obs or {}).get("town", {}) or {}).get("unlocked_shops", [])

def agent(obs, configuration=None):          # the real agent -- RE-bound, position unchanged
    return _starter(obs)              # the built-in starter takes (obs) only
