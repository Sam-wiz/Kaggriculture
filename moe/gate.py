"""MoE gate: round-robin of named agents on fresh seeds, both seats, real engine.

A candidate is only worth a submission slot if it beats the CURRENT LIVE builds head-to-head and
does not lose ground against the near-parity pool. The 13-agent fieldtest.py pool is saturated
(pipe16-class builds beat it ~97%) and cannot rank candidates -- do not use it as a gate.

usage: python moe/gate.py --seeds START N --workers W  name=path [name=path ...]
       (the default POOL below is always included; pass extra candidates as name=path)
Seed slices already used for decisions: [1150:1270], [1300:1330]. Use a fresh slice.
"""
import argparse, itertools, json, os, statistics, sys
from concurrent.futures import ProcessPoolExecutor
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT); sys.path.insert(0, ROOT)
import harness

POOL = [("LIVE_f55rec_V2", "subV2_f55rec.py"),        # live 56531508
        ("LIVE_sir_V1", "subV_sir2.py"),              # live 56532595
        ("f55rec_V1", "subV_f55rec.py"),
        ("sir_V2", "subV2_sir.py"),
        ("koshinm", "rivals/koshinm_kaggriculture-local-best-2026-09-21/main.py"),
        ("melon", "rivals5/kaggriculture-melon-threshold-squeeze-2749/_entry.py"),
        ("2802", "rivals/jaxa623_2802/main.py"),
        ("metav4", "subL_metav4.py")]


def job(a):
    A, i, j, s, sw = a
    x, y = (A[j][1], A[i][1]) if sw else (A[i][1], A[j][1])
    try:
        r = harness.run_episode(x, y, seed=s, catch_errors=True)
    except Exception:
        return (i, j, s, sw, None)
    if r["status"][0] != "DONE" or r["status"][1] != "DONE":
        return (i, j, s, sw, None)
    p, q = r["reward"][::-1] if sw else r["reward"]
    return (i, j, s, sw, p - q)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", nargs=2, type=int, default=[1330, 24])
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--only-candidates", action="store_true",
                    help="play candidates vs pool only (skip pool-vs-pool pairs)")
    ap.add_argument("--out", default=None)
    ap.add_argument("extra", nargs="*")
    a = ap.parse_args()
    cands = [tuple(e.split("=", 1)) for e in a.extra]
    A = POOL + cands
    for n, p in A:
        assert os.path.exists(p), p
    idx = json.load(open("data/seedindex_900000_1400.json"))
    seeds = [r["seed"] for r in idx][a.seeds[0]:a.seeds[0] + a.seeds[1]]
    pairs = list(itertools.combinations(range(len(A)), 2))
    if a.only_candidates and cands:
        k = len(POOL)
        pairs = [(i, j) for i, j in pairs if j >= k or i >= k]
    jobs = [(A, i, j, s, sw) for i, j in pairs for s in seeds for sw in (0, 1)]
    print(f"{len(jobs)} games, {len(A)} agents, seeds [{a.seeds[0]}:{a.seeds[0]+a.seeds[1]}]", flush=True)
    with ProcessPoolExecutor(max_workers=a.workers) as ex:
        res = list(ex.map(job, jobs, chunksize=2))
    if a.out:
        json.dump([r[1:] for r in res], open(a.out, "w"))
    n = len(A); W = [[None] * n for _ in range(n)]
    fails = sum(1 for r in res if r[4] is None)
    for i, j in pairs:
        ms = [r[4] for r in res if r[0] == i and r[1] == j and r[4] is not None]
        if ms:
            w = statistics.mean(1 if m > 0 else .5 if m == 0 else 0 for m in ms)
            W[i][j], W[j][i] = w, 1 - w
    print(f"failed games: {fails}   (row = win rate of row agent vs column; n={2*len(seeds)} per cell)")
    print(f"{'':16}" + "".join(f"{x[0][:8]:>9}" for x in A) + f"{'MEAN':>8}")
    rank = []
    for i in range(n):
        v = [W[i][j] for j in range(n) if j != i and W[i][j] is not None]
        m = statistics.mean(v) if v else float('nan'); rank.append((m, A[i][0]))
        print(f"{A[i][0][:16]:16}" + "".join(
            f"{'--':>9}" if i == j else (f"{W[i][j]:>9.2f}" if W[i][j] is not None else f"{'':>9}")
            for j in range(n)) + f"{m:>8.3f}", flush=True)
    print("\nranking:", " > ".join(x for _, x in sorted(rank, reverse=True)))
