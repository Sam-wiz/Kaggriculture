"""Diff our vs opponent action streams in band games: unit-op identity, market identity, divergence types."""
import json, sys, collections, statistics
sys.path.insert(0, 'moe/opus')
from ledger_eps import load_actions
from concurrent.futures import ProcessPoolExecutor
idx = {r['ep']: r for r in json.load(open('moe/opus/eps_index.json'))}
pg = {g['ep']: g for g in json.load(open('moe/opus/pergame_band.json'))}

def job(ep):
    row = idx[ep]; me = row['seat']
    acts, seed, rew = load_actions(row)
    unit_same = mkt_same = 0; n = 0
    div = collections.Counter()
    for t in range(1, len(acts)):
        a, b = acts[t][me], acts[t][1 - me]
        if not isinstance(a, dict) or not isinstance(b, dict):
            continue
        n += 1
        ua = [a.get('farmer')] + list(a.get('hands') or []); ub = [b.get('farmer')] + list(b.get('hands') or [])
        unit_same += ua == ub
        ma = a.get('market') or []; mb = b.get('market') or []
        if ma == mb:
            mkt_same += 1; continue
        # sells by item
        sa = collections.Counter(); sb = collections.Counter()
        for o in ma:
            if isinstance(o, list) and o and o[0] == 'SELL' and len(o) >= 3: sa[o[1]] += int(o[2])
        for o in mb:
            if isinstance(o, list) and o and o[0] == 'SELL' and len(o) >= 3: sb[o[1]] += int(o[2])
        for it in set(sa) | set(sb):
            if sa[it] and not sb[it]: div['we_sell_only:' + it] += 1
            elif sb[it] and not sa[it]: div['they_sell_only:' + it] += 1
            elif sa[it] != sb[it]: div['qty_diff:' + it] += 1
        ka = [tuple(o[:2]) for o in ma if isinstance(o, list) and o]; kb = [tuple(o[:2]) for o in mb if isinstance(o, list) and o]
        if sorted(map(str, ka)) == sorted(map(str, kb)) and ka != kb:
            div['same_set_diff_order'] += 1
        if len(ma) != len(mb):
            div['len_diff'] += 1
        # non-sell differences
        oa = collections.Counter(str(o[:2]) for o in ma if isinstance(o, list) and o and o[0] != 'SELL')
        ob = collections.Counter(str(o[:2]) for o in mb if isinstance(o, list) and o and o[0] != 'SELL')
        if oa != ob: div['nonsell_diff'] += 1
    return dict(ep=ep, unit_same=unit_same / n, mkt_same=mkt_same / n, div=dict(div))

if __name__ == '__main__':
    eps = [ep for ep, g in pg.items()]
    with ProcessPoolExecutor(2) as ex:
        out = list(ex.map(job, eps))
    json.dump(out, open('moe/opus/mktdiff_band.json', 'w'))
    print('done', len(out))
