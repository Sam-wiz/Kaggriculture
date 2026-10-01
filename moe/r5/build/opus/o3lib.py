"""O3 (tomato program) as a switchable option on C1's own executor.

C1 is land-bound from d15 (median 0 empty tiles d15-24, c1macro.jsonl), so the only tomato program it can execute
without a new executor is its own V219: at the d18 dawn (step 432) buy SE + 10 tomato seeds, plant SE rows 5-6,
water d19-25, harvest d26-29. Natively it is world-gated by CXTB (projected revenue of 80 units >= $9,000).
O3 arm per seat, ns['_O3_ARM'][player]:
  None  -> native C1 (CXTB decides)
  'on'  -> CXTB revenue gate removed; the structural conditions stay (3 quadrants, SE rows 5-6 locked, $12k cash,
           no tomato stock, no later native BUY_LAND/PLANT TOMATO)
  'off' -> never commit
The step-432 decision is logged to ns['_O3_TEL'][player] = {native, struct, rev}.
"""
import contextlib, io

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
C1 = ROOT + "/subY_C1_predict2.py"
_SRC = []


def load(tag=""):
    if not _SRC:
        _SRC.append(open(C1).read())
    ns = {"__name__": "o3_%s" % tag, "_O3_ARM": {}, "_O3_TEL": {}}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(_SRC[0], C1, "exec"), ns)
    native_q = ns["_v219_qualifies"]

    def struct_only(obs, native):
        keep = ns["_CXTB_MIN_REVENUE"]
        ns["_CXTB_MIN_REVENUE"] = -float("inf")
        try:
            return bool(ns["_cxtb_qualifies"](obs, native))
        finally:
            ns["_CXTB_MIN_REVENUE"] = keep

    def q(obs, native):
        p = int(obs["player"])
        base = native_q(obs, native)
        tel = {"native": bool(base), "struct": struct_only(obs, native),
               "rev": round(ns["_cxtb_expected_revenue"](obs))}
        ns["_O3_TEL"][p] = tel
        arm = ns["_O3_ARM"].get(p)
        if arm is None:
            return base
        return tel["struct"] if arm == "on" else False

    ns["_v219_qualifies"] = q
    return ns


def telemetry(ns, farm, player):
    rep = {k: v for k, v in ns.get("_V219_REPORT", {}).items() if isinstance(v, (int, float))}
    rep.update(ns["_O3_TEL"].get(player, {}))
    se = [farm["tiles"][y][x] for y in range(5, 10) for x in range(5, 10)]
    rep["se_unlocked"] = "SE" in farm["unlocked_quadrants"]
    rep["se_tomato_tiles"] = sum(isinstance(t, dict) and t.get("crop") == "TOMATO" for t in se)
    rep["committed"] = bool(ns.get("_V219_STATES", {}).get(player, {}).get("committed"))
    return rep
