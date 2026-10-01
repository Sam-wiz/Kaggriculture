"""Calibrate the rating scale against an agent whose true rating we already know, then refit.

`btrating.py` assumed beta=200. That assumption drives every number it produces, so it has to be
checked. sub_final is converged -- 148 episodes and drifting *down* -- so its true strength is its
displayed 2421.8. The right beta is the one for which fitting its own game record reproduces that.
Then the same beta is applied to the router family.
"""
import glob
import gzip
import json
import subprocess
import sys

import btrating as B

KA = ".venv/bin/kaggle"
TRUE_SUB_FINAL = 2421.8
LADDER = {"sub_final": 2421.8, "router": 2324.9, "router2": 2385.0, "router_slot": 1762.8}


def collect():
    own = {}
    for s, n in B.SUBS.items():
        r = subprocess.run([KA, "competitions", "episodes", str(s), "-v"],
                           capture_output=True, text=True)
        for line in r.stdout.splitlines()[1:]:
            p = line.split(",")[0].strip()
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
    G["FAMILY"] = G.get("router", []) + G.get("router2", []) + G.get("router_slot", [])
    return G


if __name__ == "__main__":
    G = collect()
    print("Calibrating the scale against sub_final, whose true rating we know (2421.8):\n")
    print(f"{'beta':>6}{'fitted theta(sub_final)':>26}{'error':>10}")
    best = None
    for beta in range(60, 500, 10):
        B.BETA = float(beta)
        th, _, _ = B.fit(G["sub_final"])
        e = th - TRUE_SUB_FINAL
        if best is None or abs(e) < abs(best[1]):
            best = (beta, e, th)
        if beta % 60 == 0 or abs(e) < 30:
            print(f"{beta:>6}{th:>26.0f}{e:>+10.0f}")
    beta = best[0]
    print(f"\n  calibrated beta = {beta}   (reproduces {best[2]:.0f} vs true 2421.8)\n")

    B.BETA = float(beta)
    print(f"{'build':<13}{'games':>6}{'score':>7}{'meanOpp':>9}{'ladder':>8}{'FITTED':>8}{'95% CI':>16}")
    for k in ["sub_final", "router", "router2", "router_slot", "FAMILY"]:
        g = G.get(k) or []
        if len(g) < 5:
            continue
        th, lo, hi = B.fit(g)
        mo = sum(R for R, _ in g) / len(g)
        lad = LADDER.get(k)
        print(f"{k:<13}{len(g):>6}{sum(r for _, r in g)/len(g):>7.3f}{mo:>9.0f}"
              f"{(f'{lad:.0f}' if lad else '--'):>8}{th:>8.0f}{f'[{lo},{hi}]':>16}")
    print("\ntop-10 cutoff 2774   rank20 2727   rank50 2634   rank100 2555")
