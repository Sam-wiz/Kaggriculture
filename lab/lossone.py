"""Day-by-day autopsy of a single lost episode."""
import gzip
import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))


def owned(farm_tiles):
    """tiles is the 10x10 board; count the cells this player actually owns."""
    n = 0
    for row in farm_tiles or []:
        for c in row if isinstance(row, list) else []:
            if c:
                n += 1
    return n


def main(ep):
    d = json.load(gzip.open(os.path.join(ROOT, "mine/loss/%s.json.gz" % ep), "rt"))
    me = d["our_seat"]
    tr = d["trace"]
    acts = d["actions"]
    print(f"episode {d['episode_id']}  seed {d['seed']}  {d['teams']}  rewards {d['rewards']}")
    print(f"we are seat {me}\n")
    print(f"{'day':>4}{'ourMoney':>10}{'theirMoney':>12}{'margin':>10}"
          f"{'ourShed':>9}{'thShed':>8}{'ourHnd':>8}{'thHnd':>7}"
          f"{'pxSTRAW':>9}{'pxMILK':>8}{'pxWOOL':>8}{'shops':>7}")
    for dd in range(30):
        i = min(len(tr) - 1, dd * 24 + 23)
        r = tr[i]
        us, th = r["money"][me], r["money"][1 - me]
        sh_u = sum(r["shed"][me].values()) if r["shed"][me] else 0
        sh_t = sum(r["shed"][1 - me].values()) if r["shed"][1 - me] else 0
        print(f"{dd:>4}{us:>10,.0f}{th:>12,.0f}{us-th:>+10,.0f}{sh_u:>9}{sh_t:>8}"
              f"{r['hands'][me]:>8}{r['hands'][1-me]:>7}"
              f"{(r['px'].get('STRAWBERRY') or 0):>9.0f}{(r['px'].get('MILK') or 0):>8.0f}"
              f"{(r['px'].get('WOOL') or 0):>8.0f}{len(r['shops']):>7}")
    # what each side sold, by product, from their own order stream
    print("\nSELL ORDERS placed (qty, not fills) by product:")
    tot = [{}, {}]
    for a in acts:
        for s in (0, 1):
            for o in ((a[s] or {}).get("market") or []):
                if o and o[0] == "SELL":
                    tot[s][o[1]] = tot[s].get(o[1], 0) + int(o[2])
    keys = sorted(set(tot[0]) | set(tot[1]))
    print(f"{'product':<14}{'ours':>8}{'theirs':>9}")
    for k in keys:
        print(f"{k:<14}{tot[me].get(k,0):>8}{tot[1-me].get(k,0):>9}")
    # last-3-day income
    n = len(tr) - 1
    for lab, a, b in (("days 0-11", 0, 11 * 24), ("days 12-23", 11 * 24, 23 * 24),
                      ("days 24-29", 23 * 24, n)):
        du = tr[b]["money"][me] - tr[a]["money"][me]
        dt = tr[b]["money"][1 - me] - tr[a]["money"][1 - me]
        print(f"  income {lab:<12} ours {du:>+10,.0f}   theirs {dt:>+10,.0f}   delta {du-dt:>+10,.0f}")


if __name__ == "__main__":
    main(sys.argv[1])
