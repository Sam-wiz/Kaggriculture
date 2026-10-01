"""Arm R retrodiction: shepherd (our recorded seat) vs candidate on the 18 WLV seeds, closed-loop. usage: rretro.py TAG name=path ..."""
import sys, json, gzip
RARGS = list(sys.argv); sys.argv = [sys.argv[0]]
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/run.py").read().split('\nif __name__ == "__main__":')[0])
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/rdiv.py").read().split('\nif __name__ == "__main__":')[0])
if __name__ == "__main__":
    tag = RARGS[1]; cands = [a.split("=", 1) for a in RARGS[2:]]
    T = tapes(); jobs = []
    for n, p in cands:
        for r in T:
            d = json.load(gzip.open(f"mine/opp/{r['ep']}.json.gz", "rt"))
            jobs.append(("shep", "subW_shepherd.py", n, p, d["seed"], r["seat"]))
    out = f"moe/r3/build/opus/rretro_{tag}.jsonl"; open(out, "w").close()
    pool(closed, jobs, out)
