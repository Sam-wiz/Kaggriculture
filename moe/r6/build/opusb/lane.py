"""r6 opusb: index lane (ranks 11-20) games incl. aliases, across top10 (09-23..26), top (early Sept), opp."""
import glob, gzip, json, collections, os
ALIAS = {"Russell Kirk": "有辣条有权", "midnq": "We wanna be tomatos"}
T = [t["team"] for t in json.load(open("moe/r6/top20.json"))]
LANE = set(T[10:20]); TOP20 = set(T)
def canon(t): return ALIAS.get(t, t)
def scan(globpat):
    out = []
    for p in sorted(glob.glob(globpat)):
        try: d = json.load(gzip.open(p, "rt"))
        except Exception: continue
        tm = [canon(t) for t in d.get("teams") or []]
        if any(t in LANE for t in tm): out.append(dict(path=p, ep=d.get("episode_id"), date=d.get("date"), teams=tm, raw=d.get("teams"), rewards=d.get("rewards")))
    return out
if __name__ == "__main__":
    idx = scan("mine/top10/*.json.gz") + scan("mine/top/*.json.gz") + scan("mine/opp/*.json.gz")
    json.dump(idx, open("moe/r6/build/opusb/lane_idx.json", "w"))
    c = collections.Counter((t, i["date"] or i["path"].split("/")[1]) for i in idx for t in i["teams"] if t in LANE)
    for t in T[10:20]: print(t, {k[1]: v for k, v in c.items() if k[0] == t})
    n26 = [p for p in glob.glob("mine/top10/*.json.gz") if int(os.path.basename(p).split(".")[0]) > 113480866]
    print("09-26 landed:", len(n26))
