"""O1 probe: when does C1 buy land, what is its dawn cash, how many quadrants at end. C1 vs C1, kag_dc engine."""
import contextlib, importlib.util, io, json, os, sys
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.path.insert(0, ROOT); os.chdir(ROOT)
import harness as H
spec = importlib.util.spec_from_file_location('kag_dc', ROOT + '/kag_dc.py'); DC = importlib.util.module_from_spec(spec); spec.loader.exec_module(DC)
H.K = DC
seed = int(sys.argv[1])
with contextlib.redirect_stdout(io.StringIO()):
    A = H.load_agent(ROOT + "/subY_C1_predict2.py", "pa"); B = H.load_agent(ROOT + "/subY_C1_predict2.py", "pb")
rec = {"land": [[], []], "dawn": [[], []]}
def hook(step, state, env):
    f = state[0].observation.farms
    for i in range(2):
        if any(o and o[0] == "BUY_LAND" for o in (state[i].action.get("market") or [])):
            rec["land"][i].append((step, list(f[i]["unlocked_quadrants"]), f[i]["money"]))
        if (step + 1) % 24 == 0:
            rec["dawn"][i].append(f[i]["money"])
with contextlib.redirect_stdout(io.StringIO()):
    r = H.run_episode(A, B, seed=seed, on_step=hook)
print(json.dumps(dict(seed=seed, bank=r["reward"], land=rec["land"], dawn0=rec["dawn"][0], shops=r["state"][0].observation.town["unlocked_shops"])))
