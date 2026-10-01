"""Where does O1's money go? Cash-flow ledger of our seat from step 264 on, off vs armed, same world (kag_dc).
Wraps the engine's per-unit commit, hire and land functions. usage: o1_decomp.py SEED ARM(S|C)"""
import contextlib, importlib.util, io, json, os, sys
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r5/build/opusb"); os.chdir(ROOT)
import harness as H
import o1lib
spec = importlib.util.spec_from_file_location("kag_dc", ROOT + "/kag_dc.py"); DC = importlib.util.module_from_spec(spec)
spec.loader.exec_module(DC); H.K = DC
seed, arm = int(sys.argv[1]), sys.argv[2]; me = seed % 2


def ledger(variant, armed):
    ns = o1lib.load(variant, "me"); opp = o1lib.load("C1", "opp")
    if armed:
        ns["_O1_ARM"][me] = True
    L, cur = {}, {"step": 0, "farm": None}
    oc, oh, ol = DC._commit_unit, DC._do_hire, DC._do_buy_land

    def add(k, units, usd):
        u, d = L.get(k, (0, 0)); L[k] = (u + units, d + usd)

    def commit(op, item, price, farm, private, market, cap=100):
        ok = oc(op, item, price, farm, private, market, cap)
        if ok and farm is cur["farm"] and cur["step"] >= 264:
            add(op + ":" + item, 1, price if op == "SELL" else -price)
        return ok

    def hire(farm, private, bs, mult=1):
        m0 = farm["money"]; r = oh(farm, private, bs, mult)
        if farm is cur["farm"] and cur["step"] >= 264:
            add("HIRE", int(farm["money"] != m0), farm["money"] - m0)
        return r

    def land(farm, bs):
        m0 = farm["money"]; r = ol(farm, bs)
        if farm is cur["farm"] and cur["step"] >= 264:
            add("LAND", int(farm["money"] != m0), farm["money"] - m0)
        return r
    DC._commit_unit, DC._do_hire, DC._do_buy_land = commit, hire, land

    ag = [None, None]; ag[me] = ns["agent"]; ag[1 - me] = opp["agent"]

    def a_me(obs):
        cur["step"] = int(obs["step"])
        return ns["agent"](obs)
    ag[me] = a_me
    st0 = {}

    def hook(step, state, env):
        cur["farm"] = state[0].observation.farms[me]
        if step == 263:
            st0["money"] = cur["farm"]["money"]
    cur_first = {}
    with contextlib.redirect_stdout(io.StringIO()):
        # farm dict identity is stable across the game; bind it after init via the first hook
        r = H.run_episode(ag[0], ag[1], seed=seed, on_step=hook)
    DC._commit_unit, DC._do_hire, DC._do_buy_land = oc, oh, ol
    shed = dict(r["state"][me].observation.private["shed"])
    return dict(bank=r["reward"][me], m264=st0["money"], L=L, shed={k: v for k, v in shed.items() if v})


off = ledger("S", False); on = ledger(arm, True)
keys = sorted(set(off["L"]) | set(on["L"]), key=lambda k: -abs(on["L"].get(k, (0, 0))[1] - off["L"].get(k, (0, 0))[1]))
print("seed %d me %d arm %s: bank off %.0f on %.0f delta %+.0f (cash at 264: %.0f / %.0f)" % (
    seed, me, arm, off["bank"], on["bank"], on["bank"] - off["bank"], off["m264"], on["m264"]))
print("%-22s %16s %16s %10s" % ("flow (step>=264)", "off units/$", "on units/$", "delta $"))
tot = 0
for k in keys:
    a, b = off["L"].get(k, (0, 0)), on["L"].get(k, (0, 0))
    if a == b:
        continue
    tot += b[1] - a[1]
    print("%-22s %7d %8.0f %7d %8.0f %+10.0f" % (k, a[0], a[1], b[0], b[1], b[1] - a[1]))
print("sum of flow deltas %+.0f; unsold shed at end off %s | on %s" % (tot, off["shed"], on["shed"]))
