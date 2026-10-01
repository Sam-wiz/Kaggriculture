"""Closed-loop test of TS (tape-switching dawn planner) vs a live agent (default C1) on the official Python engine.
usage: tsgame.py OUT.jsonl SEED0 NSEEDS WORKERS [key=value ...]   (key=value set ts module globals, e.g. M=8 R=1)
Also: tsgame.py --validate SEED  (rollout exactness: re-simulate from a mid-game snapshot with the true seed,
opponent private state and recorded opponent actions; banks must match the real game to the dollar).
"""
import copy, json, os, sys, time
from multiprocessing import Pool
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r5/build/opusb")
os.chdir(ROOT)
import harness as H
import ts

LIVE = ROOT + "/subY_C1_predict2.py"
_N = [0]


def fresh_live(path):
    _N[0] += 1
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        return H.load_agent(path, "lv_%d_%d" % (os.getpid(), _N[0]))


def set_cfg(kv):
    for k, v in kv.items():
        cur = getattr(ts, k)
        if isinstance(cur, set):
            v = set(json.loads(v))
        elif isinstance(cur, tuple):
            v = tuple(json.loads(v))
        elif isinstance(cur, float):
            v = float(v)
        elif isinstance(cur, str):
            pass
        elif isinstance(cur, int):
            v = int(v)
        setattr(ts, k, v)


def job(j):
    set_cfg(j.get("cfg", {}))
    ts.load_lib()
    ts._P = ts.Planner()
    ts._P.rng.seed(j["seed"])
    live = fresh_live(j.get("live", LIVE))
    t0 = time.time()
    pos = j["pos"]
    a, b = (ts.agent, live) if pos == 0 else (live, ts.agent)
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        r = H.run_episode(a, b, seed=j["seed"], copy_obs=True)
    me, opp = r["reward"][pos], r["reward"][1 - pos]
    lg = ts._P.log
    return dict(j, me=me, opp=opp, win=me > opp, status=r["status"], errors=r["errors"],
                plan_s=round(ts._P.plan_time, 1), plan_calls=ts._P.plan_calls,
                max_plan_s=max(x["dt"] for x in lg), switches=sum(x["sw"] for x in lg),
                teams=sorted(set(x["team"] for x in lg if x["sw"])), final_pred=lg[-1]["best"],
                wall=round(time.time() - t0, 1), log=lg)


def validate(seed, snap_step=240):
    ts.M = 4; ts.R = 1; ts.STEP0_M = 6
    """TS vs C1; snapshot TS obs + opp private at snap_step; record all actions; re-simulate from the snapshot."""
    ts.load_lib(); ts._P = ts.Planner(); ts._P.rng.seed(seed)
    live = fresh_live(LIVE)
    rec = {"acts": {}, "snap": None}
    def on_step(step, state, env):
        rec["acts"][step] = (copy.deepcopy(state[0].action), copy.deepcopy(state[1].action))
    def tsa(obs):
        if obs["step"] == snap_step:
            rec["snap"] = copy.deepcopy(obs)
        return ts.agent(obs)
    holder = {}
    def live_w(obs):
        if obs["step"] == snap_step:
            holder["opp_priv"] = copy.deepcopy(obs["private"])
        return live(obs)
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        r = H.run_episode(tsa, live_w, seed=seed, on_step=on_step, copy_obs=True)
    real = r["reward"]
    true_seed = r["seed"] if r["seed"] is not None else seed
    opp_acts = {s: a[1] for s, a in rec["acts"].items()}
    my_acts = {s: a[0] for s, a in rec["acts"].items()}
    e = {"acts": [None] + [my_acts.get(s, ts.PASS) for s in range(720)]}
    sim = ts.rollout(rec["snap"], e, true_seed, opp_private=holder["opp_priv"], opp_policy=lambda o, s: opp_acts[s])
    sim_blind = ts.rollout(rec["snap"], e, true_seed)
    P = ts._P
    # per-step true opponent deltas, injected at their own step (upper bound on what the injection model can do)
    exact = {}
    class _Inj(dict):
        pass
    def run_inj(inj_by_step):
        # reuse rollout with an hour-keyed dict rebuilt per day is not exact; do a direct loop instead
        import copy as C
        o = rec["snap"]; me = o["player"]
        farms = C.deepcopy(o["farms"]); market = C.deepcopy(o["market"]); town = C.deepcopy(o["town"])
        privs = [None, None]; privs[me] = C.deepcopy(o["private"]); privs[1 - me] = {"shed": {}, "seeds": {}, "inventories": [{}]}
        st = [ts._AS(ts.S(player=i, farms=farms, market=market, town=town, private=privs[i], step=o["step"], day=o["day"], hour=o["hour"])) for i in (0, 1)]
        env = ts._Env(true_seed)
        for s_ in range(o["step"], 720):
            st[0].observation.step = s_; st[1].observation.step = s_
            st[me].action = ts.tape_act(e, s_); st[1 - me].action = ts.PASS
            d = inj_by_step(s_)
            if d:
                for k, v in d.items(): market["inventory"][k] += v
                ts.K._refresh_prices(market)
            ts.K.interpreter(st, env)
        return farms[me]["money"]
    sim_inj_true = run_inj(lambda s_: P.deltas.get(s_))
    P.deltas = {k: v for k, v in P.deltas.items() if k < snap_step}
    sim_inj_model = ts.rollout(rec["snap"], e, true_seed, opp_inject=P.opp_model(snap_step))
    tot = {}
    for t_, d in P.deltas.items():
        if t_ >= snap_step:
            for k, v in d.items(): tot[k] = tot.get(k, 0) + v
    print(json.dumps(dict(seed=seed, env_seed=r["seed"], real=real, sim_exact=sim, sim_blind_oppPASS=sim_blind,
                          sim_inject_true_deltas=sim_inj_true, sim_inject_model=sim_inj_model, shadow_err=P.shadow_err,
                          opp_net_market_after_snap=tot)))


if __name__ == "__main__":
    if sys.argv[1] == "--validate":
        for sd in sys.argv[2:]:
            for sn in (144, 240, 360):
                validate(int(sd), sn)
        sys.exit()
    out, s0, n, w = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    cfg = dict(kv.split("=", 1) for kv in sys.argv[5:])
    jobs = [dict(seed=s0 + i, pos=i % 2, cfg=cfg) for i in range(n)]
    with Pool(w) as p, open(out, "a") as f:
        for res in p.imap_unordered(job, jobs):
            f.write(json.dumps(res, ensure_ascii=False) + "\n"); f.flush()
            print(res.get("seed"), res.get("pos"), res.get("me"), res.get("opp"), res.get("win"), "plan",
                  res.get("plan_s"), "max", res.get("max_plan_s"), "sw", res.get("switches"), res.get("teams"),
                  "pred", res.get("final_pred"), "wall", res.get("wall"), flush=True)
