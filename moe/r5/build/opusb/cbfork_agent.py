"""Kill-test item 1 probe (opusb.md §6): C1 + an in-agent os.fork rollout, run under the OFFICIAL env.run.
At FORK_STEPS the agent forks; the child plays C1 from OUR observation to the end of season (opponent = profile
injection, sampled seed) and pipes back its bank; the parent waits with a hard deadline (select + SIGKILL), reaps the
child, logs, then returns C1's real action. The fork must not change the real game (compare to a no-fork reference)."""
import contextlib, copy, io, json, os, pickle, select, signal, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r5/build/opusb")
import harness as H
import ts
from kaggle_environments.envs.kaggriculture import kaggriculture as K

with contextlib.redirect_stdout(io.StringIO()):
    _C1 = H.load_agent(ROOT + "/subY_C1_predict2.py", "cbw_%d_%d" % (os.getpid(), int(time.time() * 1e6)))
FORK_STEPS = (144, 240)
DEADLINE = 8.0
LOG = ROOT + "/moe/r5/build/opusb/cbfork_log.jsonl"


def _roll(o):
    prof = ts.load_prof(); me = o["player"]; T = o["step"]
    farms = copy.deepcopy(o["farms"]); market = copy.deepcopy(o["market"]); town = copy.deepcopy(o["town"])
    privs = [None, None]; privs[me] = copy.deepcopy(o["private"]); privs[1 - me] = {"shed": {}, "seeds": {}, "inventories": [{}]}
    st = [ts._AS(ts.S(player=i, farms=farms, market=market, town=town, private=privs[i], step=T, day=o["day"], hour=o["hour"])) for i in (0, 1)]
    env2 = ts._Env(777)
    for s in range(T, 720):
        st[0].observation.step = s; st[1].observation.step = s
        ts._inject(market, lambda s_: prof[s_], s)
        st[me].action = _C1(ts._st(copy.deepcopy(dict(st[me].observation)))); st[1 - me].action = ts.PASS
        K.interpreter(st, env2)
    return farms[me]["money"]


def _fork(o):
    r, w = os.pipe(); t0 = time.perf_counter()
    pid = os.fork()
    if pid == 0:
        os.close(r)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                res = _roll(o)
        except Exception as e:
            res = "ERR " + repr(e)
        os.write(w, pickle.dumps(res)); os.close(w); os._exit(0)
    os.close(w); data = b""; killed = False
    while True:
        left = DEADLINE - (time.perf_counter() - t0)
        if left <= 0:
            os.kill(pid, signal.SIGKILL); killed = True; break
        rd, _, _ = select.select([r], [], [], left)
        if rd:
            ch = os.read(r, 65536)
            if not ch:
                break
            data += ch
    os.close(r); _, status = os.waitpid(pid, 0)
    return dict(pid=pid, res=pickle.loads(data) if data and not killed else None, killed=killed, status=status,
                dt=round(time.perf_counter() - t0, 2))


def agent(obs, config=None):
    if obs["step"] in FORK_STEPS:
        o = json.loads(json.dumps(obs))   # plain dict copy of the Struct
        rec = _fork(o); rec.update(step=obs["step"], seat=obs["player"], parent=os.getpid())
        with open(LOG, "a") as f:
            f.write(json.dumps(rec) + "\n")
    return _C1(obs)
