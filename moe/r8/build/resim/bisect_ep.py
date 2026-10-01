"""Bisect resim vs recorded observations on rawkeep full replays."""
import gzip, json, glob, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resim import resim, actions_from_replay, snapshot, recorded_snapshot, diff_snap, PASS

EPS = [109508082, 109763722, 111099760, 111414755]
RK = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/mine/rawkeep/%d.json.gz"

def bisect(path, max_report=8):
    x = json.load(gzip.open(path, "rt"))
    info = x["info"]; steps = x["steps"]
    acts = actions_from_replay(x)
    rec = [recorded_snapshot(s) for s in steps]
    seen = []
    def on_step(step, state, env):
        seen.append(snapshot(state))
    r = resim(acts, info["seed"], on_step=on_step)
    firsts = {}
    first_step = None
    # seen[s] = post-state of game-step s == recorded steps[s+1]
    for s, g in enumerate(seen):
        k = s + 1
        if k >= len(rec) or rec[k] is None:
            continue
        for f, rv, gv in diff_snap(rec[k], g):
            if f not in firsts:
                firsts[f] = (k, rv, gv)
            if first_step is None:
                first_step = k
                print(f"  FIRST divergence: step {k} (day {k//24} h{k%24})")
            if len(firsts) <= max_report and first_step == k:
                print(f"    field {f}:")
                print(f"      rec: {json.dumps(rv, default=str)[:400]}")
                print(f"      got: {json.dumps(gv, default=str)[:400]}")
    print(f"  final money: rec={x['rewards']} got={r['money']}")
    print(f"  status: {r['status']}")
    if not firsts:
        print("  NO divergence in any field -- exact replay")
    else:
        print("  first-step per field:", {k: v[0] for k, v in sorted(firsts.items(), key=lambda kv: kv[1][0])})
    return r

if __name__ == "__main__":
    files = sys.argv[1:] or [RK % e for e in EPS]
    for f in files:
        print(f"=== {os.path.basename(f)} ===", flush=True)
        try:
            bisect(f)
        except Exception as e:
            import traceback; traceback.print_exc()
