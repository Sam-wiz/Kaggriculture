"""O1 oracle + locked rollout forecasts (luna's rule), paired per world, kag_dc engine (shops decoupled from weeds).

Per fresh seed (our seat = seed % 2; opponent = pristine C1):
  prefix  : play to dawn d11 (step 264) with our S and C namespaces in lockstep (actions must be identical; counted).
  FORECAST: from OUR observation only (as the agent would at runtime), fork full-season rollouts of our C1 for arms
            off / S (O1 sheep) / C (O1 cow); opponent = PASS + market-supply profile injection; R sampled env seeds,
            common across arms. Profiles: oppprof.json (top family; the pre-registered runtime model) and c1prof.json.
            Forecasts are written + flushed to oracle_O1_locks.jsonl BEFORE any real continuation is run.
  REAL    : fork the true game from the same state for arms off / S / C, and two placebo arms (noise floor for
            max(0, delta)): P1 = off with the day>=11 weed stream re-salted (weed luck); P2 = off plus one extra
            BUY_PRODUCT WHEAT 1 at step 264 (a ~$30 action perturbation: chaos through C1's reactive layers).
usage: o1_oracle.py OUT.jsonl SEED [SEED ...]
"""
import contextlib, copy, importlib.util, io, json, os, pickle, random, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
B = ROOT + "/moe/r5/build/opusb"
sys.path.insert(0, ROOT); sys.path.insert(0, B); os.chdir(ROOT)
import harness as H
import o1lib, ts
spec = importlib.util.spec_from_file_location("kag_dc", ROOT + "/kag_dc.py"); DC = importlib.util.module_from_spec(spec)
spec.loader.exec_module(DC); H.K = DC

FORK = 264          # dawn of day 11: O1 (V233 request window d11 h0-3 / d12 h0-1) cannot act earlier
R = 2
PROFS = {"top": json.load(open(B + "/oppprof.json"))["mean"], "c1": json.load(open(B + "/c1prof.json"))["mean"]}
PASS = {"farmer": ["PASS"], "hands": [], "market": []}
LOCKS = os.environ.get("O1_LOCKS", B + "/oracle_O1_locks.jsonl")
ARMS = os.environ.get("O1_ARMS", "S,C").split(",")                                   # O1 variants (o1lib)
PLAC = [p for p in os.environ.get("O1_PLACEBO", "P1,P2").split(",") if p]


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
    ns = {a: o1lib.load(a, "me") for a in ["S"] + [a for a in ARMS if a != "S"]}; opp = o1lib.load("C1", "opp")
    nsS = ns["S"]
    mism = [0]

    def ours(obs):
        ocs = {k: copy.deepcopy(obs) for k in ns if k != "S"}
        a = nsS["agent"](obs)
        for k, oc in ocs.items():
            if json.dumps(a, sort_keys=True) != json.dumps(ns[k]["agent"](oc), sort_keys=True):
                mism[0] += 1
        return a

    rec = dict(seed=seed, me=me)
    ag = [None, None]; ag[me] = ours; ag[1 - me] = opp["agent"]

    def arm_agent(arm):
        if arm in ARMS:
            ns[arm]["_O1_ARM"][me] = True
            return ns[arm]["agent"]
        return nsS["agent"]

    # ---------------- forecast: rollout from our observation only ----------------
    def rollout(o, arm, rseed, prof):
        a = arm_agent(arm)
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
            st[me].action = a(ts._st(copy.deepcopy(dict(st[me].observation))))
            st[1 - me].action = PASS
            DC.interpreter(st, env2)
        return {"bank": farms[me]["money"], "tel": o1lib.telemetry(ns.get(arm, nsS), farms[me])}

    # ---------------- real continuation of the true game ----------------
    def cont(state, env, arm):
        a_me = arm_agent(arm) if arm in ARMS else nsS["agent"]
        if arm == "P1":
            orig = DC._spawn_weeds; box = {"rng": None, "alt": None}

            def spawn(farm, bs, wc, rng):
                if box["rng"] is not rng:
                    box["rng"] = rng; box["alt"] = random.Random((rng.getrandbits(32) ^ 0x9E3779B1) & 0xFFFFFFFF)
                return orig(farm, bs, wc, box["alt"])
            DC._spawn_weeds = spawn
        if arm == "P2":
            base = a_me

            def a_me(obs):
                act = base(obs)
                if int(obs["step"]) == FORK and len(act.get("market") or []) < 10:
                    act = copy.deepcopy(act); act["market"] = list(act.get("market") or []) + [["BUY_PRODUCT", "WHEAT", 1]]
                return act
        agents = [None, None]; agents[me] = a_me; agents[1 - me] = opp["agent"]
        land, hires, errs = [], {}, [None, None]
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
            if step % 24 == 22:
                hires[step // 24] = state[0].observation.farms[me]["hires_today"]
        f = state[0].observation.farms
        return {"bank": f[me]["money"], "opp": f[1 - me]["money"], "land": land, "hires": hires, "errors": errs,
                "status": [s.status for s in state],
                "tel": o1lib.telemetry(ns.get(arm, nsS), f[me])}

    def hook(step, state, env):
        if step != FORK - 1:
            return
        o = json.loads(json.dumps(state[me].observation))
        o["step"] = FORK; o["day"] = FORK // 24; o["hour"] = 0
        rec["dawn_cash"] = o["farms"][me]["money"]; rec["shops_d11"] = list(o["town"]["unlocked_shops"])
        rec["prefix_mismatch"] = mism[0]
        fc = {}
        for pn, prof in PROFS.items():
            fc[pn] = {arm: [fork_call(lambda arm=arm, r=r, prof=prof: rollout(o, arm, 7_000_000 + 100 * (seed % 100000) + r, prof))
                            for r in range(R)] for arm in ["off"] + ARMS}
        rec["forecast"] = fc
        rec["fc_delta"] = {pn: {arm: sum(x["bank"] - y["bank"] for x, y in zip(fc[pn][arm], fc[pn]["off"])) / R
                                for arm in ARMS} for pn in fc}
        with open(LOCKS, "a") as fh:   # lock forecasts before any real outcome exists
            fh.write(json.dumps(dict(seed=seed, me=me, t=time.time(), fc_delta=rec["fc_delta"],
                                     fc_banks={pn: {a: [x["bank"] for x in v] for a, v in d.items()} for pn, d in fc.items()})) + "\n")
        rec["real"] = {arm: fork_call(lambda arm=arm: cont(state, env, arm)) for arm in ["off"] + ARMS + PLAC}
        raise Stop

    t0 = time.time()
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            H.run_episode(ag[0], ag[1], seed=seed, on_step=hook, catch_errors=False)
    except Stop:
        pass
    off = rec["real"]["off"]
    rec["delta"] = {a: rec["real"][a]["bank"] - off["bank"] for a in ARMS + PLAC}
    rec["delta_margin"] = {a: (rec["real"][a]["bank"] - rec["real"][a]["opp"]) - (off["bank"] - off["opp"])
                           for a in ARMS + PLAC}
    rec["sec"] = round(time.time() - t0, 1)
    return rec


if __name__ == "__main__":
    out = sys.argv[1]
    for sd in map(int, sys.argv[2:]):
        r = run_seed(sd)
        with open(out, "a") as fh:
            fh.write(json.dumps(r) + "\n")
        print(sd, r["me"], "fc top", {k: round(v) for k, v in r["fc_delta"]["top"].items()},
              "real", {k: int(v) for k, v in r["delta"].items()}, "off", r["real"]["off"]["bank"],
              "mism", r["prefix_mismatch"], r["sec"], "s", flush=True)
