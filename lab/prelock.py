"""Pre-lock re-baseline sweep: screen every new public agent against our best live build.

Public notebook sharing closes 2026-09-23 23:59 UTC (Addison Howard, Kaggle Staff, confirmed in
discussions.md). After that no new public agent can appear, and adopting the best public agent is
the only activity in 19 days that has produced a large gain. So this is the last chance to harvest
the lever, and it is worth screening everything rather than only the high-vote entries -- the
09-16 sweep found that vote count tracks republication, not strength (two of the highest-voted
notebooks were byte-identical copies of others).

Scored by paired win rate against the live base, both seats, on seeds never used for fitting.
"""
import json
import os
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

BASE = "subJ_2945.py"          # our best live build
CANDIDATES = [
    ("shiiin9-beat-v48", "rivals/shiiin9_beat-v48-100-0-your-herd-is-decided-on-day-6/main.py"),
    ("metav4-v13", "rivals/thomastschinkel_the-metav4-farm-submission-v13/main.py"),
    ("v51-lean-flock", "rivals/ahmedberatozer_kaggriculture-v51-lean-flock/v51_agent/main.py"),
    ("v50-early-yarn", "rivals/ahmedberatozer_kaggriculture-v50-early-yarn-commit/v50_agent/main.py"),
    ("gods-mode", "rivals/leoprovorov_god-s-mode-hacked-stores/gods_mode_hacked_stores/base_agent.py"),
    ("counter-big3", "rivals/haideptry_countering-the-big-3-meta/main.py"),
    ("pipe16", "rivals/nathanjacob_kaggriculture-pipe16-idle-workers/main.py"),
    ("pipe15", "rivals/nathanjacob_kaggriculture-pipe15-two-layers/main.py"),
    ("master-v4", "rivals/guruprasaathas111_kaggriculture-master-engine-v4/main.py"),
]


def _job(a):
    lab, path, seed, swap = a
    if not os.path.exists(path):
        return (lab, None, None)
    x, y = (BASE, path) if swap else (path, BASE)
    try:
        r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    except Exception:
        return (lab, None, None)
    p, q = (r["reward"][::-1] if swap else r["reward"])
    return (lab, 1 if p > q else (0.5 if p == q else 0), p - q)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    idx = json.load(open("data/seedindex_900000_1400.json"))
    seeds = [r["seed"] for r in idx][:n]
    jobs = [(lab, p, s, sw) for lab, p in CANDIDATES for s in seeds for sw in (0, 1)]
    print(f"{len(jobs)} games vs {BASE}", flush=True)
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=4))
    print(f"\n{'challenger':<20}{'winsVsBase':>12}{'margin':>11}{'n':>5}")
    rows = []
    for lab, _ in CANDIDATES:
        rs = [r for r in res if r[0] == lab and r[1] is not None]
        if not rs:
            print(f"{lab:<20}{'FAILED / missing':>12}")
            continue
        wr = statistics.mean(r[1] for r in rs)
        mg = statistics.mean(r[2] for r in rs)
        rows.append((lab, wr, mg, len(rs)))
    for lab, wr, mg, k in sorted(rows, key=lambda r: -r[1]):
        flag = "  <-- BEATS OUR BASE" if wr > 0.5 else ""
        print(f"{lab:<20}{wr:>12.3f}{mg:>+11,.0f}{k:>5}{flag}", flush=True)
