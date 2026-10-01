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
    'v48': 'subH2_v48.py',
    'metav4': 'subL_metav4.py',
    'a2802': 'rivals5/2802-two-identical-agents-90-points-apart/_entry.py',
    'melon': 'rivals5/kaggriculture-melon-threshold-squeeze-2749/_entry.py',
}
VARIANTS = [
    ('clamp', {'clamp_sells': True}, None),
    ('cl_dt', {'clamp_sells': True, 'dead_stock': True, 'terminal_liquidation': True}, None),
]
SEEDS = [6001, 6002, 6003, 6004, 6005, 6006, 6007, 6008]

if __name__ == '__main__':
    opps = {k: _load(v) for k, v in OPPS.items()}
    out = open('data/p16var_matrix.jsonl', 'a')
    for vn, flags, pm in VARIANTS:
        v = p16var.make_variant(flags, pm, vn)
        for on, op in opps.items():
            ms = []
            for s in SEEDS:
                a, b = inco.match(v.agent, op, s)
                c, d = inco.match(op, v.agent, s)
                ms += [a - b, d - c]
            w = sum(1 for x in ms if x > 0)
            rec = {'v': vn, 'vs': on, 'w': w, 'l': len(ms) - w, 'margin': sum(ms) / len(ms)}
            out.write(json.dumps(rec) + '\n'); out.flush()
            print(f'{vn:7s} vs {on:6s}: W{w}-L{len(ms)-w} margin {sum(ms)/len(ms):+8.0f}', flush=True)
