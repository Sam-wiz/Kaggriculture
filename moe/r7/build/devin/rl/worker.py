"""Pool worker for the RL loop: kagsim eval of a compiled blueprint
(seat 0) against a named opponent (seat 1), paired by seed.

Opponents load ONCE per worker process (init_worker). All per-turn agent
exceptions are caught and counted — a silently-PASS-ing candidate still
produces a valid row so a broken member just loses (and is visible in
cerr), per HANDOFF rule 4.
"""
import json
import sys

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
for _p in (ROOT, ROOT + "/kaggriculture-island-ga",
           ROOT + "/moe/r3/build/opus",
           ROOT + "/moe/r7/build/devin/rl"):
    if _p not in sys.path:
        sys.path.insert(0, _p)

PASS = {"farmer": ["PASS"], "hands": [], "market": []}
_OPPS = {}

OPP_PATHS = {
    "m30b": ROOT + "/subAB_m30b.py",
    "v8":   ROOT + "/rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py",
    "shep": ROOT + "/subW_shepherd.py",
}


def init_worker():
    from run import load
    for name, path in OPP_PATHS.items():
        a, _ = load(path, "o")
        _OPPS[name] = a


def _play(cand, opp, seed, steps=719):
    import kagsim
    g = kagsim.Game(seed=int(seed))
    cerr = oerr = 0
    for _t in range(steps):
        try:
            a0 = cand(g.observe(0))
        except Exception:
            a0 = dict(PASS)
            cerr += 1
        try:
            a1 = opp(g.observe(1)) if opp is not None else dict(PASS)
        except Exception:
            a1 = dict(PASS)
            oerr += 1
        g.step(a0, a1)
    r0 = float(g.reward(0) or 0.0)
    r1 = float(g.reward(1) or 0.0)
    return r0, r1, cerr, oerr


def eval_member(task):
    """task = (gid, bp_json, [(seed, opp_name), ...])
    -> list of per-game rows."""
    import exec3
    gid, bp_json, games = task
    out = []
    try:
        bp = json.loads(bp_json)
        cand_proto = bp
        exec3.Executor3(bp)          # init check
    except Exception as e:
        return [dict(gid=gid, err="bp_init:" + repr(e)[:120])]
    for seed, oname in games:
        try:
            cand = exec3.make_agent(cand_proto)
        except Exception as e:
            out.append(dict(gid=gid, seed=seed, opp=oname,
                            err="mk:" + repr(e)[:120]))
            continue
        opp = _OPPS.get(oname)
        try:
            r0, r1, cerr, oerr = _play(cand, opp, seed)
            out.append(dict(gid=gid, seed=int(seed), opp=oname,
                            r0=r0, r1=r1, margin=r0 - r1,
                            win=1.0 if r0 > r1 else
                            (0.5 if r0 == r1 else 0.0),
                            cerr=cerr, oerr=oerr))
        except Exception as e:      # engine/step fault: row, not a crash
            out.append(dict(gid=gid, seed=int(seed), opp=oname,
                            err="step:" + repr(e)[:120]))
    return out


def eval_pairs(task):
    """task = (tag, [agent_specs], seed, opp_name) — eval a list of
    (label, bp_json) candidates? kept for pairwise confirm; unused."""
    raise NotImplementedError
