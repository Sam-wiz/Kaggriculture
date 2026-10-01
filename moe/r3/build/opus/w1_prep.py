"""W1 prep: fresh test seeds (seedindex [1356:1376]) + library seeds covering every test pair (6 per pair)."""
import json, random, sys
sys.argv=[sys.argv[0]]
exec(open("moe/r3/build/opus/pairs.py").read().split("if __name__")[0])
wl = json.load(open("moe/r3/opus_scratch/wl_games.json"))
idx = json.load(open("data/seedindex_900000_1400.json"))
fresh = [r["seed"] for r in idx][1356:1376]
test = {g["seed"]: pair(g["seed"]) for g in wl}
test.update({s: pair(s) for s in fresh})
need = {}
for s, p in test.items(): need[p] = 0
rng = random.Random(20260925); lib = []
taken = set(test)
while any(v < 6 for v in need.values()):
    s = rng.randrange(10**8, 2 * 10**9)
    if s in taken: continue
    p = pair(s)
    if p in need and need[p] < 6:
        need[p] += 1; lib.append(s); taken.add(s)
json.dump(dict(fresh=fresh, wlv=[dict(seed=g["seed"], seat=g["seat"], ep=g["ep"]) for g in wl],
               test_pairs={str(k): v for k, v in test.items()}, lib_seeds=lib), open("moe/r3/build/opus/w1_seeds.json", "w"))
print(len(need), "pairs;", len(lib), "library seeds")
