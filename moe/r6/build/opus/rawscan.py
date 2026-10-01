"""r6 opus: raw action-tape scan of mine/top10 (09-23..25, 1,773 eps) -> rawscan.pkl
Per seat: team/opp/date/shops, per-step unit-op hash (720 int32) and market-list hash, op counters,
market style (orders/step, SELL order sizes, same-step buy+sell of the same item), premium SELL order
hours, and same-step same-product SELL collisions with the opponent.
usage: rawscan.py [WORKERS]
"""
import collections, glob, gzip, json, os, pickle, sys, zlib
from concurrent.futures import ProcessPoolExecutor

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
PREM = ("STRAWBERRY", "MELON", "MILK", "WOOL", "EGG", "TOMATO", "CARROT", "WHEAT", "FERTILIZER")


def h(s): return zlib.crc32(s.encode()) & 0x7FFFFFFF


def job(path):
    d = json.load(gzip.open(path, "rt"))
    A = d["actions"]; T = len(A)
    seats = []
    sells = [[set() for _ in range(T)] for _ in range(2)]
    for s in range(2):
        uh, mh = [], []
        ops = collections.Counter(); mops = collections.Counter()
        nord = 0; nsteps = 0; sell_sz = []; churn = 0; hours = collections.defaultdict(collections.Counter)
        sell_units_by_hour = collections.defaultdict(collections.Counter)
        for t in range(1, T):
            a = A[t][s]
            if not isinstance(a, dict): uh.append(0); mh.append(0); continue
            units = [a.get("farmer")] + list(a.get("hands") or [])
            uh.append(h(json.dumps(units))); mk = a.get("market") or []
            mh.append(h(json.dumps(mk)))
            for u in units: ops[(u or ["PASS"])[0]] += 1
            nsteps += 1; nord += len(mk)
            bought = set(); sold = set()
            for o in mk:
                if not isinstance(o, list) or not o: mops["BAD"] += 1; continue
                mops[o[0]] += 1
                if o[0] == "SELL" and len(o) >= 3:
                    try: n = int(o[2])
                    except Exception: n = 0
                    if n > 0:
                        sold.add(o[1]); sell_sz.append(n)
                        hr = (t - 1) % 24
                        hours[o[1]][hr] += 1; sell_units_by_hour[o[1]][hr] += n
                elif o[0] == "BUY_PRODUCT" and len(o) >= 2: bought.add(o[1])
            churn += len(bought & sold)
            sells[s][t] = sold
        seats.append(dict(team=d["teams"][s], opp=d["teams"][1 - s], ep=d["episode_id"], date=d.get("date"), seat=s,
                          shops=d.get("shops"), shops150=d.get("shops150"), bank=d["rewards"][s], obank=d["rewards"][1 - s],
                          uh=uh, mh=mh, ops=dict(ops), mops=dict(mops), ord_per_step=nord / max(1, nsteps),
                          sell_orders=len(sell_sz), sell_sz_mean=(sum(sell_sz) / len(sell_sz) if sell_sz else 0),
                          sell_sz1=(sum(1 for x in sell_sz if x == 1) / len(sell_sz) if sell_sz else 0),
                          churn_steps=churn, hours={k: dict(v) for k, v in hours.items()},
                          uhours={k: dict(v) for k, v in sell_units_by_hour.items()}))
    for s in range(2):
        col = {}
        for p in PREM:
            own = [t for t in range(1, T) if p in sells[s][t]]
            both = sum(1 for t in own if p in sells[1 - s][t])
            # "front-run" = opp sold p in the previous 1-3 steps
            pre = sum(1 for t in own if any(p in sells[1 - s][u] for u in range(max(1, t - 3), t)))
            col[p] = (len(own), both, pre)
        seats[s]["coll"] = col
    return seats


if __name__ == "__main__":
    W = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    paths = sorted(glob.glob(ROOT + "/mine/top10/*.json.gz"))
    out = []
    with ProcessPoolExecutor(max_workers=W) as ex:
        for i, r in enumerate(ex.map(job, paths, chunksize=8), 1):
            out.extend(r)
            if i % 400 == 0: print(i, flush=True)
    pickle.dump(out, open(ROOT + "/moe/r6/build/opus/rawscan.pkl", "wb"))
    print("seats", len(out))
