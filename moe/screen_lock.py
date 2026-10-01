"""Stage-1 screen: every agent extracted from the 09-21..09-23 lock-window kernels (rivals7/)
vs a reference build, both seats, fresh seeds. Real engine via harness. Winners go to moe/gate.py."""
import glob, json, os, statistics, sys
from concurrent.futures import ProcessPoolExecutor
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT); sys.path.insert(0, ROOT)
import harness
REF = sys.argv[1] if len(sys.argv) > 1 else "subK_pipe16.py"
S0, N = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (1354, 6)
W = int(sys.argv[4]) if len(sys.argv) > 4 else 3
def job(a):
    c, s, sw = a
    x, y = (REF, c) if sw else (c, REF)
    try: r = harness.run_episode(x, y, seed=s, catch_errors=True)
    except Exception as e: return (c, s, sw, None, repr(e)[:80])
    if r["status"][0] != "DONE" or r["status"][1] != "DONE": return (c, s, sw, None, str(r["errors"])[:80])
    p, q = r["reward"][::-1] if sw else r["reward"]
    return (c, s, sw, p - q, None)
if __name__ == "__main__":
    cands = sorted(glob.glob("rivals7/*/main.py"))
    seeds = [r["seed"] for r in json.load(open("data/seedindex_900000_1400.json"))][S0:S0 + N]
    jobs = [(c, s, sw) for c in cands for s in seeds for sw in (0, 1)]
    print(f"{len(jobs)} games: {len(cands)} lock-window agents vs {REF}", flush=True)
    with ProcessPoolExecutor(max_workers=W) as ex: res = list(ex.map(job, jobs, chunksize=2))
    json.dump(res, open(f"moe/screen_lock_{os.path.basename(REF)}.json", "w"))
    rows = []
    for c in cands:
        rs = [r for r in res if r[0] == c]; ok = [r[3] for r in rs if r[3] is not None]
        if not ok: rows.append((-1, c, 0, 0, rs[0][4] if rs else "")); continue
        wr = statistics.mean(1 if m > 0 else .5 if m == 0 else 0 for m in ok)
        rows.append((wr, c, statistics.mean(ok), len(ok), ""))
    print(f"\n{'agent':<62}{'winVsRef':>9}{'margin':>9}{'n':>4}")
    for wr, c, m, n, err in sorted(rows, reverse=True):
        name = c.split('/')[1][:60]
        print(f"{name:<62}{'ERR':>9}  {err}" if wr < 0 else f"{name:<62}{wr:>9.2f}{m:>+9.0f}{n:>4}{'   <==' if wr >= .6 else ''}")
