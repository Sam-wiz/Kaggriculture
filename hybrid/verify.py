"""Assert every episode reaches 720 steps with status DONE on both seats."""
import os, sys
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness, evalpool

def _job(t):
    a, b, s = t
    r = harness.run_episode(a, b, seed=s, catch_errors=True)
    return dict(a=a, b=b, seed=s, status=r["status"], errors=r["errors"],
                reward=r["reward"])

if __name__ == "__main__":
    me = sys.argv[1]
    seeds = [1, 2, 3, 20, 21]
    jobs = []
    for opp in evalpool.available() + ["pass", "random", "starter", me]:
        for s in seeds:
            jobs.append((me, opp, s))
            jobs.append((opp, me, s))
    with ProcessPoolExecutor(max_workers=8) as ex:
        res = list(ex.map(_job, jobs))
    bad = [r for r in res if r["status"] != ["DONE", "DONE"] or any(r["errors"])]
    print(f"{len(res)} episodes, {len(bad)} not clean")
    for r in bad[:10]:
        print("  ", os.path.basename(str(r["a"])), "vs", os.path.basename(str(r["b"])),
              "seed", r["seed"], r["status"], r["errors"])
