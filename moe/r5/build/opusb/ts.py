"""TS — tape-switching dawn planner (Architecture B prototype, build lane r5).

Library: recorded seat streams ("tapes") of the robust top-family teams (mine/top10). At step 0 and at each planning
dawn, candidate tapes are rolled forward FROM OUR REAL OBSERVED STATE to the end of the season with the official
Python interpreter (state rebuilt from the observation; opponent private state unknown -> empty; opponent acts PASS;
future weeds/shops from sampled seeds, common across candidates). We follow the candidate with the best mean final
bank; "stay" is always a candidate and a switch needs a margin. The rollout measures splice damage directly (dead ops,
unwatered plants on tiles the new tape does not know), so tapes need not be state-compatible.

Config via module globals (set before the first call): LIB_TEAMS, LIB_MAX, M (candidates/dawn), R (seeds/candidate),
PLAN_DAYS, SWITCH_MARGIN, TIME_CAP (s per planning call, wall), OPP ('pass').
"""
import copy, glob, gzip, json, os, random, time
from kaggle_environments.envs.kaggriculture import kaggriculture as K

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
LIB_TEAMS = ("THIRD FARM CLUB", "Boey", "吃白饭的大肥鱼", "Majkel1337")
LIB_MAX = 10 ** 9
M = 12
R = 2
PLAN_DAYS = set(range(1, 29))
SWITCH_MARGIN = 500.0
TIME_CAP = 6.0
STEP0_M = 24
PASS = {"farmer": ["PASS"], "hands": [], "market": []}
CFG = {"episodeSteps": 720, "actTimeout": 1, "runTimeout": 1200, "boardSize": 10, "startingMoney": 3000,
       "maxMarketOrdersPerTurn": 10, "turnsPerDay": 24, "shedCapacity": 100, "weedSpawnChance": 0.005,
       "townShopUnlockInterval": 3, "townShopSellInterval": 4, "townCenterSellInterval": 24,
       "farmHandCostMult": 1, "seed": None}


class S(dict):
    __setattr__ = dict.__setitem__

    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError(k)


def _st(o):
    if isinstance(o, list):
        return [_st(v) for v in o]
    if isinstance(o, dict):
        return S({k: _st(v) for k, v in o.items()})
    return o


class _Env:
    def __init__(self, seed):
        c = dict(CFG); c["seed"] = seed
        self.configuration = S(c); self.done = False; self.info = {"seed": seed}


class _AS:
    __slots__ = ("observation", "action", "status", "reward")

    def __init__(self, o):
        self.observation = o; self.action = None; self.status = "ACTIVE"; self.reward = 0.0


LIB = []


def load_lib():
    if LIB:
        return LIB
    for f in sorted(glob.glob(ROOT + "/mine/top10/*.json.gz")):
        d = json.load(gzip.open(f, "rt"))
        for seat in (0, 1):
            if d["teams"][seat] in LIB_TEAMS:
                acts = [a[seat] if isinstance(a[seat], dict) else PASS for a in d["actions"]]
                LIB.append(dict(ep=d["episode_id"], seat=seat, team=d["teams"][seat], shops=d["shops"] or [],
                                rec=d["rewards"][seat], acts=acts))
                if len(LIB) >= LIB_MAX:
                    return LIB
    return LIB


def tape_act(e, s):
    a = e["acts"][s + 1] if s + 1 < len(e["acts"]) else PASS
    return a if isinstance(a, dict) else PASS


OPP_DAYS = 2      # opponent model: replay its observed per-hour net market deltas, mean over the last OPP_DAYS days
OPP_SCALE = 1.0
OPP_MODE = "profile"   # profile | hour | none
PROF = None
PROF_PATH = "oppprof.json"


def load_prof():
    global PROF
    if PROF is None:
        PROF = json.load(open(ROOT + "/moe/r5/build/opusb/" + PROF_PATH))["mean"]
    return PROF


INJ_BEFORE = True


