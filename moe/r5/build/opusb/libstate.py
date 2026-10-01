"""Per-dawn state signatures of every library tape (robust teams), by exact replay on the official Python engine.
out: {"<ep>:<seat>": [[sig100, money] for dawn 0..29]}   sig: one char per tile (see SIG)
usage: libstate.py OUT.json
"""
import glob, gzip, json, sys
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r5/build/opusb")
import harness as H
import ts

CROP = {"WHEAT": "w", "CARROT": "c", "TOMATO": "t", "STRAWBERRY": "s", "MELON": "m"}
ANI = {"GOOSE": "G", "COW": "C", "SHEEP": "S"}


def sig(farm):
    out = []
    for row in farm["tiles"]:
        for t in row:
            if t is None:
                out.append(".")
            elif t == "LOCKED":
                out.append("L")
            elif t.get("kind") == "WEED":
                out.append("x")
            elif t.get("kind") == "PLANT":
                out.append(CROP.get(t.get("crop"), "?"))
            elif t.get("kind") in ("COOP", "PASTURE"):
                a = t.get("animal")
                out.append(ANI.get(a, "?") if a else ("g" if t["kind"] == "COOP" else "p"))
            else:
                out.append("?")
    return "".join(out)


if __name__ == "__main__":
    teams = set(ts.LIB_TEAMS); res = {}
    for f in sorted(glob.glob(ROOT + "/mine/top10/*.json.gz")):
        d = json.load(gzip.open(f, "rt"))
        seats = [k for k in (0, 1) if d["teams"][k] in teams]
        if not seats:
            continue
        acts = d["actions"]
        rec = {k: [] for k in seats}

        def on_step(s, state, env):
            if (s + 1) % 24 == 0 and s + 1 < 720:
                farms = state[0].observation.farms
                for k in seats:
                    rec[k].append([sig(farms[k]), farms[k]["money"]])
        tp = [lambda o, k=k: (acts[o["step"] + 1][k] if o["step"] + 1 < len(acts) and isinstance(acts[o["step"] + 1][k], dict) else ts.PASS) for k in (0, 1)]
        # dawn 0 signature
        r = H.run_episode(tp[0], tp[1], seed=d["seed"], on_step=on_step, copy_obs=False)
        for k in seats:
            res["%s:%d" % (d["episode_id"], k)] = [["L" * 0, 3000]] + rec[k]   # dawn 0 placeholder (all start equal)
    json.dump(res, open(sys.argv[1], "w"))
    print("tapes", len(res))
