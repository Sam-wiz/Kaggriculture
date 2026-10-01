"""Decompose the money gap (ours - theirs) in band episodes by phase x channel, using exact FILLS.

usage: python moe/opus/decompose.py [ledger.json] [--builds a,b] [--losses|--wins]
"""
import json, statistics, sys, collections
path = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else 'moe/opus/ledger_band.json'
args = sys.argv[1:]
L = json.load(open(path))
builds = None
for a in args:
    if a.startswith('--builds='):
        builds = set(a.split('=', 1)[1].split(','))
PH = [(0, 240, 'd0-9'), (240, 504, 'd10-20'), (504, 720, 'd21-29')]
PRODUCTS = ['WHEAT', 'CARROT', 'TOMATO', 'STRAWBERRY', 'MELON', 'EGG', 'MILK', 'WOOL', 'FERTILIZER']


def phase(step):
    for lo, hi, n in PH:
        if lo <= step < hi:
            return n


def ledger(rec, p):
    """channel -> phase -> $ (positive = money in); plus units."""
    money = collections.defaultdict(float); units = collections.defaultdict(int)
    for step, pl, op, item, price in rec['fills']:
        if pl != p:
            continue
        ph = phase(step)
        if op == 'SELL':
            money[('SELL', item, ph)] += price; units[('SELL', item, ph)] += 1
        elif op in ('HIRE', 'BUY_LAND'):
            money[(op, '', ph)] -= price; units[(op, '', ph)] += 1
        else:
            money[(op, item, ph)] -= price; units[(op, item, ph)] += 1
    prod = collections.defaultdict(int)
    for step, pl, item, n in rec['prod']:
        if pl == p:
            prod[(item, phase(step))] += n
    placed = collections.Counter(a for s, pl, a in rec['placed'] if pl == p)
    disc = sum(n for s, pl, n in rec['discard'] if pl == p)
    return money, units, prod, placed, disc