def _inject(market, opp_inject, s):
    d = opp_inject(s) if callable(opp_inject) else opp_inject.get(s % 24)
    if d:
        inv = market["inventory"]
        for k, v in d.items():
            inv[k] = inv[k] + v
        K._refresh_prices(market)


def rollout(obs, e, seed, opp_private=None, opp_policy=None, opp_inject=None):
    """Play tape e for us from obs.step to the end; returns our final money (and theirs).
    opp_inject: {hour: {item: delta}} added to market inventory after each step (opponent pattern model)."""
    me = obs["player"]
    farms = copy.deepcopy(obs["farms"]); market = copy.deepcopy(obs["market"]); town = copy.deepcopy(obs["town"])
    privs = [None, None]
    privs[me] = copy.deepcopy(obs["private"])
    privs[1 - me] = copy.deepcopy(opp_private) if opp_private is not None else {"shed": {}, "seeds": {}, "inventories": [{}]}
    st = [_AS(S(player=i, farms=farms, market=market, town=town, private=privs[i], step=obs["step"],
                day=obs["day"], hour=obs["hour"])) for i in (0, 1)]
    env = _Env(seed)
    for s in range(obs["step"], 720):
        st[0].observation.step = s; st[1].observation.step = s
        st[me].action = tape_act(e, s)
        st[1 - me].action = opp_policy(st[1 - me].observation, s) if opp_policy else PASS
        if opp_inject and INJ_BEFORE:
            _inject(market, opp_inject, s)
        K.interpreter(st, env)
        if opp_inject and not INJ_BEFORE:
            _inject(market, opp_inject, s)
        if st[0].status != "ACTIVE":
            break
    return farms[me]["money"], farms[1 - me]["money"]


def shadow_delta(prev_obs, my_action, obs):
    """Opponent's exact net market effect over one step: actual inventory minus a one-step re-simulation of our
    own action with the opponent passing (our fills do not depend on the opponent: sells always fill, buys are
    fixed-price)."""
    me = prev_obs["player"]
    farms = copy.deepcopy(prev_obs["farms"]); market = copy.deepcopy(prev_obs["market"]); town = copy.deepcopy(prev_obs["town"])
    privs = [None, None]
    privs[me] = copy.deepcopy(prev_obs["private"]); privs[1 - me] = {"shed": {}, "seeds": {}, "inventories": [{}]}
    st = [_AS(S(player=i, farms=farms, market=market, town=town, private=privs[i], step=prev_obs["step"],
                day=prev_obs["day"], hour=prev_obs["hour"])) for i in (0, 1)]
    st[me].action = my_action; st[1 - me].action = PASS
    K.interpreter(st, _Env(1))
    a, b = obs["market"]["inventory"], market["inventory"]
    return {k: a[k] - b[k] for k in a if a[k] != b[k]}


def _prefix_score(shops, known):
    n = 0
    for a, b in zip(shops, known):
        if a != b:
            break
        n += 1
    ms = sum(min(shops[:len(known)].count(x), known.count(x)) for x in set(known))
    return (n, ms)


CAND_MODE = "prefix"   # prefix | nn (state-similar retrieval: tile Hamming at this dawn - SHOP_W * shop prefix)
SHOP_W = 4.0
MONEY_W = 1.0 / 2000
LS = None


def load_ls():
    global LS
    if LS is None:
        LS = json.load(open(ROOT + "/moe/r5/build/opusb/libstate.json"))
    return LS


def _sig(farm):
    import libstate
    return libstate.sig(farm)


