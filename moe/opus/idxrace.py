"""Index race on contested same-turn sells: our SELL index vs theirs, and the $ consequence."""
import json, sys, collections, statistics
sys.path.insert(0, 'moe/opus')
from ledger_eps import load_actions
from concurrent.futures import ProcessPoolExecutor
idx = {r['ep']: r for r in json.load(open('moe/opus/eps_index.json'))}
LED = {r['ep']: r for r in json.load(open('moe/opus/ledger_band.json'))}
pg = {g['ep']: g for g in json.load(open('moe/opus/pergame_band.json'))}

def sell_index(mkt, item):
    for i, o in enumerate(mkt[:10]):
        if isinstance(o, list) and len(o) >= 3 and o[0] == 'SELL' and o[1] == item:
            return i
    return None

def job(ep):
    row = idx[ep]; me = row['seat']; r = LED[ep]
    acts, _, _ = load_actions(row)
    by = collections.defaultdict(lambda: [[], []])
    for step, pl, op, item, price in r['fills']:
        if op == 'SELL':
            by[(step, item)][0 if pl == me else 1].append(price)
    out = []
    for (step, item), (po, pt) in by.items():
        if not (po and pt):
            continue
        a = acts[step + 1][me] if step + 1 < len(acts) else None
        b = acts[step + 1][1 - me] if step + 1 < len(acts) else None
        if not isinstance(a, dict) or not isinstance(b, dict):
            continue
        io = sell_index(a.get('market') or [], item); it = sell_index(b.get('market') or [], item)
        if io is None or it is None:
            continue
        # empty-slot count before our index
        emp_o = sum(1 for o in (a.get('market') or [])[:io] if not (isinstance(o, list) and o))
        emp_t = sum(1 for o in (b.get('market') or [])[:it] if not (isinstance(o, list) and o))
        out.append((step, item, io, it, len(po), len(pt), sum(po) / len(po), sum(pt) / len(pt), emp_o, emp_t))
    return ep, out

if __name__ == '__main__':
    eps = list(pg)
    with ProcessPoolExecutor(2) as ex:
        res = dict(ex.map(job, eps))
    json.dump(res, open('moe/opus/idxrace_band.json', 'w'))
    fam = lambda b: 'SIR' if b.startswith(('sir', 'L96')) else 'f55'
    for F in ('SIR', 'f55'):
        for lab, cond in [('loss', lambda g: g['gap'] < 0), ('win', lambda g: g['gap'] > 0)]:
            E = [ep for ep in eps if fam(pg[ep]['build']) == F and cond(pg[ep]) and abs(pg[ep]['gap']) < 3000]
            c = collections.Counter(); dol = collections.defaultdict(float); emp = collections.Counter()
            for ep in E:
                for step, item, io, it, uo, ut, po, pt, eo, et in res[ep]:
                    k = 'we_earlier' if io < it else 'they_earlier' if it < io else 'same_idx'
                    c[k] += 1
                    dol[k] += uo * po - ut * pt  # crude: our $ minus theirs on that turn-item
                    if eo: emp['our_empty_before'] += 1
                    if et: emp['their_empty_before'] += 1
            n = len(E)
            print(f"{F} whisker {lab} n={n}: " + ', '.join(f"{k} {c[k]/n:.1f}/g (${dol[k]/n:+.0f}/g)" for k in ('we_earlier', 'same_idx', 'they_earlier')) + f"  empties: {dict((k, round(v/n,1)) for k,v in emp.items())}")
