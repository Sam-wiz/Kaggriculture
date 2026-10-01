# trace pipe16 vs 2802 loss: where does bank diverge and why
import inco, sys, os, json, collections
sys.path.insert(0, '.')

def _load(path):
    d = os.path.dirname(os.path.abspath(path))
    if d not in sys.path: sys.path.insert(0, d)
    return inco.load_agent(path)

import kagsim

def trace(seed):
    p16 = _load('rivals/kaggriculture-pipe16-idle-workers/_entry.py')
    a28 = _load('rivals5/2802-two-identical-agents-90-points-apart/_entry.py')
    g = kagsim.Game(seed=seed)
    snaps = []
    market_sells = {'p16': collections.Counter(), 'a28': collections.Counter()}
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        a0 = p16(o0)   # pipe16 seat 0
        a1 = a28(o1)   # 2802 seat 1
        # record market orders
        for ag, name in ((a0,'p16'),(a1,'a28')):
            for o in (ag.get('market') or []):
                if len(o) >= 2:
                    market_sells[name][' '.join(map(str, o[:3]))] += 1
        g.step(a0, a1)
        if t % 24 == 0 or t == 719:
            day = t // 24
            snaps.append((t, g.observe(0)['farms'][0]['money'], g.observe(0)['farms'][1]['money'],
                          dict(g.observe(0)['market']['prices'])))
    return snaps, market_sells, g.reward(0), g.reward(1)

snaps, ms, r0, r1 = trace(6001)
print(f'final: pipe16 {r0:.0f} vs 2802 {r1:.0f}')
print('turn  p16_money  2802_money  diff   | WHEAT CARROT MILK WOOL TOMATO STRAW MELON EGG prices')
for t, m0, m1, pr in snaps:
    if t % 72 == 0 or t == 719:
        print(f'{t:4d} {m0:9.0f} {m1:10.0f} {m0-m1:+9.0f}  {pr["WHEAT"]:5.0f} {pr["CARROT"]:5.0f} {pr["MILK"]:5.0f} {pr["WOOL"]:5.0f} {pr["TOMATO"]:5.0f} {pr["STRAWBERRY"]:5.0f} {pr["MELON"]:5.0f} {pr["EGG"]:5.0f}')
