"""Closed-loop gate for C1-chassis candidates (kagsim). Both sides are live agents.
Job: {x: name, xp: path, o: name, op: path, seed, us (x's seat), ep (optional: _V92_EP parity holdout for BOTH sides)}
Returns x's margin, banks, both sides' PREDICT telemetry and x's _DC_REPORT if present.
usage: gate.py OUT.jsonl JOBS.json WORKERS
"""
import json, os, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from run import load, act, tele
import kagsim


def job(j):
    t0 = time.time()
    try:
        a, ma = load(j["xp"], "x"); b, mb = load(j["op"], "o")
        if j.get("ep") is not None and hasattr(ma, "_V92_EP"):
            # Parity holdout on the CANDIDATE only (its PREDICT2 library holds the recorded WLV streams). The same
            # global also filters the P library, whose streams carry ep=-1 and would ALL be dropped on odd episodes;
            # the P library holds no WLV games, so shield it. (Fix 06:0x UTC: the first run set it on both sides.)
            ma._V92_EP = int(j["ep"])
            _orig = ma._v92_p_forecast
            def _pf(obs, st, _o=_orig, _m=ma):
                sv = _m._V92_EP; _m._V92_EP = None
                try:
                    return _o(obs, st)
                finally:
                    _m._V92_EP = sv
            ma._v92_p_forecast = _pf
        g = kagsim.Game(seed=int(j["seed"])); us = j["us"]
        for t in range(720):
            o0, o1 = g.observe(0), g.observe(1)
            A, B = (a, b) if us == 0 else (b, a)
            g.step(act(A, o0), act(B, o1))
        r = [float(g.reward(0)), float(g.reward(1))]
        return dict(j, m=r[us] - r[1 - us], me=r[us], opp=r[1 - us], tx=tele(ma), to=tele(mb),
                    dc=dict(getattr(ma, "_DC_REPORT", {}) or {}), s=round(time.time() - t0, 1))
    except Exception as e:
        return dict(j, err=repr(e)[:200])


if __name__ == "__main__":
    out, jobs, W = sys.argv[1], json.load(open(sys.argv[2])), int(sys.argv[3])
    key = lambda r: (r["x"], r["o"], r["seed"], r["us"])
    done = set()
    if os.path.exists(out):
        for line in open(out):
            done.add(key(json.loads(line)))
    jobs = [j for j in jobs if key(j) not in done]
    print(len(jobs), "jobs", flush=True)
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=W) as ex, open(out, "a") as f:
        for i, r in enumerate(ex.map(job, jobs, chunksize=1), 1):
            f.write(json.dumps(r) + "\n"); f.flush()
            if i % 10 == 0: print(i, flush=True)
