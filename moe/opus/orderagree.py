"""On turns where both lists SELL >=2 common items, does the opponent order them like we do?"""
import json, sys, collections
sys.path.insert(0, 'moe/opus')
from ledger_eps import load_actions
from concurrent.futures import ProcessPoolExecutor
idx = {r['ep']: r for r in json.load(open('moe/opus/eps_index.json'))}
pg = {g['ep']: g for g in json.load(open('moe/opus/pergame_band.json'))}

def sells(m):
    return [o[1] for o in (m or [])[:10] if isinstance(o, list) and len(o) >= 3 and o[0] == 'SELL']

def job(ep):
    row = idx[ep]; me = row['seat']
    acts, _, _ = load_actions(row)
    c = collections.Counter()
    for t in range(1, len(acts)):
        a, b = acts[t][me], acts[t][1 - me]
        if not isinstance(a, dict) or not isinstance(b, dict): continue
        sa, sb = sells(a.get('market')), sells(b.get('market'))
        com = [x for x in sa if x in sb]
        if len(com) < 2: continue
        c['turns'] += 1
        ob = [x for x in sb if x in com]
        c['same_rel_order'] += (com == ob)
        c['same_first'] += (com[0] == ob[0])
        # would opponent-first-item-last rotation of our list have been possible?
    return ep, dict(c)

if __name__ == '__main__':
    eps = [ep for ep in pg if abs(pg[ep]['gap']) < 3000]
    with ProcessPoolExecutor(2) as ex:
        res = dict(ex.map(job, eps))
    fam = lambda b: 'SIR' if b.startswith(('sir', 'L96')) else 'f55'
    for F in ('SIR', 'f55'):
        E = [ep for ep in eps if fam(pg[ep]['build']) == F]
        T = collections.Counter()
        for ep in E: T.update(res[ep])
        print(f"{F} n={len(E)}: multi-item contested turns/game {T['turns']/len(E):.1f}; opp same relative order {T['same_rel_order']/max(1,T['turns']):.0%}; same first item {T['same_first']/max(1,T['turns']):.0%}")
    # distribution per game of agreement for SIR builds
    ag = sorted(round(res[ep].get('same_rel_order', 0) / max(1, res[ep].get('turns', 0)), 2) for ep in eps if fam(pg[ep]['build']) == 'SIR')
    print('SIR per-game agreement deciles:', ag[::max(1, len(ag)//10)])
