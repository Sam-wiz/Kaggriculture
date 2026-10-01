"""Prove a candidate layer fires: counters, timing, bank sanity. usage: firetest.py cand.py opp.py seed [seat]"""
import importlib.util, sys, time, os
sys.path.insert(0, os.getcwd())
import harness
def load(p, name):
    spec = importlib.util.spec_from_file_location(name, p); m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m; spec.loader.exec_module(m); return m
cand, opp, seed = sys.argv[1], sys.argv[2], int(sys.argv[3])
seat = int(sys.argv[4]) if len(sys.argv) > 4 else 0
m = load(cand, 'candmod'); o = load(opp, 'oppmod')
t0 = time.time()
ags = [m.agent, o.agent] if seat == 0 else [o.agent, m.agent]
r = harness.run_episode(ags[0], ags[1], seed=seed)
dt = time.time() - t0
print('reward', r['reward'], 'status', r['status'], 'errors', r['errors'], f'{dt:.1f}s')
print("stats", getattr(m, "_BRX_STATS", None), getattr(m, "_BRX2", {}).get("upd"), getattr(m, "_BRX2", {}).get("nat"), getattr(m, "_BRX2", {}).get("sir"), round(getattr(m, "_BRX2", {}).get("lo", 0), 2))
me = r['reward'][seat]; th = r['reward'][1 - seat]
print('cand margin', me - th)
