"""O3 selector check: LOCKED rollout forecast vs realised delta for C1's tomato option (o3lib), paired per world.
Adapted from opusb's o1_oracle.py (same fork harness, kag_dc engine, profile-injected PASS opponent in rollouts).

Per fresh seed (our seat = seed % 2; opponent = pristine C1):
  prefix  : play to dawn d18 (step 432), where C1's V219 tomato decision is taken.
  FORECAST: from OUR observation only, fork full-season rollouts (432..719) of our C1 with arm on / off; opponent =
            PASS + market-supply profile injection (oppprof.json = top family, the pre-registered runtime model;
            c1prof.json = matched-opponent sensitivity); R env seeds common across arms. Written + flushed to LOCKS
            before any real continuation exists.
  REAL    : fork the true game from the same state for arms nat (native C1) / on / off / P2 (nat + one extra
            BUY_PRODUCT WHEAT 1 at step 432: chaos floor). nat must equal on or off to the dollar (fires check).
usage: o3_oracle.py OUT.jsonl SEED [SEED ...]
"""
import contextlib, copy, importlib.util, io, json, os, pickle, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
OB = ROOT + "/moe/r5/build/opusb"
OP = ROOT + "/moe/r5/build/opus"
sys.path.insert(0, ROOT); sys.path.insert(0, OB); sys.path.insert(0, OP); os.chdir(ROOT)
import harness as H
import o3lib, ts
spec = importlib.util.spec_from_file_location("kag_dc", ROOT + "/kag_dc.py"); DC = importlib.util.module_from_spec(spec)
spec.loader.exec_module(DC); H.K = DC

FORK = int(os.environ.get("O3_FORK", 432))
R = int(os.environ.get("O3_R", 4))
PROFS = {"top": json.load(open(OB + "/oppprof.json"))["mean"], "c1": json.load(open(OB + "/c1prof.json"))["mean"]}
PASS = {"farmer": ["PASS"], "hands": [], "market": []}
LOCKS = os.environ.get("O3_LOCKS", OP + "/oracle_O3_locks.jsonl")
ARMS = ("on", "off")


class Stop(Exception):
    pass


def fork_call(fn):
    r, w = os.pipe(); t0 = time.perf_counter()
    pid = os.fork()
    if pid == 0:
        os.close(r)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                res = fn()
        except Exception as e:  # noqa: BLE001
            res = {"err": repr(e)}
        os.write(w, pickle.dumps(res)); os.close(w); os._exit(0)
    os.close(w); data = b""
    while True:
        ch = os.read(r, 1 << 16)
        if not ch:
            break
        data += ch
    os.close(r); os.waitpid(pid, 0)
    res = pickle.loads(data)
    if isinstance(res, dict):
        res["sec"] = round(time.perf_counter() - t0, 2)
    return res


