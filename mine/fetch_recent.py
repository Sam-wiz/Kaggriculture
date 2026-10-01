"""Parallel-fetch every episode of the given submissions into mine/opp (reduced)."""
import gzip, json, os, subprocess, sys, glob, tempfile
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAGGLE = os.path.join(ROOT, ".venv/bin/kaggle")
OUT = os.path.join(ROOT, "mine/opp")


def episode_ids(sub):
    r = subprocess.run([KAGGLE, "competitions", "episodes", str(sub), "-v"],
                       capture_output=True, text=True, timeout=600)
    return [int(l.split(",")[0]) for l in r.stdout.splitlines()[1:]
            if l.split(",")[0].strip().isdigit()]


def reduce(path):
    with open(path) as f:
        d = json.load(f)
    info = d.get("info", {})
    teams = info.get("TeamNames") or []
    if len(teams) != 2:
        return None
    steps = d.get("steps", [])
    return {"episode_id": info.get("EpisodeId"), "seed": info.get("seed"),
            "teams": teams, "rewards": d.get("rewards"),
            "actions": [[s[0].get("action"), s[1].get("action")] for s in steps]}


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
    return "ok %s" % (rec["rewards"],)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    eps = []
    for sub in sys.argv[1:]:
        ids = episode_ids(sub)
        print("submission", sub, "->", len(ids), flush=True)
        eps += ids
    eps = [e for e in dict.fromkeys(eps)
           if not os.path.exists(os.path.join(OUT, "%d.json.gz" % e))]
    print("to fetch:", len(eps), flush=True)
    done = [0]
    def go(ep):
        r = fetch(ep)
        done[0] += 1
        if done[0] % 10 == 0:
            print("  %d/%d" % (done[0], len(eps)), flush=True)
        return r
    with ThreadPoolExecutor(max_workers=6) as ex:
        list(ex.map(go, eps))
    print("DONE", flush=True)
