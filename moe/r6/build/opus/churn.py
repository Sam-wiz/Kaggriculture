"""r6 opus: exact wheat/fertilizer churn P&L per seat (Boey, Fourth Quadrant, + family baselines).
Replays each episode with ledger fill hooks; per seat and item: units/cash bought (BUY_PRODUCT) and
sold (SELL); same-step round trips; production of the item (harvest / collect) for the stock identity.
usage: churn.py OUT.jsonl TEAMS(comma) [WORKERS] [LIMIT_PER_TEAM]
"""
import collections, glob, gzip, json, os, sys
from concurrent.futures import ProcessPoolExecutor
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/opus")
import harness
import ledger_eps as L
PASS = {"farmer": ["PASS"], "hands": [], "market": []}


def job(path):
    L._install_hooks()
    d = json.load(gzip.open(path, "rt")); acts = d["actions"]

    def mk(seat):
        def ag(obs):
            t = obs["step"] + 1
            a = acts[t][seat] if t < len(acts) else None
            return a if isinstance(a, dict) else PASS
        return ag
    rec = dict(fills=[], prod=[], placed=[], discard=[], herd=[], shops=None)
    L.G["rec"] = rec
    try:
        r = harness.run_episode(mk(0), mk(1), seed=d["seed"], copy_obs=False)
    except Exception as e:
        L.G["rec"] = None
        return dict(ep=d["episode_id"], err=repr(e)[:200])
    L.G["rec"] = None
    out = dict(ep=d["episode_id"], date=d.get("date"), teams=d["teams"], rewards=d["rewards"],
               match=[abs(a - b) < 0.5 for a, b in zip(r["reward"], d["rewards"])], seats=[])
    for s in range(2):
        agg = {}
        steps = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0, 0, 0]))  # step->item->[bu,bc,su,sr]
        for st, p, op, it, pr in rec["fills"]:
            if p != s or op not in ("BUY_PRODUCT", "SELL") or it not in ("WHEAT", "FERTILIZER"): continue
            x = steps[st][it]
            if op == "BUY_PRODUCT": x[0] += 1; x[1] += pr
            else: x[2] += 1; x[3] += pr
        for it in ("WHEAT", "FERTILIZER"):
            bu = sum(v[it][0] for v in steps.values()); bc = sum(v[it][1] for v in steps.values())
            su = sum(v[it][2] for v in steps.values()); sr = sum(v[it][3] for v in steps.values())
            # same-step round trips: matched units min(bu,su) per step, P&L = avg sell px - avg buy px on matched units
            rt_u = 0; rt_pl = 0.0
            for v in steps.values():
                b, c, u, rv = v[it]
                m = min(b, u)
                if m: rt_u += m; rt_pl += m * (rv / u - c / b)
            prod = sum(n for st, p, k, n in rec["prod"] if p == s and k == it)
            agg[it] = dict(bu=bu, bc=bc, su=su, sr=sr, rt_u=rt_u, rt_pl=round(rt_pl, 1), prod=prod)
        out["seats"].append(agg)
    return out


if __name__ == "__main__":
    OUT = sys.argv[1]; TEAMS = set(sys.argv[2].split(",")); W = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    LIM = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 9
    cnt = collections.Counter(); paths = []
    for p in sorted(glob.glob(ROOT + "/mine/top10/*.json.gz")):
        d = json.load(gzip.open(p, "rt"))
        hit = [t for t in d["teams"] if t in TEAMS]
        if hit and any(cnt[t] < LIM for t in hit):
            paths.append(p)
            for t in hit: cnt[t] += 1
    print(len(paths), "episodes", dict(cnt), flush=True)
    with ProcessPoolExecutor(max_workers=W) as ex, open(OUT, "w") as f:
        for res in ex.map(job, paths, chunksize=4):
            f.write(json.dumps(res) + "\n")
