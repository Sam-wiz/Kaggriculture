"""Per-game channel gaps (ours - theirs, $ net incl. matching buys) for band episodes."""
import json, sys, collections, statistics
sys.path.insert(0, 'moe/opus')
from decompose import ledger, PH
L = [r for r in json.load(open(sys.argv[1] if len(sys.argv) > 1 else 'moe/opus/ledger_band.json')) if 'err' not in r]
CH = ['WHEAT', 'CARROT', 'TOMATO', 'STRAWBERRY', 'MELON', 'EGG', 'MILK', 'WOOL', 'FERTILIZER']
rows = []
for r in L:
    me = r['seat']
    mo, uo, po, _, _ = ledger(r, me); mt, ut, pt, _, _ = ledger(r, 1 - me)
    g = {}
    for c in CH:
        g[c] = sum(v for k, v in mo.items() if k[1] == c and k[0] in ('SELL', 'BUY_PRODUCT')) - \
               sum(v for k, v in mt.items() if k[1] == c and k[0] in ('SELL', 'BUY_PRODUCT'))
    g['other'] = sum(v for k, v in mo.items() if k[0] in ('BUY_SEED', 'BUY_ANIMAL', 'HIRE', 'BUY_LAND')) - \
                 sum(v for k, v in mt.items() if k[0] in ('BUY_SEED', 'BUY_ANIMAL', 'HIRE', 'BUY_LAND'))
    g['tom_u'] = (sum(v for k, v in uo.items() if k[:2] == ('SELL', 'TOMATO')), sum(v for k, v in ut.items() if k[:2] == ('SELL', 'TOMATO')))
    g['car_u'] = (sum(v for k, v in uo.items() if k[:2] == ('SELL', 'CARROT')), sum(v for k, v in ut.items() if k[:2] == ('SELL', 'CARROT')))
    g['gap'] = r['replayed'][me] - r['replayed'][1 - me]
    shops = r['shops']; g['pizza_fm'] = sum(s in ('PIZZA_SHOP', 'FARMERS_MARKET') for s in shops)
    g['first2'] = shops[:2]
    g.update(ep=r['ep'], build=r['build'], opp=r['opp'], R=r['R'], seat=me)
    rows.append(g)
json.dump(rows, open('moe/opus/pergame_band.json', 'w'))
loss = [g for g in rows if g['gap'] < 0]
print('losses', len(loss))
# concentration: tomato
tg = sorted(loss, key=lambda g: g['TOMATO'])
print('tomato gap distribution in losses:', [round(g['TOMATO']) for g in tg[:15]], '...')
print('n losses with |tomato gap|>500:', sum(abs(g['TOMATO']) > 500 for g in loss), ' tomato<-500:', sum(g['TOMATO'] < -500 for g in loss))
print('n losses where opp sold >=20 more tomato:', sum(g['tom_u'][1] - g['tom_u'][0] >= 20 for g in loss))
print('\nlosses with tomato gap < -500:')
for g in tg:
    if g['TOMATO'] >= -500: break
    print(f"  ep{g['ep']} {g['build']:10s} {g['opp'][:18]:18s} R{g['R']:.0f} gap {g['gap']:+7.0f} tomato {g['TOMATO']:+6.0f} u{g['tom_u']} pizza/fm={g['pizza_fm']} shops={g['first2']}")
# which channel "decides" each loss: largest negative channel
dec = collections.Counter()
for g in loss:
    c = min(CH + ['other'], key=lambda c: g[c]); dec[c] += 1
print('\nlargest-negative channel per loss:', dec.most_common())
# mean abs gap per channel in losses vs wins
win = [g for g in rows if g['gap'] > 0]
print(f"\n{'chan':12s}{'loss mean':>10s}{'win mean':>10s}{'loss med':>10s}")
for c in CH + ['other']:
    print(f"{c:12s}{statistics.mean(g[c] for g in loss):>+10.0f}{statistics.mean(g[c] for g in win):>+10.0f}{statistics.median(g[c] for g in loss):>+10.0f}")
# margin distribution
ms = sorted(g['gap'] for g in loss)
print('\nloss margins: median', statistics.median(ms), ' quartiles', ms[len(ms)//4], ms[3*len(ms)//4], ' n<-5000:', sum(m < -5000 for m in ms), ' n>-1000:', sum(m > -1000 for m in ms))
print('sum of loss gap in games < -5000:', sum(m for m in ms if m < -5000), ' total', sum(ms))
