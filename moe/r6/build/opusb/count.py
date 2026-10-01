"""r6 opusb: per-team seat counts in macro.jsonl (09-23..25 dump) and by date."""
import json, collections
T = [t["team"] for t in json.load(open("moe/r6/top20.json"))]
c = collections.Counter(); cd = collections.defaultdict(collections.Counter)
subs = collections.defaultdict(collections.Counter)
for l in open("moe/r5/build/opus/macro.jsonl"):
    d = json.loads(l)
    for s in range(2):
        c[d["teams"][s]] += 1; cd[d["teams"][s]][d["date"]] += 1
for i, t in enumerate(T, 1):
    print(i, t, c[t], dict(cd[t]))
print("all teams:", len(c)); print(c.most_common(45))
