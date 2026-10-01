"""Screen freshly published agents head-to-head against our live build.

This is the check with the only track record in this project: every real gain came from adopting a
stronger published base (683 -> 2513 -> 2610 -> the public-state router, +190), and every hour of
tuning returned roughly nothing. It costs about forty minutes and should run daily.
"""
import os
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

ME = "sub_vent.py"
NEW = [
    "rivals/y3uanm_kaggriculture-market-impact-router-v4/main.py",
    "rivals/antimocarlino_o-p-a-antimode-v1/main.py",
    "rivals/yamakawanin_king-v4e-rc4/main.py",
    "rivals/dmitriigluzdov_kaggriculture-goose-portfolio-historical-lb-2615/main.py",
    "rivals/yamakawanin_kaggriculture-2312-9-q30-v2a/main.py",
    "rivals/flexonafft_kaggriculture-smart-farm-strategy-lab/main.py",
    "rivals/junaid512_02-adaptive-replay-agent/main.py",
    "rivals/tetsutani_shape-the-shop-work-the-pasture-kaggriculture/main.py",
]


def _job(a):
    opp, seed, swap = a
    x, y = (opp, ME) if swap else (ME, opp)
    try:
        r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    except Exception as e:
        return (opp, None, None, repr(e)[:90])
    me, them = (r["reward"][::-1] if swap else r["reward"])
    err = (r["errors"][::-1] if swap else r["errors"])[1]
    return (opp, me, them, (err or "")[:90])


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    jobs = [(p, s, sw) for p in NEW for s in range(4100, 4100 + n) for sw in (0, 1)]
    with ProcessPoolExecutor(max_workers=7) as ex:
        res = list(ex.map(_job, jobs, chunksize=4))
    print(f"our build: {ME}   ({n} seeds x 2 seats each)\n")
    print(f"{'rival':<50}{'theirBank':>11}{'ourBank':>10}{'ourMargin':>11}{'ourWR':>8}")
    rows = []
    for p in NEW:
        rs = [r for r in res if r[0] == p and r[1] is not None]
        if not rs:
            print(f"{os.path.basename(os.path.dirname(p))[:48]:<50}  FAILED")
            continue
        m = [a - b for _, a, b, _ in rs]
        rows.append((p, statistics.mean(b for _, a, b, _ in rs),
                     statistics.mean(a for _, a, b, _ in rs),
                     statistics.mean(m), sum(1 for x in m if x > 0) / len(m)))
    for p, tb, ob, mg, wr in sorted(rows, key=lambda r: -r[1]):
        flag = "   <-- STRONGER THAN US" if mg < 0 else ""
        print(f"{os.path.basename(os.path.dirname(p))[:48]:<50}{tb:>11,.0f}{ob:>10,.0f}"
              f"{mg:>+11,.0f}{wr:>8.3f}{flag}")
