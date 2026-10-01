import json, collections, statistics as S, sys
rows=[json.loads(l) for l in open(sys.argv[1] if len(sys.argv)>1 else 'moe/r4/build/opusb/t1.jsonl')]
print(len(rows), 'errs', sum('err' in r for r in rows))
V = '-v' in sys.argv
agg = collections.defaultdict(list)
for r in rows:
    if 'err' in r: print(r['err']); continue
    t=r['tele']; agg[r['arm']].append(r)
    if V: print(r['arm'][:5], r['team'][:10].ljust(10), 'me %6.0f opp %6.0f | rec %6.0f/%6.0f | shops %s | dead %d refS %d refA %d refH %d refL %d plantD %d harvD %d esc %d dry %d'%(
        r['me'],r['opp'],r['rec_me'],r['rec_opp'], r['shops']==r['rec_shops'], t['dead_actions'],t['refused_buy_seed'],t['refused_buy_animal'],t['refused_hire'],t['refused_buy_land'],t['plant_dead'],t['harvest_dead'],t['animals_escaped'],t['plants_dry']))
for arm, rs in agg.items():
    m = [r['me']-r['opp'] for r in rs]
    ret = [r['me']/r['rec_me'] for r in rs]
    W = sum(x>0 for x in m)
    tk = lambda k: S.mean(r['tele'][k] for r in rs)
    print(f"{arm:6s} n={len(rs):3d} tapeW-L {W}-{len(rs)-W} margin med {S.median(m):+8.0f} mean {S.mean(m):+8.0f} | tape bank/rec {S.median(ret):.3f} | opp bank med {S.median(r['opp'] for r in rs):8.0f} | dead {tk('dead_actions'):.0f} refA {tk('refused_buy_animal'):.1f} refL {tk('refused_buy_land'):.1f} refS {tk('refused_buy_seed'):.1f} refH {tk('refused_hire'):.1f} esc {tk('animals_escaped'):.1f} dry {tk('plants_dry'):.1f} plantD {tk('plant_dead'):.0f}")
