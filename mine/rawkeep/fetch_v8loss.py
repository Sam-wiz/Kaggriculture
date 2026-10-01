"""Fetch v8's live loss/win replays with FULL per-step observations (both seats public tiles)
for state-diff analysis. Output: mine/rawkeep/v8live/<ep>.json.gz
usage: fetch_v8loss.py <ep,seed,opp,ours,theirs,seat> rows from /tmp/v8_losses.json (+wins file)
"""
import gzip, json, os, subprocess, sys, glob, tempfile
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KAGGLE = os.path.join(ROOT, ".venv/bin/kaggle")
OUT = os.path.join(ROOT, "mine/rawkeep/v8live")


def reduce(path):
    with open(path) as f:
        d = json.load(f)
    info = d.get("info", {})
    teams = info.get("TeamNames") or []
    steps = d.get("steps", [])
    if len(teams) != 2 or not steps:
        return None
    out_steps = []
    for s in steps:
        out_steps.append([{"observation": s[i].get("observation"), "action": s[i].get("action")}
                          for i in (0, 1)])
    return {"episode_id": info.get("EpisodeId"), "seed": info.get("seed"),
            "teams": teams, "rewards": d.get("rewards"), "steps": out_steps}


def fetch(ep):
    dest = os.path.join(OUT, "%d.json.gz" % ep)
    if os.path.exists(dest):
        return "cached"
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([KAGGLE, "competitions", "replay", str(ep), "-p", td],
                       capture_output=True, text=True, timeout=1800)
        files = glob.glob(os.path.join(td, "*.json"))
        if not files:
            return "nofile"
        rec = reduce(files[0])
    if rec is None:
        return "unparsed"
    with gzip.open(dest, "wt") as f:
        json.dump(rec, f)
    return "ok"


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    eps = [int(a) for a in sys.argv[1:]]
    with ThreadPoolExecutor(max_workers=4) as ex:
        for ep, r in zip(eps, ex.map(fetch, eps)):
            print(ep, r, flush=True)
