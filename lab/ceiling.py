"""Why do our agents stall and fall back around 2.6k?

Two explanations fit the observed shape (climb to ~2.5-2.7k, then decay 200-300 as games accumulate),
and they imply completely different responses:

  A. MATCHMAKING CEILING. TrueSkill pairs by rating, so as we climb we meet stronger opponents. If
     our win rate crosses 50% somewhere near 2.6k, that IS our true strength and the peak was an
     overshoot from the fast early phase. Nothing is "going wrong" -- the agent simply cannot hold
     a rating it does not deserve, and the fix has to be a stronger agent.

  B. SOMETHING BREAKS against a particular kind of opponent found up there -- a specific counter, a
     timeout, a crash. That would be fixable directly.

The test that separates them: win rate against opponents grouped by THEIR leaderboard rating. Under
A the curve crosses 0.5 smoothly near our ceiling; under B there is a cliff, or an excess of
zero-bank / error games in one band.
"""
import collections
import glob
import gzip
import json
import os
import statistics
import subprocess
import sys

KA = ".venv/bin/kaggle"
SUBS = {
    "56394147": "pipe16 (live)",
    "56366726": "subJ_2945",
    "56366720": "subH2_v48",
    "56331236": "subH_v48",
}
BANDS = [(0, 2200), (2200, 2400), (2400, 2550), (2550, 2700), (2700, 2850), (2850, 9999)]


def owners():
    own = {}
    for sub, name in SUBS.items():
        r = subprocess.run([KA, "competitions", "episodes", sub, "-v"],
                           capture_output=True, text=True)
        for line in r.stdout.splitlines()[1:]:
            p = line.split(",")[0].strip()
            if p.isdigit():
                own[int(p)] = name
    return own


def load(own, lb):
    rows = []
    for p in glob.glob("mine/opp/*.json.gz"):
        try:
            d = json.load(gzip.open(p, "rt"))
        except Exception:
            continue
        t = d.get("teams") or []
        if "Sam-wiz" not in t or not d.get("rewards") or t[0] == t[1]:
            continue
        ep = int(d["episode_id"])
        if ep not in own:
            continue
        me = t.index("Sam-wiz")
        opp = t[1 - me]
        R = lb.get(opp)
        if R is None:
            continue
        a, b = d["rewards"][me], d["rewards"][1 - me]
        rows.append(dict(build=own[ep], opp=opp, R=R, ours=a, theirs=b, m=a - b,
                         res=1 if a > b else (0.5 if a == b else 0)))
    return rows


if __name__ == "__main__":
    lb = json.load(open("data/lb.json"))
    rows = load(owners(), lb)
    print(f"{len(rows)} episodes with a rated opponent\n")

    print("WIN RATE BY OPPONENT RATING BAND   value(n)")
    hdr = f"{'build':<16}" + "".join(f"{f'{lo}-{hi}':>13}" for lo, hi in BANDS)
    print(hdr)
    for build in list(SUBS.values()) + ["ALL"]:
        g0 = rows if build == "ALL" else [r for r in rows if r["build"] == build]
        if not g0:
            continue
        line = f"{build:<16}"
        for lo, hi in BANDS:
            g = [r for r in g0 if lo <= r["R"] < hi]
            line += (f"{statistics.mean(r['res'] for r in g):>7.2f}({len(g):>3})"
                     if g else f"{'--':>13}")
        print(line)

    print("\nMEAN MARGIN BY BAND (all builds)")
    line = f"{'ALL':<16}"
    for lo, hi in BANDS:
        g = [r for r in rows if lo <= r["R"] < hi]
        line += (f"{statistics.mean(r['m'] for r in g):>+13,.0f}" if g else f"{'--':>13}")
    print(line)

    print("\nFAILURE MODES BY BAND (zero bank = agent died; these would indicate B, not A)")
    line = f"{'zero-bank':<16}"
    for lo, hi in BANDS:
        g = [r for r in rows if lo <= r["R"] < hi]
        z = sum(1 for r in g if r["ours"] == 0)
        line += (f"{z:>6}/{len(g):<6}" if g else f"{'--':>13}")
    print(line)

    # where does the win-rate curve cross 0.5?
    pts = []
    for lo, hi in BANDS:
        g = [r for r in rows if lo <= r["R"] < hi]
        if len(g) >= 8:
            pts.append(((lo + hi) / 2, statistics.mean(r["res"] for r in g), len(g)))
    cross = None
    for (x0, y0, _), (x1, y1, _) in zip(pts, pts[1:]):
        if y0 >= 0.5 > y1:
            cross = x0 + (x1 - x0) * (y0 - 0.5) / (y0 - y1)
            break
    print(f"\nwin-rate curve crosses 0.50 at opponent rating ~{cross:.0f}" if cross
          else "\nwin-rate curve does not cross 0.50 in the sampled range")
    print("If that crossing sits near where our rating stalls, the stall is a matchmaking ceiling")
    print("(explanation A) and only a stronger agent moves it.")
