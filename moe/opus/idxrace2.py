"""Same-index contested sells: who fills more units, and is the short side order-limited or stock-limited."""
import json, sys, collections
sys.path.insert(0, 'moe/opus')
from ledger_eps import load_actions
from concurrent.futures import ProcessPoolExecutor
idx = {r['ep']: r for r in json.load(open('moe/opus/eps_index.json'))}
LED = {r['ep']: r for r in json.load(open('moe/opus/ledger_band.json'))}
pg = {g['ep']: g for g in json.load(open('moe/opus/pergame_band.json'))}

def qty(mkt, item):
    return sum(int(o[2]) for o in mkt[:10] if isinstance(o, list) and len(o) >= 3 and o[0] == 'SELL' and o[1] == item)

def job(ep):
    row = idx[ep]; me = row['seat']; r = LED[ep]
    acts, _, _ = load_actions(row)
    by = collections.defaultdict(lambda: [[], []])
    for step, pl, op, item, price in r['fills']:
        if op == 'SELL':
            by[(step, item)][0 if pl == me else 1].append(price)
    agg = collections.defaultdict(lambda: collections.defaultdict(float))
    for (step, item), (po, pt) in by.items():
        a = acts[step + 1][me]; b = acts[step + 1][1 - me]
        qo = qty(a.get('market') or [], item); qt = qty(b.get('market') or [], item)
        A = agg[item]
        if po and pt:
            A['n'] += 1; A['uo'] += len(po); A['ut'] += len(pt)
            if len(po) < len(pt):
                A['short_o'] += 1
                A['short_o_orderlim'] += (len(po) >= qo)   # we filled everything we ordered
                A['short_o_units'] += len(pt) - len(po)
            elif len(pt) < len(po):
                A['short_t'] += 1
                A['short_t_orderlim'] += (len(pt) >= qt)
                A['short_t_units'] += len(po) - len(pt)
    return ep, {k: dict(v) for k, v in agg.items()}

if __name__ == '__main__':
    eps = [ep for ep in pg if abs(pg[ep]['gap']) < 3000 and abs(pg[ep]['TOMATO']) <= 500]
    with ProcessPoolExecutor(2) as ex:
        res = dict(ex.map(job, eps))
    fam = lambda b: 'SIR' if b.startswith(('sir', 'L96')) else 'f55'
    for F in ('SIR', 'f55'):
        E = [ep for ep in eps if fam(pg[ep]['build']) == F]
        n = len(E)
        print(f"\n{F} whisker n={n}   per game: contested turns, units ours/theirs, turns we're short (order-limited), units short; turns they're short (order-limited), units")
        for item in ['WHEAT', 'CARROT', 'STRAWBERRY', 'EGG', 'MILK', 'WOOL', 'FERTILIZER', 'MELON', 'TOMATO']:
            T = collections.defaultdict(float)
            for ep in E:
                for k, v in res[ep].get(item, {}).items():
                    T[k] += v
            if not T['n']: continue
            print(f"  {item:11s} turns {T['n']/n:5.1f} u {T['uo']/n:6.1f}/{T['ut']/n:6.1f} | we short {T['short_o']/n:4.1f} ({T['short_o_orderlim']/max(1,T['short_o']):.0%} order-lim) -{T['short_o_units']/n:5.1f}u | they short {T['short_t']/n:4.1f} ({T['short_t_orderlim']/max(1,T['short_t']):.0%} order-lim) -{T['short_t_units']/n:5.1f}u")
