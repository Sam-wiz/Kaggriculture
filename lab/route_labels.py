"""A-lite measurement: per-route margin vs fixed opponent under decoupled shop draws.

Pin route R at the day-6 switch on subV_sirxL96, play vs subV_sirxP, record our
bank + the seed's FULL unlocked-shop sequence. Shop draws are agent-independent
under kag_dc.

Usage: route_labels.py START_SEED N_SEEDS
"""
import importlib.util, json, os, sys
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

_DC = None
def dc():
    global _DC
    if _DC is None:
        spec = importlib.util.spec_from_file_location('kag_dc', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kag_dc.py'))
        _DC = importlib.util.module_from_spec(spec); spec.loader.exec_module(_DC)
    return _DC

def kload(path, pin=None):
    env = {}
    exec(compile(open(path).read(), path, 'exec'), env)
    impl = env['_IMPL']
    if pin is not None:
        orig_router = env['_router']
        def pinned(obs, step, state):
            r = orig_router(obs, step, state)
            if step >= 144 and not state.get('day27'):
                state['route'] = pin
                return pin
            return r
        impl.chassis.router = pinned
    return env['agent']

ROUTES = [r for r in range(0, 13) if r != 1] + list(range(100, 129))

def job(args):
    route, seed = args
    harness.K = dc()
    a = kload('subV_sirxL96.py', pin=route)
    b = kload('subV_sirxP.py')
    seqs = []
    def hook(step, state, env):
        shops = list(state[0].observation.town['unlocked_shops'])
        if not seqs or seqs[-1] != shops:
            seqs.append(shops)
    r = harness.run_episode(a, b, seed=seed, on_step=hook)
    return route, seed, r['reward'][0], r['reward'][1], seqs[-1] if seqs else []

if __name__ == '__main__':
    start, n = int(sys.argv[1]), int(sys.argv[2])
    jobs = [(r, s) for s in range(start, start + n) for r in ROUTES]
    out = open('route_labels.jsonl', 'a')
    with ProcessPoolExecutor(max_workers=10) as ex:
        for res in ex.map(job, jobs):
            out.write(json.dumps({'route': res[0], 'seed': res[1], 'bank': res[2], 'opp': res[3], 'shops': res[4]}) + '\n')
            out.flush()
    out.close()
    print("done", len(jobs))
