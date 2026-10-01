"""r6 opusb: exact-replay macro of C1's own live games (mine/opp, our seat opens like subY_C1: BUY_PRODUCT WHEAT 8)."""
import glob, gzip, json, os, sys, statistics as S, collections
sys.path.insert(0, "moe/r5/build/opus")
from concurrent.futures import ProcessPoolExecutor
C1OPEN = [["BUY_PRODUCT", "WHEAT", 8], ["SELL", "WHEAT", 3], ["BUY_SEED", "WHEAT", 1]]
OUT = "moe/r6/build/opusb/c1live.jsonl"
if __name__ == "__main__":
    import macro
    paths = []
    for p in sorted(glob.glob("mine/opp/*.json.gz"), reverse=True):
        try: d = json.load(gzip.open(p, "rt"))
        except Exception: continue
        if "Sam-wiz" not in d["teams"]: continue
        s = d["teams"].index("Sam-wiz"); a = d["actions"][1][s]
        if isinstance(a, dict) and a.get("market") == C1OPEN: paths.append(p)
        if len(paths) >= 40: break
    print(len(paths), "C1 live games", flush=True)
    if not os.path.exists(OUT):
        with ProcessPoolExecutor(max_workers=2) as ex, open(OUT, "w") as f:
            for r in ex.map(macro.job, paths): f.write(json.dumps(r, separators=(",", ":")) + "\n")
    R = [json.loads(l) for l in open(OUT)]
    R = [r for r in R if "err" not in r and all(r["match"])]
    agg = collections.defaultdict(list)
    for r in R:
        s = r["teams"].index("Sam-wiz"); se = r["seats"][s]
        agg["bank"].append(r["rewards"][s]); agg["margin"].append(r["rewards"][s] - r["rewards"][1 - s])
        agg["fprod"].append(sum(x.get("FERTILIZER", 0) for x in se["prod"])); agg["fsold"].append(sum(x["sell"].get("FERTILIZER", [0, 0])[0] for x in se["dec"]))
        agg["fbuy"].append(sum(x["buyp"].get("FERTILIZER", 0) for x in se["dec"])); agg["wbuy"].append(sum(x["buyp"].get("WHEAT", 0) for x in se["dec"]))
        agg["wsold"].append(sum(x["sell"].get("WHEAT", [0, 0])[0] for x in se["dec"])); agg["wprod"].append(sum(x.get("WHEAT", 0) for x in se["prod"]))
        agg["land"].append(tuple(st for x in se["dec"] for st in x.get("land_step", [])))
        agg["hires"].append(sum(x["hire"] for x in se["dec"]))
        for p in ("CARROT", "TOMATO", "STRAWBERRY", "EGG", "MILK", "WOOL", "MELON"): agg["p_" + p].append(sum(x.get(p, 0) for x in se["prod"]))
    print("n", len(R), "all replay-exact")
    for k, v in agg.items():
        print(k, collections.Counter(v).most_common(4) if k == "land" else round(S.mean(v), 1))
