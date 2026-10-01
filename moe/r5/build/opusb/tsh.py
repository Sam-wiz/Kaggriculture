"""Horizon ablation of TS-NN (sonnet r5 THREAD 21:52 gate 1): same pool/seeds/config as ts_NN.jsonl, but each dawn
rollout stops after HDAYS days (the day + HDAYS-1 continuation) and is scored by terminal value instead of the
end-of-season bank. usage: tsh.py OUT.jsonl SEED0 N WORKERS HDAYS [key=value ...]
Terminal value = money + shed/inventories at current price (animals at cost) + seeds at cost
               + plant yield_units x price + placed animals at cost + their held yield x product price."""
import copy, json, sys
from multiprocessing import Pool
sys.path.insert(0, "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r5/build/opusb")
import tsgame, ts
K = ts.K
HDAYS = int(sys.argv[5]) if len(sys.argv) > 5 and sys.argv[5].isdigit() else 4
import os
H0FULL = os.environ.get("H0FULL") == "1"   # step-0 tape pick keeps the full-season horizon (isolates the dawn-switch horizon)


def tvalue(farm, priv, market):
    p = market["prices"]
    v = farm["money"]
    def item(k, n):
        if k in K.ANIMALS:
            return n * K.ANIMALS[k]["cost"]
        return n * p.get(k, 0)
    for k, n in (priv.get("shed") or {}).items():
        v += item(k, n)
    for inv in priv.get("inventories") or []:
        for k, n in (inv or {}).items():
            v += item(k, n)
    for k, n in (priv.get("seeds") or {}).items():
        v += n * K.CROPS[k]["seed"]
    for row in farm["tiles"]:
        for t in row:
            if isinstance(t, dict):
                if t.get("kind") == "PLANT":
                    v += (t.get("yield_units") or 0) * p.get(t["crop"], 0)
                elif t.get("animal"):
                    a = K.ANIMALS[t["animal"]]
                    v += a["cost"] + (t.get("yield_units") or 0) * p.get(a["product"], 0)
    return v


def rollout_h(obs, e, seed, opp_private=None, opp_policy=None, opp_inject=None):
    me = obs["player"]
    farms = copy.deepcopy(obs["farms"]); market = copy.deepcopy(obs["market"]); town = copy.deepcopy(obs["town"])
    privs = [None, None]
    privs[me] = copy.deepcopy(obs["private"])
    privs[1 - me] = copy.deepcopy(opp_private) if opp_private is not None else {"shed": {}, "seeds": {}, "inventories": [{}]}
    st = [ts._AS(ts.S(player=i, farms=farms, market=market, town=town, private=privs[i], step=obs["step"],
                      day=obs["day"], hour=obs["hour"])) for i in (0, 1)]
    env = ts._Env(seed)
    end = 720 if (H0FULL and obs["step"] == 0) else min(720, obs["step"] + 24 * HDAYS)
    for s in range(obs["step"], end):
        st[0].observation.step = s; st[1].observation.step = s
        st[me].action = ts.tape_act(e, s)
        st[1 - me].action = opp_policy(st[1 - me].observation, s) if opp_policy else ts.PASS
        if opp_inject and ts.INJ_BEFORE:
            ts._inject(market, opp_inject, s)
        K.interpreter(st, env)
        if st[0].status != "ACTIVE":
            break
    if end >= 720:
        return farms[me]["money"], farms[1 - me]["money"]
    return tvalue(farms[me], st[me].observation.private, market), 0


ts.rollout = rollout_h

if __name__ == "__main__":
    out, s0, n, w = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    cfg = dict(kv.split("=", 1) for kv in sys.argv[6:])
    jobs = [dict(seed=s0 + i, pos=i % 2, cfg=cfg, hdays=HDAYS) for i in range(n)]
    with Pool(w) as pl, open(out, "a") as f:
        for res in pl.imap_unordered(tsgame.job, jobs):
            f.write(json.dumps(res, ensure_ascii=False) + "\n"); f.flush()
            print(res.get("seed"), res.get("pos"), res.get("me"), res.get("opp"), res.get("win"), "plan",
                  res.get("plan_s"), "sw", res.get("switches"), "pred", res.get("final_pred"), "wall", res.get("wall"),
                  "err", res.get("errors"), flush=True)
