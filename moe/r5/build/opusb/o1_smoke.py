"""O1 smoke: (1) S-unarmed == pristine C1 to the dollar; (2) S/C armed fire (SE bought, 6 animals placed, product
harvested); (3) prefix identity of S and C namespaces through step 263. kag_dc engine. usage: o1_smoke.py SEED SEAT"""
import contextlib, copy, importlib.util, io, json, os, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r5/build/opusb"); os.chdir(ROOT)
import harness as H
import o1lib
spec = importlib.util.spec_from_file_location("kag_dc", ROOT + "/kag_dc.py"); DC = importlib.util.module_from_spec(spec)
spec.loader.exec_module(DC); H.K = DC

seed, me = int(sys.argv[1]), int(sys.argv[2])


def game(variant, armed):
    ns = o1lib.load(variant, "me"); opp = o1lib.load("C1", "opp")
    if armed:
        ns["_O1_ARM"][me] = True
    land = []
    def hook(step, state, env):
        if any(o and o[0] == "BUY_LAND" for o in (state[me].action.get("market") or [])):
            land.append(step)
    ag = [None, None]; ag[me] = ns["agent"]; ag[1 - me] = opp["agent"]
    t0 = time.time()
    with contextlib.redirect_stdout(io.StringIO()):
        r = H.run_episode(ag[0], ag[1], seed=seed, on_step=hook)
    farm = r["state"][0].observation.farms[me]
    tel = o1lib.telemetry(ns, farm)
    keep = {k: tel[k] for k in ("se_unlocked", "se_animals", "se_kinds", "committed", "sheep_committed",
                                "sheep_workers_confirmed", "sheep_wool_harvested", "sheep_fert_collected",
                                "sheep_budget_declines", "sheep_purchase_shortfalls", "sheep_hire_shortfalls") if k in tel}
    return dict(bank=r["reward"][me], opp=r["reward"][1 - me], land=land, status=r["status"], errors=r["errors"],
                tel=keep, s=round(time.time() - t0, 1))


out = dict(seed=seed, me=me)
for name, v, a in (("c1", "C1", False), ("S_off", "S", False), ("S_on", "S", True), ("C_on", "C", True)):
    out[name] = game(v, a)
out["noop_exact"] = out["c1"]["bank"] == out["S_off"]["bank"] and out["c1"]["opp"] == out["S_off"]["opp"]
print(json.dumps(out))