def run_seed(seed):
    me = seed % 2
    ns = o3lib.load("me"); opp = o3lib.load("opp")
    rec = dict(seed=seed, me=me)
    ag = [None, None]; ag[me] = ns["agent"]; ag[1 - me] = opp["agent"]

    def set_arm(arm):
        if arm in ARMS:
            ns["_O3_ARM"][me] = arm

    def rollout(o, arm, rseed, prof):
        set_arm(arm)
        farms = copy.deepcopy(o["farms"]); market = copy.deepcopy(o["market"]); town = copy.deepcopy(o["town"])
        privs = [None, None]; privs[me] = copy.deepcopy(o["private"])
        privs[1 - me] = {"shed": {}, "seeds": {}, "inventories": [{}]}
        st = [ts._AS(ts.S(player=i, farms=farms, market=market, town=town, private=privs[i], step=FORK, day=o["day"],
                          hour=o["hour"], remainingOverageTime=60.0)) for i in (0, 1)]
        env2 = ts._Env(rseed)
        for s in range(FORK, 720):
            for i in (0, 1):
                st[i].observation.step = s
                st[i].observation.day = st[0].observation.day; st[i].observation.hour = st[0].observation.hour
            ts._inject(market, lambda s_: prof[s_], s)
            st[me].action = ns["agent"](ts._st(copy.deepcopy(dict(st[me].observation))))
            st[1 - me].action = PASS
            DC.interpreter(st, env2)
        return {"bank": farms[me]["money"], "tel": o3lib.telemetry(ns, farms[me], me)}

    def cont(state, env, arm):
        set_arm(arm)
        a_me = ns["agent"]
        if arm == "P2":
            def a_me(obs):
                act = ns["agent"](obs)
                if int(obs["step"]) == FORK and len(act.get("market") or []) < 10:
                    act = copy.deepcopy(act); act["market"] = list(act.get("market") or []) + [["BUY_PRODUCT", "WHEAT", 1]]
                return act
        agents = [None, None]; agents[me] = a_me; agents[1 - me] = opp["agent"]
        land, errs, tom = [], [None, None], {}
        for step in range(FORK, 720):
            obs0 = state[0].observation
            for i in (0, 1):
                state[i].observation.step = step; state[i].observation.day = obs0.day; state[i].observation.hour = obs0.hour
                if i:
                    state[i].observation.farms = obs0.farms; state[i].observation.market = obs0.market
                    state[i].observation.town = obs0.town
            for i in (0, 1):
                if state[i].status != "ACTIVE":
                    state[i].action = PASS; continue
                try:
                    act = agents[i](copy.deepcopy(state[i].observation))
                except Exception as e:  # noqa: BLE001
                    errs[i] = repr(e); state[i].status = "ERROR"; act = PASS
                state[i].action = act if isinstance(act, dict) else PASS
            if any(o and o[0] == "BUY_LAND" for o in (state[me].action.get("market") or [])):
                land.append(step)
            DC.interpreter(state, env)
            if step % 24 == 23:
                m = state[0].observation.market
                tom[step // 24] = [m["inventory"]["TOMATO"], m["prices"]["TOMATO"]]
        f = state[0].observation.farms
        opp_tom = sum(isinstance(t, dict) and t.get("crop") == "TOMATO" for row in f[1 - me]["tiles"] for t in row)
        return {"bank": f[me]["money"], "opp": f[1 - me]["money"], "land": land, "errors": errs,
                "status": [s.status for s in state], "tom_mkt": tom, "opp_tom_tiles_end": opp_tom,
                "opp_committed": bool(opp.get("_V219_STATES", {}).get(1 - me, {}).get("committed")),
                "tel": o3lib.telemetry(ns, f[me], me)}

    def hook(step, state, env):
        if step != FORK - 1:
            return
        o = json.loads(json.dumps(state[me].observation))
        o["step"] = FORK; o["day"] = FORK // 24; o["hour"] = 0
        rec["dawn_cash"] = o["farms"][me]["money"]; rec["shops"] = list(o["town"]["unlocked_shops"])
        rec["tom_inv"] = o["market"]["inventory"]["TOMATO"]; rec["tom_px"] = o["market"]["prices"]["TOMATO"]
        rec["opp_tom_tiles"] = sum(isinstance(t, dict) and t.get("crop") == "TOMATO"
                                   for row in o["farms"][1 - me]["tiles"] for t in row)
        fc = {}
        for pn, prof in PROFS.items():
            fc[pn] = {arm: [fork_call(lambda arm=arm, r=r, prof=prof: rollout(o, arm, 7_300_000 + 100 * (seed % 100000) + r, prof))
                            for r in range(R)] for arm in ARMS}
        rec["forecast"] = fc
        rec["fc_delta"] = {pn: sum(x["bank"] - y["bank"] for x, y in zip(fc[pn]["on"], fc[pn]["off"])) / R for pn in fc}
        rec["fc_tel"] = {pn: fc[pn]["on"][0].get("tel", {}) for pn in fc}
        with open(LOCKS, "a") as fh:   # lock forecasts before any real outcome exists
            fh.write(json.dumps(dict(seed=seed, me=me, t=time.time(), fc_delta=rec["fc_delta"],
                                     fc_banks={pn: {a: [x.get("bank") for x in v] for a, v in d.items()} for pn, d in fc.items()})) + "\n")
        rec["real"] = {arm: fork_call(lambda arm=arm: cont(state, env, arm)) for arm in ("nat",) + ARMS + ("P2",)}
        raise Stop

    t0 = time.time()
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            H.run_episode(ag[0], ag[1], seed=seed, on_step=hook, catch_errors=False)
    except Stop:
        pass
    re_ = rec["real"]
    rec["delta"] = re_["on"]["bank"] - re_["off"]["bank"]                     # the option's realised value
    rec["delta_margin"] = (re_["on"]["bank"] - re_["on"]["opp"]) - (re_["off"]["bank"] - re_["off"]["opp"])
    rec["nat_is"] = [a for a in ARMS if re_[a]["bank"] == re_["nat"]["bank"] and re_[a]["opp"] == re_["nat"]["opp"]]
    rec["p2"] = re_["P2"]["bank"] - re_["nat"]["bank"]
    rec["sec"] = round(time.time() - t0, 1)
    return rec


if __name__ == "__main__":
    out = sys.argv[1]
    for sd in map(int, sys.argv[2:]):
        r = run_seed(sd)
        with open(out, "a") as fh:
            fh.write(json.dumps(r) + "\n")
        tel = r["real"]["on"]["tel"]
        print(sd, r["me"], "native", tel.get("native"), "struct", tel.get("struct"), "rev", tel.get("rev"),
              "fc", {k: round(v) for k, v in r["fc_delta"].items()}, "real", int(r["delta"]), "nat_is", r["nat_is"],
              "p2", int(r["p2"]), "cash", int(r["dawn_cash"]), r["sec"], "s", flush=True)
