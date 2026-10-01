"""Autopsy lane: fetch m30b/v8hh episodes -> reduced replays into replays/.
Keeps teams, rewards, seed, per-turn actions, and per-player statuses.
Usage: .venv/bin/python fetch.py <subid> <n_latest>
"""
import gzip, json, os, subprocess, sys, glob, tempfile
from concurrent.futures import ThreadPoolExecutor

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
KAGGLE = os.path.join(ROOT, ".venv/bin/kaggle")
OUT = os.path.join(ROOT, "moe/r9/build/autopsy/replays")
SUMMARY = os.path.join(ROOT, "moe/r9/build/autopsy/episodes.jsonl")


def episode_ids(sub, n=None):
    r = subprocess.run([KAGGLE, "competitions", "episodes", str(sub), "-v"],
                       capture_output=True, text=True, timeout=600)
    rows = []
    for l in r.stdout.splitlines()[1:]:
        p = l.split(",")
        if p[0].strip().isdigit() and "COMPLETED" in l:
            rows.append(int(p[0]))
    return rows[:n] if n else rows


def fetch_one(ep):
    dest = os.path.join(OUT, "%d.json.gz" % ep)
    if os.path.exists(dest):
        with gzip.open(dest) as f:
            return json.load(f)
    tmp = tempfile.mkdtemp(dir="/tmp")
    try:
        subprocess.run([KAGGLE, "competitions", "replay", str(ep), "-p", tmp],
                       capture_output=True, text=True, timeout=900)
        files = glob.glob(os.path.join(tmp, "*.json"))
        if not files:
            return {"ep": ep, "err": "nofile"}
        with open(files[0]) as f:
            d = json.load(f)
        info = d.get("info", {})
        steps = d.get("steps", [])
        statuses = set()
        for s in steps:
            for a in s:
                if a.get("status"):
                    statuses.add(a["status"])
        rec = {"ep": info.get("EpisodeId") or ep, "seed": info.get("seed"),
               "teams": info.get("TeamNames") or [],
               "rewards": d.get("rewards"), "nsteps": len(steps),
               "statuses": sorted(statuses),
               "actions": [[s[0].get("action"), s[1].get("action")] for s in steps]}
        with gzip.open(dest, "wt") as f:
            json.dump(rec, f)
        return rec
    except Exception as e:
        return {"ep": ep, "err": str(e)[:120]}
    finally:
        for f in glob.glob(os.path.join(tmp, "*")):
            os.remove(f)
        os.rmdir(tmp)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    sub = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 25
    ids = episode_ids(sub, n)
    print(f"{sub}: fetching {len(ids)} episodes", flush=True)
    with ThreadPoolExecutor(max_workers=5) as ex, open(SUMMARY, "a") as sf:
        for rec in ex.map(fetch_one, ids):
            slim = {k: v for k, v in rec.items() if k != "actions"}
            sf.write(json.dumps(slim) + "\n")
            print(slim.get("ep"), slim.get("teams"), slim.get("rewards"),
                  slim.get("statuses"), slim.get("err", ""), flush=True)