class Planner:
    def __init__(self):
        self.cur = None; self.rng = random.Random(1234); self.log = []; self.plan_time = 0.0; self.plan_calls = 0
        self.prev = None; self.prev_act = None; self.deltas = {}; self.shadow_err = 0

    def observe(self, obs):
        if self.prev is not None and self.prev["step"] + 1 == obs["step"]:
            try:
                self.deltas[self.prev["step"]] = shadow_delta(self.prev, self.prev_act, obs)
            except Exception:
                self.shadow_err += 1

    def remember(self, obs, act):
        self.prev = copy.deepcopy(obs); self.prev_act = copy.deepcopy(act)

    def opp_model(self, step):
        if OPP_MODE == "none":
            return None
        if OPP_MODE == "profile":
            prof = load_prof()
            oc, pc = {}, {}
            for t, d in self.deltas.items():
                for k, v in d.items():
                    oc[k] = oc.get(k, 0) + v
            for t in range(0, step):
                for k, v in prof[t].items():
                    pc[k] = pc.get(k, 0) + v
            sc = {k: OPP_SCALE * min(3.0, max(0.3, (max(0.0, oc.get(k, 0)) + 30.0) / (max(0.0, pc.get(k, 0)) + 30.0)))
                  for k in set(oc) | set(pc)}
            return lambda s, prof=prof, sc=sc: {k: v * sc.get(k, OPP_SCALE) for k, v in prof[s].items()}
        if OPP_DAYS <= 0 or not self.deltas:
            return None
        out = {}
        for h in range(24):
            acc = {}; n = 0
            for d in range(1, OPP_DAYS + 1):
                t = step - 24 * d + h
                if t in self.deltas:
                    n += 1
                    for k, v in self.deltas[t].items():
                        acc[k] = acc.get(k, 0) + v
            if n:
                out[h] = {k: OPP_SCALE * v / n for k, v in acc.items()}
        return out

    def plan(self, obs):
        t0 = time.perf_counter()
        lib = load_lib()
        known = list(obs["town"]["unlocked_shops"])
        if self.cur is None:
            cands = self.rng.sample(lib, min(STEP0_M, len(lib)))
        else:
            if CAND_MODE == "nn":
                ls = load_ls(); d = obs["day"]; me = obs["player"]
                mine = _sig(obs["farms"][me]); mon = obs["farms"][me]["money"]
                def dist(e):
                    rec = ls.get("%s:%d" % (e["ep"], e["seat"]))
                    if not rec or d >= len(rec):
                        return 1e9
                    sg, m = rec[d]
                    ham = sum(1 for a, b in zip(sg, mine) if a != b) if sg else 0
                    return ham + MONEY_W * abs(m - mon) - SHOP_W * _prefix_score(e["shops"], known)[0] + 1e-3 * self.rng.random()
                ranked = sorted(lib, key=dist)
            else:
                ranked = sorted(lib, key=lambda e: _prefix_score(e["shops"], known) + (self.rng.random(),), reverse=True)
            cands = [self.cur] + [e for e in ranked if e is not self.cur][:M]
        seeds = [self.rng.randrange(1, 2 ** 31) for _ in range(R)]
        inj = self.opp_model(obs["step"])
        scores = []
        for e in cands:
            if time.perf_counter() - t0 > TIME_CAP and scores:
                break
            v = sum(rollout(obs, e, sd, opp_inject=inj)[0] for sd in seeds) / len(seeds)
            scores.append((v, e))
        best_v, best = max(scores, key=lambda x: x[0])
        cur_v = scores[0][0] if self.cur is not None else None
        switched = False
        if self.cur is None or (best is not self.cur and best_v > cur_v + SWITCH_MARGIN):
            self.cur = best; switched = True
        dt = time.perf_counter() - t0
        self.plan_time += dt; self.plan_calls += 1
        self.log.append(dict(step=obs["step"], n=len(scores), best=round(best_v), cur=None if cur_v is None else round(cur_v),
                             sw=switched, team=self.cur["team"], ep=self.cur["ep"], dt=round(dt, 2),
                             match=_prefix_score(self.cur["shops"], known)[0]))


_P = Planner()


def agent(obs, configuration=None):
    s = obs["step"]
    _P.observe(obs)
    if _P.cur is None or (s % 24 == 0 and obs["day"] in PLAN_DAYS):
        _P.plan(obs)
    a = tape_act(_P.cur, s)
    _P.remember(obs, a)
    return a
