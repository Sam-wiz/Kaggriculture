# Engine / rollout cost benchmark for runtime planning (Architecture B), pure Python official interpreter.
# Measures: C1-vs-C1 full episode wall; interpreter-only cost per step (PASS/PASS) from a mid-game snapshot;
# deepcopy cost of the full engine state; C1 per-step agent cost.  Usage: bench_engine.py [snap_step]
import copy, sys, time, os
sys.path.insert(0, os.getcwd())
import harness as H
from kaggle_environments.envs.kaggriculture import kaggriculture as K

SNAP = int(sys.argv[1]) if len(sys.argv) > 1 else 240
C1 = 'subY_C1_predict2.py'
PASS = {"farmer": ["PASS"], "hands": [], "market": []}

snap = {}
agent_t = [0.0, 0.0]
a0 = H.load_agent(C1, 'c1a'); a1 = H.load_agent(C1, 'c1b')
def timed(f, i):
    def g(obs):
        t = time.perf_counter(); r = f(obs); agent_t[i] += time.perf_counter() - t; return r
    return g
def on_step(step, state, env):
    if step == SNAP - 1:
        snap['state'] = copy.deepcopy(state); snap['env'] = copy.deepcopy(env)
t0 = time.perf_counter()
r = H.run_episode(timed(a0, 0), timed(a1, 1), seed=9400001, on_step=on_step, copy_obs=False)
wall = time.perf_counter() - t0
print(f"C1 vs C1 full episode: wall {wall:.2f}s, agent0 {agent_t[0]:.2f}s ({agent_t[0]/720*1e3:.2f} ms/step), "
      f"agent1 {agent_t[1]:.2f}s, engine+glue {wall-sum(agent_t):.2f}s ({(wall-sum(agent_t))/720*1e3:.2f} ms/step); banks {r['reward']}")

# deepcopy cost
N = 20; t = time.perf_counter()
for _ in range(N):
    s2 = copy.deepcopy(snap['state']); e2 = copy.deepcopy(snap['env'])
dc = (time.perf_counter() - t) / N
print(f"deepcopy(state+env) at step {SNAP}: {dc*1e3:.2f} ms")

# interpreter-only rollout PASS/PASS from snapshot to end
def rollout_pass(steps):
    st = copy.deepcopy(snap['state']); env = copy.deepcopy(snap['env'])
    t = time.perf_counter()
    for k in range(steps):
        obs0 = st[0].observation
        step = SNAP + k
        for i in range(2):
            st[i].observation.step = step
            if i > 0:
                st[i].observation.farms = obs0.farms; st[i].observation.market = obs0.market; st[i].observation.town = obs0.town
            st[i].action = PASS
        K.interpreter(st, env)
    return time.perf_counter() - t
n = 720 - SNAP
dt = rollout_pass(n)
print(f"interpreter PASS/PASS {n} steps from {SNAP}: {dt:.3f}s = {dt/n*1e3:.3f} ms/step")
# a 'busy' action mix without agent cost: replay the recorded C1 actions would need logging; approximate with
# per-step C1 agent cost measured above.