def summarize(recs, label):
    if not recs:
        return
    n = len(recs)
    gaps = collections.defaultdict(list)
    tab = collections.defaultdict(lambda: [0.0, 0.0])  # key -> [ours_sum, theirs_sum]
    for r in recs:
        me, op_ = r['seat'], 1 - r['seat']
        mo, uo, po, plo, do = ledger(r, me)
        mt, ut, pt, plt, dt = ledger(r, op_)
        # identity check
        tot_o = 3000 + sum(mo.values()); tot_t = 3000 + sum(mt.values())
        assert abs(tot_o - r['replayed'][me]) < 1 and abs(tot_t - r['replayed'][op_]) < 1, (r['ep'], tot_o, r['replayed'])
        keys = set(mo) | set(mt)
        for k in keys:
            tab[('$',) + k][0] += mo.get(k, 0); tab[('$',) + k][1] += mt.get(k, 0)
            tab[('u',) + k][0] += uo.get(k, 0); tab[('u',) + k][1] += ut.get(k, 0)
        for k in set(po) | set(pt):
            tab[('prod',) + k][0] += po.get(k, 0); tab[('prod',) + k][1] += pt.get(k, 0)
        for a in set(plo) | set(plt):
            tab[('placed', a)][0] += plo.get(a, 0); tab[('placed', a)][1] += plt.get(a, 0)
        tab[('discard',)][0] += do; tab[('discard',)][1] += dt
        tab[('final',)][0] += r['replayed'][me]; tab[('final',)][1] += r['replayed'][op_]
    f = lambda k: (tab[k][0] / n, tab[k][1] / n, (tab[k][0] - tab[k][1]) / n)
    o, t, g = f(('final',))
    print(f"\n=== {label}: n={n}  mean final ours {o:,.0f} theirs {t:,.0f} gap {g:+,.0f}")
    # phase x channel money gaps
    chans = collections.OrderedDict()
    for p in PRODUCTS:
        chans['SELL ' + p] = [('$', 'SELL', p)]
    chans['BUY_SEED'] = [('$', 'BUY_SEED', c) for c in ['WHEAT', 'CARROT', 'TOMATO', 'STRAWBERRY', 'MELON']]
    chans['BUY_ANIMAL'] = [('$', 'BUY_ANIMAL', a) for a in ['COW', 'SHEEP', 'GOOSE']]
    chans['BUY_PRODUCT WHEAT'] = [('$', 'BUY_PRODUCT', 'WHEAT')]
    chans['BUY_PRODUCT FERT'] = [('$', 'BUY_PRODUCT', 'FERTILIZER')]
    chans['HIRE'] = [('$', 'HIRE', '')]
    chans['BUY_LAND'] = [('$', 'BUY_LAND', '')]
    print(f"{'channel ($ gap ours-theirs)':28s}" + ''.join(f"{n_:>10s}" for _, _, n_ in PH) + f"{'total':>10s}{'ours':>10s}{'theirs':>10s}")
    for name, ks in chans.items():
        row = []
        for _, _, ph in PH:
            row.append(sum(f(k + (ph,))[2] for k in ks))
        ours = sum(f(k + (ph,))[0] for k in ks for _, _, ph in PH)
        th = sum(f(k + (ph,))[1] for k in ks for _, _, ph in PH)
        print(f"{name:28s}" + ''.join(f"{x:>+10,.0f}" for x in row) + f"{sum(row):>+10,.0f}{ours:>10,.0f}{th:>10,.0f}")
    # sell volume & price per product
    print(f"\n{'product':12s}{'u_ours':>8s}{'u_thr':>8s}{'p_ours':>8s}{'p_thr':>8s}{'vol_eff':>10s}{'px_eff':>10s}  prod_ours prod_thr (harvested units)")
    for p in PRODUCTS:
        uo = sum(f(('u', 'SELL', p, ph))[0] for _, _, ph in PH); ut = sum(f(('u', 'SELL', p, ph))[1] for _, _, ph in PH)
        mo_ = sum(f(('$', 'SELL', p, ph))[0] for _, _, ph in PH); mt_ = sum(f(('$', 'SELL', p, ph))[1] for _, _, ph in PH)
        po_ = mo_ / uo if uo else 0; pt_ = mt_ / ut if ut else 0
        pro = sum(f(('prod', p, ph))[0] for _, _, ph in PH); prt = sum(f(('prod', p, ph))[1] for _, _, ph in PH)
        print(f"{p:12s}{uo:>8.1f}{ut:>8.1f}{po_:>8.1f}{pt_:>8.1f}{(uo-ut)*pt_:>+10,.0f}{uo*(po_-pt_):>+10,.0f}  {pro:8.1f} {prt:8.1f}")
    print("placed:", {a: (round(f(('placed', a))[0], 1), round(f(('placed', a))[1], 1)) for a in ['COW', 'SHEEP', 'GOOSE']},
          " discards:", tuple(round(x, 1) for x in f(('discard',))[:2]),
          " hires:", tuple(round(sum(f(('u', 'HIRE', '', ph))[i] for _, _, ph in PH), 1) for i in (0, 1)))


def herd(recs, day):
    o = collections.Counter(); t = collections.Counter()
    for r in recs:
        for d, h in r['herd']:
            if d == day:
                o.update(h[r['seat']]); t.update(h[1 - r['seat']])
    n = len(recs)
    ks = sorted(set(o) | set(t))
    return {k: (round(o[k] / n, 1), round(t[k] / n, 1)) for k in ks if k != 'hands'}


if __name__ == '__main__':
    recs = [r for r in L if 'err' not in r and all(r['match'])]
    if builds:
        recs = [r for r in recs if r['build'] in builds]
    loss = [r for r in recs if r['ours'] < r['theirs']]
    win = [r for r in recs if r['ours'] > r['theirs']]
    summarize(loss, 'LOSSES')
    for d in (6, 12, 20, 27):
        print(f"  herd/plants at dawn day {d} (ours, theirs):", herd(loss, d))
    summarize(win, 'WINS')
    for d in (6, 12, 20, 27):
        print(f"  herd/plants at dawn day {d} (ours, theirs):", herd(win, d))
