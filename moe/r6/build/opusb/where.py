"""r6 opusb: find every recorded game of ranks 11-20 across all local archives (by team name)."""
import glob, gzip, json, collections, os, sys
T = [t["team"] for t in json.load(open("moe/r6/top20.json"))]
LANE = T[10:20]
hits = collections.defaultdict(list); names = collections.Counter()
for g in ["mine/top10/*.json.gz", "mine/opp/*.json.gz", "mine/top/*.json.gz", "mine/top3/*", "mine/loss/*", "mine/rawtop/*"]:
    for p in glob.glob(g):
        try:
            d = json.load(gzip.open(p, "rt")) if p.endswith(".gz") else json.load(open(p))
        except Exception as e:
            continue
        teams = d.get("teams") or (d.get("info", {}) or {}).get("TeamNames") or []
        for t in teams: names[(g.split("/")[1], t)] += 1
        for s, t in enumerate(teams):
            if t in LANE: hits[t].append((g.split("/")[1], os.path.basename(p), s, d.get("date"), teams[1 - s] if len(teams) == 2 else None))
for t in LANE:
    L = hits[t]; print(t, len(L), collections.Counter(x[0] for x in L), collections.Counter(x[3] for x in L).most_common(6))
json.dump({t: hits[t] for t in LANE}, open("moe/r6/build/opusb/where.json", "w"))
json.dump([[k[0], k[1], v] for k, v in names.items()], open("moe/r6/build/opusb/allnames.json", "w"))
