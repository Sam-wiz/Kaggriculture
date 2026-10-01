"""Batch Bradley-Terry fit over the public episode dumps.

The live ladder is a SEQUENTIAL estimator starting every submission at 600 and moving ~4.5 points a
game, which is the entire source of our ~240-point lag -- and keiz's 3,047 is the same estimator run
for many more games. A batch fit has no sequential lag: it estimates every agent at once from the
whole win/loss network, so our current submissions and keiz's are placed on equal footing.

This is also the metric that actually pays: the competition's final leaderboard is a Bradley-Terry
tournament run after the deadline.

    P(i beats j) = sigmoid(theta_i - theta_j)

Fitted by regularised MLE (the prior is essential -- unbeaten agents would otherwise run to
infinity), with bootstrap intervals.
"""
import zipfile, json, glob, os, sys, collections, math, random
import numpy as np

ROOT = os.path.dirname(os.path.abspath(__file__))


def load_edges(zips):
    """(winner, loser) per decided episode, plus per-team game counts."""
    edges = []
    teams = collections.Counter()
    for zp in zips:
        try:
            z = zipfile.ZipFile(zp)
        except Exception:
            continue
        for name in z.namelist():
            if not name.endswith(".json"):
                continue
            try:
                with z.open(name) as f:
                    d = json.load(f)
            except Exception:
                continue
            t = d.get("info", {}).get("TeamNames")
            r = d.get("rewards")
            if not t or not r or len(t) != 2 or t[0] == t[1]:
                continue
            if r[0] is None or r[1] is None or r[0] == r[1]:
                continue
            w, l = (0, 1) if r[0] > r[1] else (1, 0)
            edges.append((t[w], t[l]))
            teams[t[0]] += 1; teams[t[1]] += 1
    return edges, teams


def fit_bt(edges, names, reg=1.0, iters=400):
    idx = {n: i for i, n in enumerate(names)}
    W = np.zeros((len(names),), dtype=float)
    wi = np.array([idx[w] for w, l in edges])
    li = np.array([idx[l] for w, l in edges])
    theta = np.zeros(len(names))
    for _ in range(iters):
        d = theta[wi] - theta[li]
        p = 1.0 / (1.0 + np.exp(-d))          # P(winner beats loser) under current theta
        g = np.zeros(len(names))
        np.add.at(g, wi, (1.0 - p))
        np.add.at(g, li, -(1.0 - p))
        g -= reg * theta                       # L2 prior toward 0
        theta += 0.05 * g
        theta -= theta.mean()
    return theta


if __name__ == "__main__":
    zips = sorted(glob.glob(os.path.join(ROOT, "data/ep*/*.zip")))
    print(f"reading {len(zips)} daily dump(s)...", flush=True)
    edges, teams = load_edges(zips)
    print(f"{len(edges):,} decided episodes, {len(teams):,} teams", flush=True)
    MIN = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    keep = {t for t, n in teams.items() if n >= MIN}
    edges = [(w, l) for w, l in edges if w in keep and l in keep]
    names = sorted(keep)
    print(f"after requiring >={MIN} games: {len(edges):,} edges, {len(names):,} teams", flush=True)
    theta = fit_bt(edges, names)
    # bootstrap for intervals
    B = 40
    boots = np.zeros((B, len(names)))
    for b in range(B):
        samp = [edges[random.randrange(len(edges))] for _ in range(len(edges))]
        boots[b] = fit_bt(samp, names, iters=200)
    lo = np.percentile(boots, 2.5, axis=0); hi = np.percentile(boots, 97.5, axis=0)
    order = np.argsort(-theta)
    print(f"\n{'rank':>5}{'team':<26}{'BT strength':>13}{'95% interval':>22}{'games':>8}")
    for r, i in enumerate(order[:25], 1):
        print(f"{r:>5} {names[i][:25]:<25}{theta[i]:>13.3f}   [{lo[i]:>6.3f},{hi[i]:>6.3f}]{teams[names[i]]:>8}")
    if "Sam-wiz" in names:
        i = names.index("Sam-wiz")
        rank = int(np.where(order == i)[0][0]) + 1
        print(f"\n   US: rank {rank}/{len(names)}  strength {theta[i]:.3f}  "
              f"[{lo[i]:.3f},{hi[i]:.3f}]  ({teams['Sam-wiz']} games)")
        for opp in ("keiz", "Jesse Bullard", "Andrey Tikhomirov", "Crop Dusta"):
            if opp in names:
                j = names.index(opp)
                diff = theta[j] - theta[i]
                pw = 1 / (1 + math.exp(-(theta[i] - theta[j])))
                frac = float((boots[:, j] > boots[:, i]).mean())
                print(f"      vs {opp:<20} they are {diff:+.3f} above us  "
                      f"-> P(we beat them) = {pw:.1%}   P(they are truly better) = {frac:.0%}")
