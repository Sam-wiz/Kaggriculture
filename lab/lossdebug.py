"""Why we lost: read the per-turn traces and classify every defeat.

Terminal money is the score, so the question for each loss is *when* the margin went negative and
what the two farms looked like on either side of that point. Three shapes matter and they need
different fixes:

  blown lead   - we led for most of the game and lost it late (an endgame/selling problem)
  never ahead  - behind from early on (a build/economy problem)
  late collapse- ahead at the last day and still lost (a liquidation problem)
"""
import glob
import gzip
import json
import os
import statistics
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(ROOT, "mine/loss")


def load(path):
    d = json.load(gzip.open(path, "rt"))
    me = d["our_seat"]
    tr = d["trace"]
    if not tr:
        return None
    m = [r["money"][me] - r["money"][1 - me] for r in tr]
    d["m"] = m
    d["me"] = me
    return d


def shape(d):
    m = d["m"]
    n = len(m)
    lead = sum(1 for x in m if x > 0) / n
    # last turn at which the sign flipped for good
    last_pos = max((i for i, x in enumerate(m) if x > 0), default=-1)
    if lead < 0.25:
        return "never ahead", lead, last_pos
    if last_pos >= n - 25:
        return "late collapse", lead, last_pos
    return "blown lead", lead, last_pos


def summarize(d):
    me, tr, m = d["me"], d["trace"], d["m"]
    sh, lead, last_pos = shape(d)
    fin = tr[-1]
    def shedn(r, i):
        return sum(r["shed"][i].values()) if r["shed"][i] else 0
    return dict(
        ep=d["episode_id"], opp=d["teams"][1 - me], final=m[-1], shape=sh,
        lead=lead, flip_day=last_pos // 24 if last_pos >= 0 else -1,
        tiles=[tr[-1]["tiles"][me], tr[-1]["tiles"][1 - me]],
        peak_lead=max(m), worst=min(m),
        shed_end=[shedn(fin, me), shedn(fin, 1 - me)],
        m_day=[m[min(len(m) - 1, dd * 24)] for dd in range(0, 30, 3)],
    )


if __name__ == "__main__":
    fs = sorted(glob.glob(os.path.join(DIR, "*.json.gz")))
    recs = [summarize(d) for d in (load(f) for f in fs) if d]
    if not recs:
        sys.exit("no traces yet")
    print(f"{len(recs)} losses traced\n")
    by = {}
    for r in recs:
        by.setdefault(r["shape"], []).append(r)
    print(f"{'shape':<16}{'n':>4}{'medFinal':>11}{'medPeakLead':>13}{'medFlipDay':>12}")
    for k, g in sorted(by.items(), key=lambda kv: -len(kv[1])):
        print(f"{k:<16}{len(g):>4}{statistics.median(r['final'] for r in g):>+11,.0f}"
              f"{statistics.median(r['peak_lead'] for r in g):>+13,.0f}"
              f"{statistics.median(r['flip_day'] for r in g):>12.0f}")
    print()
    print("MEAN MARGIN BY DAY, per shape  (positive = we lead)")
    hdr = "".join(f"{'d'+str(dd):>8}" for dd in range(0, 30, 3))
    print(f"{'shape':<16}{hdr}")
    for k, g in sorted(by.items(), key=lambda kv: -len(kv[1])):
        row = "".join(f"{statistics.median(r['m_day'][i] for r in g):>+8,.0f}"
                      for i in range(len(g[0]["m_day"])))
        print(f"{k:<16}{row}")
    print()
    print("WORST 15")
    print(f"{'ep':<11}{'opponent':<22}{'final':>9}{'shape':<15}{'peak':>8}{'flipD':>6}"
          f"{'tiles us/them':>15}{'shed us/them':>14}")
    for r in sorted(recs, key=lambda r: r["final"])[:15]:
        tiles = "%d/%d" % (r["tiles"][0], r["tiles"][1])
        shed = "%d/%d" % (r["shed_end"][0], r["shed_end"][1])
        print(f"{r['ep']:<11}{r['opp'][:20]:<22}{r['final']:>+9,.0f}{r['shape']:<15}"
              f"{r['peak_lead']:>+8,.0f}{r['flip_day']:>6}{tiles:>15}{shed:>14}")
