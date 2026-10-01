"""Recover the gate's omitted i index from its deterministic job order."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import itertools
import json
import statistics as S
import collections
import random
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from moe.gate import POOL


def recover(tag, extra, start=906, count=24):
    agents = POOL + extra
    pairs = [(i, j) for i, j in itertools.combinations(range(len(agents)), 2)
             if j >= len(POOL)]
    seeds = [r['seed'] for r in json.loads((ROOT/'data/seedindex_900000_1400.json').read_text())][start:start+count]
    expected = [(i, j, seed, seat) for i, j in pairs for seed in seeds for seat in (0, 1)]
    raw = json.loads((ROOT / ('moe/codex/gate_' + tag + '.json')).read_text())
    assert len(expected) == len(raw)
    records = []
    for (i, j, seed, seat), (jj, ss, sw, margin) in zip(expected, raw):
        assert (j, seed, seat) == (jj, ss, sw)
        records.append({'a': agents[i][0], 'b': agents[j][0], 'seed': seed,
                        'swapped': seat, 'margin_a': margin})
    (ROOT / ('moe/codex/gate_' + tag + '_records.jsonl')).write_text(
        ''.join(json.dumps(r)+'\n' for r in records))
    return records


def view(records, name):
    out = {}
    for r in records:
        if r['a'] == name:
            opp, seat, margin = r['b'], int(r['swapped']), r['margin_a']
        elif r['b'] == name:
            opp, seat = r['a'], 1-int(r['swapped'])
            margin = None if r['margin_a'] is None else -r['margin_a']
        else:
            continue
        out[opp, r['seed'], seat] = margin
    return out


def stats(values):
    return dict(n=len(values), wins=sum(x>0 for x in values), ties=sum(x==0 for x in values),
                losses=sum(x<0 for x in values), win_rate=S.mean(1 if x>0 else .5 if x==0 else 0 for x in values),
                mean_margin=S.mean(values), worst_margin=min(values))


def bootstrap(seed_values):
    rng = random.Random(984230)
    values = list(seed_values)
    means = sorted(S.mean(rng.choices(values, k=len(values))) for _ in range(10000))
    return [means[250], means[9749]]


if __name__ == '__main__':
    candidates = recover('candidates', [('delivery','moe/codex/cand_delivery.py'), ('capture','moe/codex/cand_capture.py')])
    controls = recover('controls', [('sir_control','subV_sir2.py'), ('f55_control','subV2_f55rec.py')])
    all_records = candidates + controls
    assert all(r['margin_a'] is not None for r in all_records), 'failed games'
    views = {name:view(all_records,name) for name in ('delivery','capture','sir_control','f55_control')}
    report = {}
    rest = {n for n,p in POOL[2:]}
    for name, v in views.items():
        rows = {}
        for opp in sorted({k[0] for k in v}):
            vals = [x for k,x in v.items() if k[0] == opp]
            rows[opp] = stats(vals)
            if name in ('delivery','capture') and opp in {n for n,p in POOL}:
                pairs = {k:x-views['sir_control'][k] for k,x in v.items() if k[0]==opp}
                block = collections.defaultdict(list)
                for (o,seed,seat), delta in pairs.items():
                    block[seed].append(delta)
                rows[opp]['paired_gain_vs_sir'] = S.mean(pairs.values())
                rows[opp]['paired_gain_seed_bootstrap_95'] = bootstrap(S.mean(x) for x in block.values())
                rows[opp]['worst_paired_gain'] = min(pairs.values())
        report[name] = {'matchups':rows, 'rest6_mean_win_rate':S.mean(rows[n]['win_rate'] for n in rest),
                         'rest6_mean_margin':S.mean(rows[n]['mean_margin'] for n in rest)}
    stronger = max(('sir_control', 'f55_control'), key=lambda n: report[n]['rest6_mean_win_rate'])
    win = lambda m: 1 if m > 0 else .5 if m == 0 else 0
    for name in ('delivery', 'capture'):
        block_margin = collections.defaultdict(list)
        block_win = collections.defaultdict(list)
        for k, margin in views[name].items():
            opp, seed, seat = k
            if opp not in rest:
                continue
            ref = views[stronger][k]
            block_margin[seed].append(margin-ref)
            block_win[seed].append(win(margin)-win(ref))
        md = [S.mean(v) for v in block_margin.values()]
        wd = [S.mean(v) for v in block_win.values()]
        report[name]['rest6_paired_vs_stronger'] = {
            'control':stronger, 'seeds':len(md), 'games':sum(map(len,block_margin.values())),
            'mean_margin_gain':S.mean(md), 'margin_seed_bootstrap_95':bootstrap(md),
            'win_rate_gain':S.mean(wd), 'win_rate_seed_bootstrap_95':bootstrap(wd)}
    for name in views:
        print(name, json.dumps(report[name], indent=2))
    (ROOT/'moe/codex/gate_analysis.json').write_text(json.dumps(report,indent=2))
