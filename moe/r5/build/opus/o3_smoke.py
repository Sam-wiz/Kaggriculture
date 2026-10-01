"""O3 smoke: o3lib unarmed == pristine C1 (full game, kag_dc) to the dollar. usage: o3_smoke.py SEED"""
import contextlib, importlib.util, io, json, os, sys
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r5/build/opus"); os.chdir(ROOT)
import harness as H
import o3lib
spec = importlib.util.spec_from_file_location("kag_dc", ROOT + "/kag_dc.py"); DC = importlib.util.module_from_spec(spec)
spec.loader.exec_module(DC); H.K = DC
seed = int(sys.argv[1]); me = seed % 2
with contextlib.redirect_stdout(io.StringIO()):
    a = H.load_agent(ROOT + "/subY_C1_predict2.py", "p0"); b = H.load_agent(ROOT + "/subY_C1_predict2.py", "p1")
    r0 = H.run_episode(a, b, seed=seed)
    ns = o3lib.load("me"); opp = o3lib.load("opp")
    ag = [None, None]; ag[me] = ns["agent"]; ag[1 - me] = opp["agent"]
    r1 = H.run_episode(ag[0], ag[1], seed=seed)
print(json.dumps(dict(seed=seed, pristine=r0["reward"], o3_unarmed=r1["reward"], exact=r0["reward"] == r1["reward"],
                      tel=ns["_O3_TEL"], opp_tel=opp["_O3_TEL"])))
