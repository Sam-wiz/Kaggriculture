"""r6 opusb: exact-replay macro decode (opus macro.job) of lane-team games in newly landed dumps (ep > 113480866).
Resumable; appends to macro26.jsonl."""
import glob, gzip, json, os, sys
sys.path.insert(0, "moe/r5/build/opus")
from concurrent.futures import ProcessPoolExecutor
LANE_RAW = {"KawattaTaido", "Azat Akhtyamov", "有辣条有权", "Russell Kirk", "kigasudayooo", "TheEggman", "Arda Ceylan",
            "atsushi11o7", "Yizhou", "My second life", "We wanna be tomatos", "midnq", "nah id win"}
OUT = "moe/r6/build/opusb/macro26.jsonl"
if __name__ == "__main__":
    import macro
    done = set()
    if os.path.exists(OUT):
        for l in open(OUT): done.add(json.loads(l)["ep"])
    paths = []
    for p in sorted(glob.glob("mine/top10/*.json.gz")):
        e = int(os.path.basename(p).split(".")[0])
        if e <= 113480866 or e in done: continue
        try: d = json.load(gzip.open(p, "rt"))
        except Exception: continue
        if any(t in LANE_RAW for t in d["teams"]): paths.append(p)
    print(len(paths), "to decode", flush=True)
    with ProcessPoolExecutor(max_workers=2) as ex, open(OUT, "a") as f:
        for res in ex.map(macro.job, paths):
            f.write(json.dumps(res, separators=(",", ":")) + "\n"); f.flush()
            print(res.get("ep"), res.get("teams"), res.get("match"), res.get("err"), flush=True)
