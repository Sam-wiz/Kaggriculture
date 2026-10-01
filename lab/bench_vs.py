"""Head-to-head candidates vs a base, paired seeds x both seats.

Usage: bench_vs.py BASE_FILE "name=path,name=path" START_SEED [N_SEEDS]
"""
import os
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness


def kload(path):
    src = open(path).read()
    env = {}
    exec(compile(src, path, "exec"), env)  # noqa: S102
    return [v for v in env.values() if callable(v)][-1]


def job(a):
    name, cp, bp, s, sw = a
    ca = kload(cp)
    ba = kload(bp)
    x, y = (ba, ca) if sw else (ca, ba)
    r = harness.run_episode(x, y, seed=s, catch_errors=True)
    p, q = r["reward"][::-1] if sw else r["reward"]
    return name, p, q


if __name__ == "__main__":
    base = sys.argv[1]
    cands = dict(kv.split("=", 1) for kv in sys.argv[2].split(","))
    start = int(sys.argv[3])
    nseeds = int(sys.argv[4]) if len(sys.argv) > 4 else 20
    jobs = [(n, p, base, s, sw) for n, p in cands.items()
            for s in range(start, start + nseeds) for sw in (0, 1)]
    res = {n: [] for n in cands}
    with ProcessPoolExecutor(7) as ex:
        for n, p, q in ex.map(job, jobs, chunksize=2):
            res[n].append(p - q)
    for n, ms in res.items():
        w = sum(1 for m in ms if m > 0)
        l = sum(1 for m in ms if m < 0)
        print("%-12s W%d-L%d  margin=%+.0f" % (n, w, l, sum(ms) / len(ms)))
