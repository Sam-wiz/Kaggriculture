"""Estimate our TRUE rating from the games we have actually played, given opponent ratings.

The ladder's own number is a sequential estimate that starts every submission at 600 and crawls;
after 50 games it is still mostly prior. But we know each opponent's converged leaderboard rating,
so our strength is a one-parameter fit -- exactly the Bradley-Terry idea, and far tighter than the
ladder's own estimate at the same number of games.

    P(we beat an opponent rated R) = Phi( (theta - R) / (sqrt(2)*beta) )
"""
import gzip, glob, json, math, os, subprocess, sys

KA = ".venv/bin/kaggle"
SUBS = {56053687: "router_slot", 56051487: "router2", 56050947: "router", 56039245: "sub_final"}
BETA = 200.0


def _phi(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def loglik(theta, games):
    s = 0.0
    for R, res in games:
        p = min(max(_phi((theta - R) / (math.sqrt(2) * BETA)), 1e-9), 1 - 1e-9)
        s += res * math.log(p) + (1 - res) * math.log(1 - p)
    return s


def fit(games):
    lo, hi = 500.0, 4500.0
    for _ in range(200):
        m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
        if loglik(m1, games) < loglik(m2, games):
            lo = m1
        else:
            hi = m2
    th = (lo + hi) / 2
    best = loglik(th, games)
    ci = [t for t in range(500, 4500, 2) if loglik(t, games) > best - 1.92]
    return th, (min(ci) if ci else th), (max(ci) if ci else th)


if __name__ == "__main__":
    own = {}
    for s, n in SUBS.items():
        r = subprocess.run([KA, "competitions", "episodes", str(s), "-v"],
                           capture_output=True, text=True)
        for l in r.stdout.splitlines()[1:]:
            p = l.split(",")[0].strip()
            if p.isdigit():
                own[int(p)] = n
    LB = json.load(open("data/lb.json"))
    G = {}
    for p in glob.glob("mine/opp/*.json.gz"):
        d = json.load(gzip.open(p, "rt"))
        t = d["teams"]
        if "Sam-wiz" not in t or not d.get("rewards"):
            continue
        ep = int(d["episode_id"])
        if ep not in own or t[0] == t[1]:
            continue
        me = t.index("Sam-wiz")
        R = LB.get(t[1 - me])
        if R is None:
            continue
        m = d["rewards"][me] - d["rewards"][1 - me]
        G.setdefault(own[ep], []).append((R, 1.0 if m > 0 else (0.5 if m == 0 else 0.0)))
    G["ROUTER FAMILY"] = G.get("router", []) + G.get("router2", []) + G.get("router_slot", [])
    print(f"beta = {BETA:.0f}   (P(win) = Phi((theta - R_opp)/(sqrt(2)*beta)))\n")
    print(f"{'build':<15}{'games':>6}{'score':>8}{'ladder now':>12}{'FITTED theta':>14}{'95% CI':>18}")
    live = {"router": 2324.9, "router2": 2385.0, "router_slot": 1762.8, "sub_final": 2421.8,
            "ROUTER FAMILY": float("nan")}
    for k in ["sub_final", "router", "router2", "router_slot", "ROUTER FAMILY"]:
        g = G.get(k) or []
        if len(g) < 5:
            continue
        th, lo, hi = fit(g)
        sc = sum(r for _, r in g) / len(g)
        ln = live.get(k)
        lns = "--" if ln != ln else f"{ln:.0f}"
        print(f"{k:<15}{len(g):>6}{sc:>8.3f}{lns:>12}{th:>14.0f}{f'[{lo}, {hi}]':>18}")
    print(f"\ntop-10 cutoff 2774   rank20 2727   rank50 2634   rank100 2555")
