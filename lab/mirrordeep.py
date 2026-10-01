"""Quantify the two leads the divergence scan surfaced: HIRE volume and endgame behaviour.

In the 59 near-clone games we lost (median 99.9% action identity, ~14 divergent turns each), the
single most common thing the opponent does on a divergent turn is issue a HIRE (448 occurrences),
and the divergence mass concentrates on day 0, day 2, and then days 28-29.

Both are cheap to price exactly, because we have both seats' full action streams:

  HIRE     total hires per game, per day, and the Fibonacci cost actually paid -- hires reset daily
           and cost fib(hires_today), so "more hires" and "more labour cost" are not the same claim
  ENDGAME  what each side does over days 28-29: units acting vs idle, and market volume, since the
           last two days are where unsold stock becomes worthless
"""
import collections
import glob
import gzip
import json
import statistics
import subprocess
import sys

KA = ".venv/bin/kaggle"
SUBS = {"56394147": "pipe16", "56394286": "metav4", "56366726": "subJ_2945",
        "56366720": "subH2_v48", "56331236": "subH_v48"}
MOVES = {"NORTH", "SOUTH", "EAST", "WEST"}


def fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


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


def seat_stats(acts, seat):
    hires_by_day = collections.Counter()
    hire_cost = 0
    sells = collections.Counter()
    late_acts = collections.Counter()
    late_units = 0
    for t, pair in enumerate(acts):
        a = pair[seat]
        if not isinstance(a, dict):
            continue
        day = t // 24
        for o in (a.get("market") or []):
            if not o:
                continue
            if o[0] == "HIRE":
                hire_cost += fib(hires_by_day[day])
                hires_by_day[day] += 1
            elif o[0] == "SELL" and len(o) > 2:
                sells[day] += int(o[2])
        if day >= 28:
            for u in [a.get("farmer")] + list(a.get("hands") or []):
                if not u:
                    continue
                late_units += 1
                op = u[0] if isinstance(u, list) else str(u)
                late_acts["PASS" if op == "PASS" else
                          ("MOVE" if op in MOVES else "productive")] += 1
    return dict(hires=sum(hires_by_day.values()), hire_cost=hire_cost,
                hires_by_day=hires_by_day, sells=sells,
                late=late_acts, late_units=late_units)


if __name__ == "__main__":
    own = owners()
    lost, won = [], []
    for p in glob.glob("mine/opp/*.json.gz"):
        try:
            d = json.load(gzip.open(p, "rt"))
        except Exception:
            continue
        t = d.get("teams") or []
        if "Sam-wiz" not in t or not d.get("rewards") or t[0] == t[1]:
            continue
        if int(d["episode_id"]) not in own:
            continue
        acts = d.get("actions") or []
        if not acts:
            continue
        me = t.index("Sam-wiz")
        same = sum(1 for a in acts if a[me] == a[1 - me]) / len(acts)
        if same < 0.90:
            continue
        rec = dict(us=seat_stats(acts, me), them=seat_stats(acts, 1 - me),
                   margin=d["rewards"][me] - d["rewards"][1 - me])
        (won if rec["margin"] > 0 else lost).append(rec)

    for label, g in (("LOST (n=%d)" % len(lost), lost), ("WON (n=%d)" % len(won), won)):
        if not g:
            continue
        print(f"\n=== {label} ===")
        for side in ("us", "them"):
            h = statistics.mean(r[side]["hires"] for r in g)
            c = statistics.mean(r[side]["hire_cost"] for r in g)
            s = statistics.mean(sum(r[side]["sells"].values()) for r in g)
            lu = statistics.mean(r[side]["late_units"] for r in g)
            la = collections.Counter()
            for r in g:
                la.update(r[side]["late"])
            tot = sum(la.values()) or 1
            print(f"  {side:<6} hires/game {h:>6.1f}   labour $ {c:>8,.0f}   "
                  f"sell units {s:>7.0f}   days28-29 unit-turns {lu:>6.0f}  "
                  f"(PASS {la['PASS']/tot:>5.1%}  MOVE {la['MOVE']/tot:>5.1%}  "
                  f"prod {la['productive']/tot:>5.1%})")
        dh = statistics.mean(r["them"]["hires"] - r["us"]["hires"] for r in g)
        dc = statistics.mean(r["them"]["hire_cost"] - r["us"]["hire_cost"] for r in g)
        ds = statistics.mean(sum(r["them"]["sells"].values()) - sum(r["us"]["sells"].values())
                             for r in g)
        print(f"  DELTA  hires {dh:+.1f}   labour ${dc:+,.0f}   sell units {ds:+.0f}")

    if lost:
        print("\nhires by day, LOST games (ours vs theirs):")
        for day in range(0, 30):
            u = statistics.mean(r["us"]["hires_by_day"].get(day, 0) for r in lost)
            t2 = statistics.mean(r["them"]["hires_by_day"].get(day, 0) for r in lost)
            if u or t2:
                flag = "  <--" if abs(t2 - u) >= 0.4 else ""
                print(f"   day {day:>2}:  us {u:>5.1f}   them {t2:>5.1f}   "
                      f"delta {t2-u:>+5.1f}{flag}")
