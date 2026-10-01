import inco, sys, os, json
sys.path.insert(0, '.')
import p16var

def _load(p):
    d = os.path.dirname(os.path.abspath(p))
    if d not in sys.path: sys.path.insert(0, d)
    return inco.load_agent(p)

OPPS = {
    'p16': 'rivals/kaggriculture-pipe16-idle-workers/_entry.py',
    'v2945': 'subJ_2945.py',
    'a2802': 'rivals5/2802-two-identical-agents-90-points-apart/_entry.py',
}
VARIANTS = [
    ('allon', {'budget_guard': True, 'room_guard': True, 'clamp_sells': True,
               'dead_stock': True, 'terminal_liquidation': True}, None),
    ('fr_union', {'front_run': True}, 'union'),
]
SEEDS = [6001, 6002, 6003, 6004]

if __name__ == '__main__':
    opps = {k: _load(v) for k, v in OPPS.items()}
    for vn, flags, pm in VARIANTS:
        v = p16var.make_variant(flags, pm, vn)
        for on, op in opps.items():
            ms = []
            for s in SEEDS:
                a, b = inco.match(v.agent, op, s)
                c, d = inco.match(op, v.agent, s)
                ms += [a - b, d - c]
            w = sum(1 for x in ms if x > 0)
            print(f'{vn:9s} vs {on:6s}: W{w}-L{len(ms)-w} margin {sum(ms)/len(ms):+8.0f}  {[round(x) for x in ms]}', flush=True)
