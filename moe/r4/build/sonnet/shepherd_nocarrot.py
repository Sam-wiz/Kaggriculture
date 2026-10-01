"""
Crude carrot-ablation wrapper on subW_shepherd.py.

Q1 evidence (meta/episode_features.csv, submission-level, peak-rating band):
carrot's share of plantings falls monotonically with rating and hits ~0.00
above 2900, while our live chassis (shepherd/hyb2965 lineage) still plants
carrot at ~3-6% of tiles (mine/opp sample). This wrapper does the crudest
possible test of "does dropping carrot help": intercept any PLANT CARROT
call from the base agent (farmer or hands) and turn it into a PASS instead.
It does NOT reallocate the freed land/actions to melon/strawberry, so any
positive result here is a lower bound on the real lever.
"""
import importlib.util
import os
import sys

_ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
_BASE_PATH = os.path.join(_ROOT, "subW_shepherd.py")


def _load_base():
    spec = importlib.util.spec_from_file_location("_shep_base_nocarrot", _BASE_PATH)
    m = importlib.util.module_from_spec(spec)
    sys.modules["_shep_base_nocarrot"] = m
    spec.loader.exec_module(m)
    return m.agent


_base_agent = _load_base()

REPORT = {"blocked": 0, "calls": 0}


def _is_plant_carrot(op):
    return isinstance(op, list) and len(op) >= 2 and op[0] == "PLANT" and op[1] == "CARROT"


def _strip(act):
    if not isinstance(act, dict):
        return act
    changed = False
    f = act.get("farmer")
    if _is_plant_carrot(f):
        act = dict(act)
        act["farmer"] = ["PASS"]
        changed = True
        REPORT["blocked"] += 1
    hands = act.get("hands")
    if hands:
        new_hands = []
        h_changed = False
        for h in hands:
            if _is_plant_carrot(h):
                new_hands.append(["PASS"])
                h_changed = True
                REPORT["blocked"] += 1
            else:
                new_hands.append(h)
        if h_changed:
            if not changed:
                act = dict(act)
            act["hands"] = new_hands
    return act


def agent(observation, configuration=None):
    REPORT["calls"] += 1
    act = _base_agent(observation, configuration)
    return _strip(act)
