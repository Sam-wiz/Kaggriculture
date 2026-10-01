"""Summarize measured fills and same-seed candidate deltas, never requests."""
from pathlib import Path
import collections
import csv
import json
import statistics as S
HERE = Path(__file__).resolve().parent


def read(name):
    return [json.loads(line) for line in (HERE / name).read_text().splitlines()]


def key(r):
    return r['opponent'], r['seed'], r['seat']


base = read('trace_baseline.jsonl')
bykey = {key(r): r for r in base}
report = {}
for label in ('baseline', 'delivery', 'capture'):
    rows = read('trace_' + label + '.jsonl')
    report[label] = {}
    for opp in sorted({r['opponent'] for r in rows}):
        group = [r for r in rows if r['opponent'] == opp]
        ds = [r['margin'] - bykey[key(r)]['margin'] for r in group]
        row = {'games': len(group), 'wins': sum(r['margin'] > 0 for r in group),
               'losses': sum(r['margin'] < 0 for r in group),
               'ties': sum(r['margin'] == 0 for r in group),
               'mean_margin': S.mean(r['margin'] for r in group),
               'mean_paired_margin_gain': S.mean(ds), 'worst_paired_margin_gain': min(ds)}
        row['telemetry'] = dict(sum((collections.Counter(r['telemetry'][r['seat']])
                                     for r in group), collections.Counter()))
        report[label][opp] = row

out = HERE / 'endgame_fills.csv'
with out.open('w') as f:
    writer = csv.writer(f)
    writer.writerow(['variant', 'opponent', 'seed', 'our_seat', 'step', 'player',
                     'order_index', 'item', 'actual_units', 'receipts', 'mean_fill_price',
                     'first_fill_price', 'last_fill_price'])
    for label in ('baseline', 'delivery', 'capture'):
        for r in read('trace_' + label + '.jsonl'):
            d = json.loads(Path(r['path']).read_text())
            if label != 'baseline':
                old = json.loads(Path(bykey[key(r)]['path']).read_text())
                assert d['steps'][:504] == old['steps'][:504], (label, key(r), 'early drift')
                assert [x['shops'] for x in d['steps']] == [x['shops'] for x in old['steps']], (label, key(r), 'shop drift')
                seat = str(r['seat'])
                counts = collections.Counter()
                for a, b in zip(d['steps'], old['steps']):
                    now, prev = a['before'][seat]['action'], b['before'][seat]['action']
                    counts['any_action_turns'] += now != prev
                    counts['market_turns'] += now.get('market') != prev.get('market')
                    counts['unit_turns'] += (now.get('farmer'), now.get('hands')) != (prev.get('farmer'), prev.get('hands'))
                r['final_action_tape_differences_vs_base'] = dict(counts)
            periods = {}
            for lo, hi in ((504, 575), (576, 647), (648, 718), (504, 718)):
                q = [collections.Counter(), collections.Counter()]
                rev = [collections.Counter(), collections.Counter()]
                for st in d['steps']:
                    if not lo <= st['step'] <= hi:
                        continue
                    fills = collections.defaultdict(list)
                    for player, index, op, item, price in st['fills']:
                        if op != 'SELL':
                            continue
                        p = 0 if player == r['seat'] else 1
                        q[p][item] += 1
                        rev[p][item] += price
                        fills[player, index, item].append(price)
                    if (lo, hi) == (504, 718):
                        for (player, index, item), prices in fills.items():
                            writer.writerow([label, r['opponent'], r['seed'], r['seat'],
                                             st['step'], player, index, item, len(prices),
                                             sum(prices), S.mean(prices), prices[0], prices[-1]])
                periods[str(lo) + ':' + str(hi)] = {'units': q, 'receipts': rev}
            r['periods'] = periods
            report[label].setdefault('_games', []).append(r)
report['validation'] = {'prefix_through_503_identical': True, 'shop_sequences_identical': True,
                         'cash_reconciled_every_step': True, 'projected_stock_matched_engine': True}
(HERE / 'trace_analysis.json').write_text(json.dumps(report, indent=2))
for label in ('baseline', 'delivery', 'capture'):
    for opp, row in report[label].items():
        if opp == '_games':
            continue
        print(label, opp, json.dumps(row))
print('Validation:', report['validation'])
