"""Island-GA over kagsim + exec3 (row-walker executor).

Usage: python run_ga.py [hours] [out_dir]
"""
import json
import sys
import time

sys.path.insert(0, "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture")
sys.path.insert(0,
    "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/kaggriculture-island-ga")

import kagsim
import exec3
import multiprocessing as mp
from islandga.search import SearchConfig, run_search

PASS = {"farmer": ["PASS"], "hands": [], "market": []}


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


def margin_of(bp, seed):
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


def eval_stream(pool, tasks):
    if pool is None:
        for gid, bp_json, seed in tasks:
            yield gid, seed, margin_of(json.loads(bp_json), seed)
    else:
        from gaworker import worker_eval
        yield from pool.imap_unordered(worker_eval, tasks, chunksize=1)


def main():
    hours = float(sys.argv[1]) if len(sys.argv) > 1 else 0.25
    out = sys.argv[2] if len(sys.argv) > 2 else "results/run1"
    procs = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    cfg = SearchConfig(
        seeds=(11, 23, 47),
        confirm_seeds=(5, 13, 29, 61, 83),
        pop=8,
        hours=hours,
        pool_file=None,          # opponent pool only matters for in-company
    )
    if procs:
        ctx = mp.get_context("spawn")
        run_search(cfg, out, eval_stream=eval_stream,
                   pool_factory=lambda p: ctx.Pool(procs))
    else:
        run_search(cfg, out, eval_stream=eval_stream,
                   pool_factory=lambda p: _NoPool())


class _NoPool:
    def close(self):
        pass

    def join(self):
        pass


if __name__ == "__main__":
    main()
