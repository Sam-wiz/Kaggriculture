"""Fetch OUR submissions' episodes: opponent identity + result, per episode.
Replays are ~30MB — reduce and delete. Parallel over episode ids.
Usage: fetch_ours.py <subid> <n_latest> <out.jsonl>
"""
import gzip, json, os, subprocess, sys, glob, tempfile
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAGGLE = os.path.join(ROOT, ".venv/bin/kaggle")


def episode_ids(sub, n):
    r = subprocess.run([KAGGLE, "competitions", "episodes", str(sub), "-v"],
                       capture_output=True, text=True, timeout=600)
    ids = [int(l.split(",")[0]) for l in r.stdout.splitlines()[1:]
           if l.split(",")[0].strip().isdigit()]
    return ids[:n]


def fetch_one(ep):
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
        teams = info.get("TeamNames") or []
        rewards = d.get("rewards")
        steps = d.get("steps", [])
        # which seat is ours? match team name absent -> use rewards side w/ ours unknown;
        # caller resolves by team name list (our team name is in teams)
        return {"ep": ep, "seed": info.get("seed"), "teams": teams,
                "rewards": rewards, "nsteps": len(steps)}
    except Exception as e:
        return {"ep": ep, "err": str(e)[:120]}
    finally:
        for f in glob.glob(os.path.join(tmp, "*")):
            os.remove(f)
        os.rmdir(tmp)


if __name__ == "__main__":
    sub, n, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    ids = episode_ids(sub, n)
    print(f"{sub}: {len(ids)} episode ids", flush=True)
    with ThreadPoolExecutor(max_workers=6) as ex, open(out, "a") as f:
        for rec in ex.map(fetch_one, ids):
            f.write(json.dumps(rec) + "\n")
            print(rec["ep"], rec.get("teams"), rec.get("rewards"), flush=True)
