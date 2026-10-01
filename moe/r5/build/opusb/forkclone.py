"""Can a C1 rollout be cloned with os.fork (no module-state snapshot)? Exactness + cost.
C1 vs C1 on the official engine; at step T the parent forks: the child continues the SAME game (both C1 instances,
engine state deep-copied) to the end and reports banks through a pipe; the parent continues for real.
Also times: fork + child continuation with our C1 vs an opponent-profile injection (the C+B rollout shape).
usage: forkclone.py SEED T
"""
import copy, io, contextlib, json, os, pickle, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r5/build/opusb")
os.chdir(ROOT)
import harness as H
from kaggle_environments.envs.kaggriculture import kaggriculture as K
import ts

seed, T = int(sys.argv[1]), int(sys.argv[2])
with contextlib.redirect_stdout(io.StringIO()):
    A = H.load_agent(ROOT + "/subY_C1_predict2.py", "fa"); B = H.load_agent(ROOT + "/subY_C1_predict2.py", "fb")
box = {}


def continue_game(state, env, agents, start):
    for step in range(start, 720):
        obs0 = state[0].observation
        for i in range(2):
            state[i].observation.step = step
            if i:
                state[i].observation.farms = obs0.farms; state[i].observation.market = obs0.market; state[i].observation.town = obs0.town
                state[i].observation.day = obs0.day; state[i].observation.hour = obs0.hour
        for i in range(2):
            state[i].action = agents[i](copy.deepcopy(state[i].observation))
        K.interpreter(state, env)
    f = state[0].observation.farms
    return [f[0]["money"], f[1]["money"]]


def fork_run(fn):
    r, w = os.pipe(); t0 = time.perf_counter()
    pid = os.fork()
    if pid == 0:
        os.close(r)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                res = fn()
        except Exception as e:
            res = repr(e)
        os.write(w, pickle.dumps(res)); os.close(w); os._exit(0)
    os.close(w)
    data = b""
    while True:
        chunk = os.read(r, 65536)
        if not chunk:
            break
        data += chunk
    os.close(r); os.waitpid(pid, 0)
    return pickle.loads(data), time.perf_counter() - t0


def on_step(step, state, env):
    if step == T - 1:   # state now holds obs for step T; fork the true continuation (both C1s)
        box["exact"] = fork_run(lambda: continue_game(state, env, [A, B], T))
        # C+B rollout shape: our C1 from OUR observation only; opponent = profile injection, sampled seed
        me = 0; o = copy.deepcopy(state[0].observation)
        prof = ts.load_prof()
        def cb():
            farms = copy.deepcopy(o["farms"]); market = copy.deepcopy(o["market"]); town = copy.deepcopy(o["town"])
            privs = [copy.deepcopy(o["private"]), {"shed": {}, "seeds": {}, "inventories": [{}]}]
            st = [ts._AS(ts.S(player=i, farms=farms, market=market, town=town, private=privs[i], step=T, day=o["day"], hour=o["hour"])) for i in (0, 1)]
            env2 = ts._Env(777)
            for s in range(T, 720):
                st[0].observation.step = s; st[1].observation.step = s
                ts._inject(market, lambda s_: prof[s_], s)
                st[0].action = A(copy.deepcopy(st[0].observation)); st[1].action = ts.PASS
                K.interpreter(st, env2)
            return farms[0]["money"]
        box["cb"] = fork_run(cb)


with contextlib.redirect_stdout(io.StringIO()):
    r = H.run_episode(A, B, seed=seed, on_step=on_step, copy_obs=True)
print(json.dumps(dict(seed=seed, T=T, real=r["reward"], fork_exact=box["exact"][0], fork_exact_s=round(box["exact"][1], 2),
                      match=[float(a) == float(b) for a, b in zip(r["reward"], box["exact"][0])],
                      cb_rollout_bank=box["cb"][0], cb_rollout_s=round(box["cb"][1], 2))))
