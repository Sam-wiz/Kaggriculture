"""r6 opusb: pull lane-team episodes (with aliases) out of opus's exact-replay macro.jsonl -> lane_macro.jsonl"""
import json
ALIAS = {"Russell Kirk": "有辣条有权", "midnq": "We wanna be tomatos", "nah id win": "We wanna be tomatos"}
T = [t["team"] for t in json.load(open("moe/r6/top20.json"))]
LANE = set(T[10:20])
n = 0
with open("moe/r6/build/opusb/lane_macro.jsonl", "w") as f:
    for src in ["moe/r5/build/opus/macro.jsonl"] + ["moe/r6/build/opusb/macro26.jsonl"]:
        try: fh = open(src)
        except FileNotFoundError: continue
        for l in fh:
            d = json.loads(l)
            if any(ALIAS.get(t, t) in LANE for t in d["teams"]):
                f.write(l); n += 1
print(n)
