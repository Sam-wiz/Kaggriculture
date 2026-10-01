"""Fetch every lost episode in full and extract a per-turn trace of both farms.

Our earlier fetcher reduced replays to action tapes and threw the observations away, so the only way
to get a bank curve was to re-simulate -- and re-simulation does not reproduce the episode (the tape
replay drifts). But the raw replay already contains the full observation at every step, for both
seats: money, tiles, shed, the shared market and the town. Reading it directly is exact.

Per episode we keep 720 rows of (money, tiles, shed size, hands) for both players plus the shared
market and the shop unlock list -- a few hundred KB instead of 32 MB.
"""
import glob
import gzip
import json
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.abspath(__file__))
KAGGLE = os.path.join(ROOT, ".venv/bin/kaggle")
OUT = os.path.join(ROOT, "mine/loss")
US = "Sam-wiz"
TRACKED = ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON", "EGG", "MILK", "WOOL", "FERTILIZER")


def _shed(priv):
    s = (priv or {}).get("shed") or {}
    return {k: int(v) for k, v in s.items() if v}


def extract(path):
    with open(path) as f:
        d = json.load(f)
    info = d.get("info", {})
    teams = info.get("TeamNames") or []
    if len(teams) != 2 or US not in teams:
        return None
    me = teams.index(US)
    steps = d["steps"]
    rows = []
    for t, pair in enumerate(steps):
        o0 = pair[0].get("observation") or {}
        o1 = pair[1].get("observation") or {}
        farms = o0.get("farms")
        if not farms:
            continue
        priv = [(o0.get("private") or {}), (o1.get("private") or {})]
        rows.append(dict(
            t=t,
            money=[farms[0].get("money"), farms[1].get("money")],
            hands=[len(farms[0].get("hands") or []), len(farms[1].get("hands") or [])],
            tiles=[len(farms[0].get("tiles") or []), len(farms[1].get("tiles") or [])],
            shed=[_shed(priv[0]), _shed(priv[1])],
            px={k: (o0.get("market", {}).get("prices") or {}).get(k) for k in TRACKED},
            inv={k: (o0.get("market", {}).get("inventory") or {}).get(k) for k in TRACKED},
            shops=sorted((o0.get("town", {}) or {}).get("unlocked_shops") or []),
        ))
    return dict(episode_id=info.get("EpisodeId") or d.get("id"), seed=info.get("seed"),
                teams=teams, rewards=d.get("rewards"), our_seat=me,
                actions=[[p[0].get("action"), p[1].get("action")] for p in steps],
                trace=rows)


def fetch(ep):
    dest = os.path.join(OUT, "%d.json.gz" % ep)
    if os.path.exists(dest):
        return "cached"
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([KAGGLE, "competitions", "replay", str(ep), "-p", td],
                       capture_output=True, text=True, timeout=1800)
        fs = glob.glob(os.path.join(td, "*.json"))
        if not fs:
            return "nofile"
        rec = extract(fs[0])
    if rec is None:
        return "unparsed"
    with gzip.open(dest, "wt") as f:
        json.dump(rec, f)
    return "ok"


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    eps = [int(x) for x in sys.argv[1:]]
    todo = [e for e in eps if not os.path.exists(os.path.join(OUT, "%d.json.gz" % e))]
    print(f"{len(eps)} episodes, {len(todo)} to fetch", flush=True)
    done = [0]

    def go(e):
        r = fetch(e)
        done[0] += 1
        if done[0] % 5 == 0:
            print(f"  {done[0]}/{len(todo)}", flush=True)
        return r

    with ThreadPoolExecutor(max_workers=5) as ex:
        list(ex.map(go, todo))
    print("DONE", flush=True)
