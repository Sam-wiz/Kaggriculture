"""Rank mined opponent tapes by how they fare against our current best agent."""
import gzip, glob, json, os, sys, hashlib, statistics
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness

BEST = "port2/h_over.py"
PASS = {"farmer": ["PASS"], "hands": [], "market": []}


def make_agent_from_path(path):
    with gzip.open(path, "rt") as f:
        actions = json.load(f)["opp_actions"]
    n = len(actions)

    def agent(obs):
        step = obs.get("step")
        if step is None:
            step = int(obs.get("day", 0)) * 24 + int(obs.get("hour", 0))
        if step < 0 or step >= n:
            return dict(PASS)
        a = actions[step]
        if not isinstance(a, dict):
            return dict(PASS)
        hands = a.get("hands") or []
        have = len(obs["farms"][obs["player"]].get("hands", []))
        if len(hands) > have:
            hands = hands[:have]
        elif len(hands) < have:
            hands = list(hands) + [["PASS"]] * (have - len(hands))
        return {"farmer": a.get("farmer", ["PASS"]), "hands": hands,
                "market": (a.get("market") or [])[:10]}
    return agent


def _job(args):
    path, seed, swap = args
    ag = make_agent_from_path(path)
    x, y = (BEST, ag) if swap else (ag, BEST)
    r = harness.run_episode(x, y, seed=seed, catch_errors=True)
    if r["errors"] != [None, None]:
        return None
    p, q = (r["reward"][::-1] if swap else r["reward"])
    return (p, q)


def main(nseed=6, workers=8):
    recs = []
    for p in sorted(glob.glob("mine/tapes/*.json.gz")):
        with gzip.open(p, "rt") as f:
            r = json.load(f)
        r["_path"] = p
        recs.append(r)
    print("episodes mined:", len(recs))
    ours = [r["our_bank"] for r in recs if r.get("our_bank") is not None]
    opps = [r["opp_bank"] for r in recs if r.get("opp_bank") is not None]
    won = sum(1 for r in recs if (r.get("our_bank") or 0) > (r.get("opp_bank") or 0))
    print("our ladder record here: %d-%d   mean bank %.0f vs %.0f"
          % (won, len(recs) - won, statistics.mean(ours), statistics.mean(opps)))
    best = {}
    for r in recs:
        if not r.get("opp_actions"):
            continue
        k = r["opponent"]
        if k not in best or r["opp_bank"] > best[k]["opp_bank"]:
            best[k] = r
    print("distinct opponents:", len(best))
    seeds = list(range(1, nseed + 1))
    jobs, index = [], []
    for name, r in best.items():
        for s in seeds:
            for swap in (0, 1):
                jobs.append((r["_path"], s, swap))
                index.append(name)
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res = list(ex.map(_job, jobs))
    agg = {}
    for name, out in zip(index, res):
        a = agg.setdefault(name, [0, 0, 0, 0.0, 0])
        if out is None:
            a[4] += 1
            continue
        p, q = out
        a[0] += p > q; a[1] += q > p; a[2] += p == q; a[3] += p - q
    rows = []
    for name, (w, l, t, m, bad) in agg.items():
        n = w + l + t
        rows.append((name, best[name]["opp_bank"], w, l, t, m / max(1, n), bad))
    rows.sort(key=lambda x: (-x[2], -x[5]))
    print(f"\n{'opponent':<26}{'ladderBank':>11}{'W':>4}{'L':>4}{'T':>4}{'margin vs h_over':>18}{'err':>5}")
    for name, bank, w, l, t, m, bad in rows:
        print(f"{name[:25]:<26}{bank:>11.0f}{w:>4}{l:>4}{t:>4}{m:>18,.0f}{bad:>5}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 6)
