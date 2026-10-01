"""Identify which agent a live near-mirror opponent actually ran, by exact closed-loop reproduction.

For a recorded game (our seat = shepherd), re-run it on the recorded seed with shepherd in our seat
and candidate C in the opponent seat, both closed-loop. If C is what the opponent ran, C's emitted
actions reproduce the recorded opponent actions step for step. Score = fraction of the 719 steps
where C's action == recorded opponent action; prefix = first step where they differ.
usage: identify.py OUT.jsonl N_GAMES WORKERS  (candidates = rivals7/*/main.py + our builds)
"""
import glob, gzip, json, os, sys
from concurrent.futures import ProcessPoolExecutor
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT); sys.path.insert(0, ROOT)
import harness

SHEP = "subW_shepherd.py"


def canon(a):
    return json.dumps(a, sort_keys=True) if isinstance(a, dict) else None


def job(arg):
    ep, cand = arg
    d = json.load(gzip.open(f"mine/opp/{ep}.json.gz", "rt"))
    me = d["teams"].index("Sam-wiz"); op = 1 - me
    rec = [canon(x[op]) for x in d["actions"]]
    got = {}

    def on_step(step, state, env):
        got[step] = canon(state[op].action)
    try:
        pair = (SHEP, cand) if me == 0 else (cand, SHEP)
        r = harness.run_episode(pair[0], pair[1], seed=d["seed"], on_step=on_step, catch_errors=True)
    except Exception as e:
        return dict(ep=ep, cand=cand, err=repr(e)[:80])
    # recorded actions[t] produced step t; our on_step(step) sees the action that produced step+1
    n = match = 0; prefix = None
    for s in range(len(rec) - 1):
        a, b = got.get(s), rec[s + 1]
        if b is None: continue
        n += 1
        if a == b: match += 1
        elif prefix is None: prefix = s
    return dict(ep=ep, cand=cand, match=match / max(n, 1), prefix=prefix,
                bank=r["reward"][op], rec_bank=d["rewards"][op])


if __name__ == "__main__":
    out, ngames, W = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    ids = json.load(open("moe/r3/live_episode_ids.json"))["56549546"]
    lb = json.load(open("moe/r3/lb_0925_1612.json"))
    def ops(a):
        if not isinstance(a, dict): return ()
        return tuple(tuple(x) if isinstance(x, list) else x for x in [a.get("farmer")] + list(a.get("hands") or []))
    games = []
    for e in ids:
        d = json.load(gzip.open(f"mine/opp/{e}.json.gz", "rt")); t = d["teams"]; me = t.index("Sam-wiz")
        R = lb.get(t[1 - me]) or 0
        same = sum(1 for x in d["actions"] if ops(x[me]) == ops(x[1 - me])) / len(d["actions"])
        if R >= 2200 and same >= 0.95: games.append(e)
    games = games[:ngames]
    cands = sorted(glob.glob("rivals7/*/main.py")) + ["subW_shepherd.py", "subX_hyb2965.py", "subV_sir2.py"]
    jobs = [(e, c) for e in games for c in cands]
    print(f"{len(games)} clone games x {len(cands)} candidates = {len(jobs)} runs", flush=True)
    with ProcessPoolExecutor(max_workers=W) as ex, open(out, "w") as f:
        for r in ex.map(job, jobs, chunksize=1):
            f.write(json.dumps(r) + "\n"); f.flush()
