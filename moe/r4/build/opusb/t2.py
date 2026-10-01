"""T2 — screen every top-dump tape (one seat of one recorded game) on fresh seeds vs a live agent, closed-loop.

The tape is OUR candidate (open-loop by nature); the opponent is a live agent that reacts, so this is a valid
closed-loop measurement of "tape vs live agent" (the C18 objection is about open-loop OPPONENTS).
Job: {g: path, seat: k, seed: fresh seed, pos: 0|1 (tape plays seat pos), live: path}
usage: t2.py OUT.jsonl JOBS.json WORKERS
"""
import gzip, json, os, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
sys.path.insert(0, ROOT + "/moe/r4/build/opusb")
from run import load, act, PASS
from t1 import TELE, ep, tape
import kagsim

_CACHE = {}


def live(path):
    if path not in _CACHE:
        _CACHE.clear(); _CACHE[path] = load(path, "lv")
    return _CACHE[path]


def job(j):
    t0 = time.time()
    try:
        G = ep(j["g"]); X = tape(G["actions"], j["seat"])
        fn, m = load(j["live"], "lv")   # fresh module per game: agents keep per-game state
        O = lambda o: act(fn, o)
        p = j["pos"]
        g = kagsim.Game(seed=int(j["seed"]))
        for t in range(720):
            o0, o1 = g.observe(0), g.observe(1)
            g.step(X(o0) if p == 0 else O(o0), O(o1) if p == 0 else X(o1))
        r = [float(g.reward(0)), float(g.reward(1))]
        return dict(j, team=G["teams"][j["seat"]], rec_me=G["rewards"][j["seat"]], me=r[p], opp=r[1 - p],
                    tele={k: g.telemetry(p).get(k) for k in TELE}, s=round(time.time() - t0, 1))
    except Exception as e:
        return dict(j, err=repr(e)[:200])


if __name__ == "__main__":
    out, jobs, W = sys.argv[1], json.load(open(sys.argv[2])), int(sys.argv[3])
    key = lambda r: (r["g"], r["seat"], r["seed"], r["pos"], r["live"])
    done = set()
    if os.path.exists(out):
        for line in open(out):
            done.add(key(json.loads(line)))
    jobs = [j for j in jobs if key(j) not in done]
    print(len(jobs), "jobs", flush=True)
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=W) as ex, open(out, "a") as f:
        for i, r in enumerate(ex.map(job, jobs, chunksize=1), 1):
            f.write(json.dumps(r, ensure_ascii=False) + "\n"); f.flush()
            if i % 20 == 0: print(i, flush=True)
