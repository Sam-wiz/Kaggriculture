"""Bit-exactness + speed check of a kagsim build: replay recorded top-dump games (both tapes) and compare banks.
usage: python kagsim_check.py SO_DIR GAMES_DIR N"""
import sys, os, glob, gzip, json, time
sys.path.insert(0, sys.argv[1]); import kagsim
paths = sorted(glob.glob(os.path.join(sys.argv[2], "*.json.gz")))[:int(sys.argv[3])]
ok = 0; t0 = time.time(); games = []
for p in paths:
    d = json.load(gzip.open(p, "rt")); acts = d["actions"]
    P = {"farmer": ["PASS"], "hands": [], "market": []}
    sa = kagsim.Stream([acts[t + 1][0] if t + 1 < len(acts) and isinstance(acts[t + 1][0], dict) else P for t in range(720)])
    sb = kagsim.Stream([acts[t + 1][1] if t + 1 < len(acts) and isinstance(acts[t + 1][1], dict) else P for t in range(720)])
    games.append((sa, sb, d["seed"], d["rewards"]))
t1 = time.time()
for sa, sb, seed, rew in games:
    r = kagsim.run_episode(sa, sb, seed)
    ok += all(abs(a - b) < 0.5 for a, b in zip(r, rew))
t2 = time.time()
print(f"kagsim {getattr(kagsim, 'ENGINE_VERSION', '?')} exact {ok}/{len(games)}  {1000*(t2-t1)/len(games):.2f} ms/episode (load {t1-t0:.1f}s)")
