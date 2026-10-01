"""Fingerprint recorded seats against every agent file we hold (exact-prefix identification).

Candidate c plays seat s on the recorded seed (kagsim) against the recorded opponent tape. Before the
first divergence the state is identical to the recording, so the open-loop opponent is exact there.
Reports first divergence of the full action, the unit channel and the market channel (cap K steps).
usage: fp.py OUT.jsonl K WORKERS EP:SEAT[,EP:SEAT...] [CAND_GLOB ...]
"""
import glob, gzip, json, os, sys, signal
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from run import load, act, PASS
import kagsim


def canon(a, part=None):
    if not isinstance(a, dict): return None
    if part == "u": return json.dumps([a.get("farmer")] + list(a.get("hands") or []))
    if part == "m": return json.dumps(a.get("market") or [])
    return json.dumps(dict(farmer=a.get("farmer"), hands=list(a.get("hands") or []), market=a.get("market") or []), sort_keys=True)


class TO(Exception): pass


def _alarm(*_): raise TO()


def job(arg):
    cand, ep, seat, K = arg
    d = json.load(gzip.open(f"mine/top10/{ep}.json.gz", "rt"))
    acts = d["actions"]
    signal.signal(signal.SIGALRM, _alarm); signal.alarm(60)
    try:
        fn, m = load(cand, "fp")
        g = kagsim.Game(seed=int(d["seed"]))
        pre = dict(full=None, u=None, m=None)
        for t in range(min(K, 719)):
            o = [g.observe(0), g.observe(1)]
            a = act(fn, o[seat]); rec = acts[t + 1][seat]
            for k, part in (("full", None), ("u", "u"), ("m", "m")):
                if pre[k] is None and canon(a, part) != canon(rec, part): pre[k] = t + 1
            if pre["u"] is not None and pre["m"] is not None: break
            other = acts[t + 1][1 - seat] if isinstance(acts[t + 1][1 - seat], dict) else PASS
            pair = (rec if isinstance(rec, dict) else PASS, other)  # keep the recorded trajectory
            g.step(*(pair if seat == 0 else pair[::-1]))
        signal.alarm(0)
        return dict(cand=cand, ep=ep, seat=seat, team=d["teams"][seat], **{k: (v if v is not None else K) for k, v in pre.items()})
    except TO:
        return dict(cand=cand, ep=ep, seat=seat, err="timeout")
    except Exception as e:
        signal.alarm(0)
        return dict(cand=cand, ep=ep, seat=seat, err=repr(e)[:80])


if __name__ == "__main__":
    out, K, W = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    targets = [(int(x.split(":")[0]), int(x.split(":")[1])) for x in sys.argv[4].split(",")]
    globs = sys.argv[5:] or ["rivals*/*/_entry.py", "rivals*/*/main.py", "sub*.py", "rivals7/*/main.py"]
    cands = []
    for gpat in globs:
        for p in sorted(glob.glob(gpat)):
            dd = os.path.dirname(p)
            if p.endswith("/main.py") and os.path.exists(os.path.join(dd, "_entry.py")): continue
            cands.append(p)
    cands = sorted(set(cands))
    done = set()
    if os.path.exists(out):
        for line in open(out):
            try: r = json.loads(line); done.add((r["cand"], r["ep"], r["seat"]))
            except Exception: pass
    jobs = [(c, ep, s, K) for c in cands for ep, s in targets if (c, ep, s) not in done]
    print(len(cands), "candidates,", len(jobs), "jobs", flush=True)
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=W, max_tasks_per_child=20) as ex, open(out, "a") as f:
        for i, r in enumerate(ex.map(job, jobs, chunksize=1), 1):
            f.write(json.dumps(r) + "\n"); f.flush()
            if i % 200 == 0: print(i, flush=True)
