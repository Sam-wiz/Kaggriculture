"""Sell-timing forensics on whisker games: per product, contested vs solo sells, lead/lag."""
import json, sys, collections, statistics
L = [r for r in json.load(open('moe/opus/ledger_band.json')) if 'err' not in r]
tom = {g['ep']: g for g in json.load(open('moe/opus/pergame_band.json'))}
P = ['WHEAT','CARROT','TOMATO','STRAWBERRY','MELON','EGG','MILK','WOOL','FERTILIZER']
def analyze(recs, label):
    acc = collections.defaultdict(lambda: collections.defaultdict(float))
    for r in recs:
        me = r['seat']
        by = collections.defaultdict(lambda: [[], []])  # (step,item) -> [prices seat0, seat1]
        for step, pl, op, item, price in r['fills']:
            if op == 'SELL':
                by[(step, item)][pl].append(price)
        for (step, item), pr in by.items():
            o, t = pr[me], pr[1 - me]
            ph = 0 if step < 240 else 1 if step < 504 else 2
            if o and t:
                k = 'both'
            elif o:
                k = 'solo_o'
            else:
                k = 'solo_t'
            a = acc[item]
            a[k + '_n'] += 1
            a[k + '_uo'] += len(o); a[k + '_ut'] += len(t)
            a[k + '_$o'] += sum(o); a[k + '_$t'] += sum(t)
            a['stepw_o'] += step * len(o); a['stepw_t'] += step * len(t)
            a['u_o'] += len(o); a['u_t'] += len(t)
    n = len(recs)
    print(f"\n== {label} n={n}  (per game means)")
    print(f"{'item':11s}{'mstep_o':>8s}{'mstep_t':>8s} | {'both: turns':>11s}{'u_o':>6s}{'u_t':>6s}{'p_o':>7s}{'p_t':>7s}{'$gap':>7s} | {'solo_o u':>9s}{'p':>6s} | {'solo_t u':>9s}{'p':>6s} | tot$gap")
    for item in P:
        a = acc[item]
        if not a['u_o'] and not a['u_t']: continue
        f = lambda k: a[k] / n
        po = a['both_$o'] / a['both_uo'] if a['both_uo'] else 0; pt = a['both_$t'] / a['both_ut'] if a['both_ut'] else 0
        tot = (a['both_$o'] + a['solo_o_$o'] - a['both_$t'] - a['solo_t_$t']) / n
        print(f"{item:11s}{a['stepw_o']/max(1,a['u_o']):>8.1f}{a['stepw_t']/max(1,a['u_t']):>8.1f} | {f('both_n'):>11.1f}{f('both_uo'):>6.1f}{f('both_ut'):>6.1f}{po:>7.1f}{pt:>7.1f}{f('both_$o')-f('both_$t'):>+7.0f} | "
              f"{f('solo_o_uo'):>9.1f}{(a['solo_o_$o']/a['solo_o_uo'] if a['solo_o_uo'] else 0):>6.1f} | {f('solo_t_ut'):>9.1f}{(a['solo_t_$t']/a['solo_t_ut'] if a['solo_t_ut'] else 0):>6.1f} | {tot:+.0f}")
wl = [r for r in L if -3000 < r['replayed'][r['seat']] - r['replayed'][1-r['seat']] < 0 and abs(tom[r['ep']]['TOMATO']) <= 500]
ww = [r for r in L if 0 < r['replayed'][r['seat']] - r['replayed'][1-r['seat']] < 3000 and abs(tom[r['ep']]['TOMATO']) <= 500]
analyze(wl, 'WHISKER LOSSES (-3000<gap<0, no tomato annex)')
analyze(ww, 'WHISKER WINS (0<gap<3000, no tomato annex)')
