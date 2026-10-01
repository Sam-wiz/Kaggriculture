"""Spawn-pool worker for run_ga: kagsim + exec3 evaluation.

Must be importable in spawned processes -> PYTHONPATH must include the
repo root and kaggriculture-island-ga when launching.
"""
import json
import sys

for _p in ("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture",
           "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/"
           "kaggriculture-island-ga"):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import kagsim            # noqa: E402
import exec3             # noqa: E402

PASS = {"farmer": ["PASS"], "hands": [], "market": []}
_OPP = None


def _opp():
    global _OPP
    if _OPP is None:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "opp", "/Users/samrudh/Documents/Projects/kaggle/"
            "Kaggriculture/subI_pipe7.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        _OPP = m.agent
    return _OPP


def bank_of(bp, seed):
    agent = exec3.make_agent(bp)
    game = kagsim.Game(seed=int(seed))
    for _ in range(720):
        try:
            act = agent(game.observe(0))
        except Exception:
            act = dict(PASS)
        game.step(act, dict(PASS))
    return float(game.reward(0))


def margin_vs_opp(bp, seed):
    """In-company fitness: candidate (seat 0) vs pipe7 (seat 1).
    Returns margin = cand - opp bank."""
    cand = exec3.make_agent(bp)
    opp = _opp()
    game = kagsim.Game(seed=int(seed))
    for _ in range(720):
        try:
            a0 = cand(game.observe(0))
        except Exception:
            a0 = dict(PASS)
        try:
            a1 = opp(game.observe(1))
        except Exception:
            a1 = dict(PASS)
        game.step(a0, a1)
    return float(game.reward(0) - game.reward(1))


def worker_eval(task):
    gid, bp_json, seed = task
    return gid, seed, margin_vs_opp(json.loads(bp_json), seed)
