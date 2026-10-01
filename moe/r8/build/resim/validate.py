"""Validate resim exactness over mine/top10 tapes.

Usage: python validate.py [limit] [team-filter-substr]
Writes nothing; prints per-episode and aggregate match stats.
"""
import gzip, json, glob, os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resim import resim

T10 = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/mine/top10"


def check_one(path):
    try:
        x = json.load(gzip.open(path, "rt"))
    except Exception:
        return None
    acts = x.get("actions") or []
    rec = x.get("rewards")
    if not acts or not rec or x.get("seed") is None:
        return None
    r = resim(acts, x["seed"])
    got = r["money"]
    errs = [abs(got[i] - rec[i]) for i in range(2)]
    rel = [errs[i] / max(1.0, abs(rec[i])) for i in range(2)]
    return {
        "ep": x.get("episode_id"), "teams": x.get("teams"), "seed": x.get("seed"),
        "rec": rec, "got": got, "exact": max(errs) < 1.0, "within1": max(rel) <= 0.01,
        "maxrel": max(rel), "status": r["status"],
    }


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    teamf = sys.argv[2] if len(sys.argv) > 2 else None
    files = sorted(glob.glob(T10 + "/*.json.gz"))
    random.Random(7).shuffle(files)
    n = ok1 = okx = 0
    fails = []
    for f in files:
        if teamf:
            try:
                head = json.load(gzip.open(f, "rt"))
                if teamf not in (head.get("teams") or []):
                    continue
            except Exception:
                continue
        c = check_one(f)
        if c is None:
            continue
        n += 1
        okx += c["exact"]; ok1 += c["within1"]
        if not c["within1"]:
            fails.append(c)
            print("MISS", os.path.basename(f), c["teams"], "rec", c["rec"], "got", c["got"], flush=True)
        if n >= limit:
            break
    print(f"\n{n} episodes: exact={okx} ({okx/max(1,n):.0%}), within1%={ok1} ({ok1/max(1,n):.0%})")
