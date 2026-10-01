"""run fam0 vs an opponent on the official Python engine (harness) with dawn telemetry.
usage: run0.py OPP SEED [quiet]"""
import sys, os, time, importlib.util
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0, ROOT)
import harness
def load(path):
    spec = importlib.util.spec_from_file_location("m%d" % abs(hash(path)), path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.agent
opp = sys.argv[1]; seed = int(sys.argv[2]); quiet = len(sys.argv) > 3
A = load(ROOT + "/moe/r5/build/opus/fam0.py")
B = opp if opp in ("pass", "random", "starter") else load(ROOT + "/" + opp)
tel = []
def on_step(step, state, env):
    ob = state[0].observation
    if (step + 1) % 24 == 0:
        f = ob.farms[0]; h = {}
        for row in f["tiles"]:
            for t in row:
                if isinstance(t, dict):
                    k = t.get("animal") or ("P_" + t["crop"][:3] if t.get("kind") == "PLANT" else t.get("kind"))
                    h[k] = h.get(k, 0) + 1
        tel.append((step // 24 + 1, int(f["money"]), int(ob.farms[1]["money"]), len(f.get("unlocked_quadrants") or []), h))
t0 = time.time()
r = harness.run_episode(A, B, seed=seed, on_step=on_step)
if not quiet:
    for x in tel: print(x)
print("RESULT", opp, seed, r["reward"], r.get("status"), "%.1fs" % (time.time() - t0))
