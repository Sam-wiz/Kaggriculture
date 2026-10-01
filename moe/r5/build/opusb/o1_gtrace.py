"""Trace the goose arm's V233 commit on a world where it bought SE but never committed. usage: o1_gtrace.py SEED"""
import contextlib, importlib.util, io, json, os, sys
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r5/build/opusb"); os.chdir(ROOT)
import harness as H
import o1lib
spec = importlib.util.spec_from_file_location("kag_dc", ROOT + "/kag_dc.py"); DC = importlib.util.module_from_spec(spec)
spec.loader.exec_module(DC); H.K = DC
seed = int(sys.argv[1]); me = seed % 2
ns = o1lib.load("G", "me"); ns["_O1_ARM"][me] = True; opp = o1lib.load("C1", "opp")
ag = [None, None]; ag[me] = ns["agent"]; ag[1 - me] = opp["agent"]
lines = []
def hook(step, state, env):
    if 264 <= step <= 292:
        o = state[me].observation; f = o.farms[me]
        mk = [x for x in (state[me].action.get("market") or []) if x and x[0] in ("BUY_LAND", "BUY_ANIMAL", "HIRE", "BUY_PRODUCT")]
        st = ns["_V233_STATES"].get(me, {})
        lines.append("%d shedGOOSE=%s inv=%s money=%d SE=%s pending=%s committed=%s orders=%s" % (
            step, o.private["shed"].get("GOOSE", 0), [i.get("GOOSE", 0) for i in o.private["inventories"]], f["money"],
            "SE" in f["unlocked_quadrants"], st.get("pending"), st.get("committed"), mk))
with contextlib.redirect_stdout(io.StringIO()):
    H.run_episode(ag[0], ag[1], seed=seed, on_step=hook)
print("\n".join(lines)); print({k: v for k, v in ns["_V233_REPORT"].items() if v})
