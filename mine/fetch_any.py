"""Mine ANY team's episodes: both players' full action tapes, seed, banks.

Kaggle lets you list episodes for any submission id and download any replay, so the
top of the leaderboard is directly observable. Raw replays are ~30MB; reduce and
delete as we go.
"""
import gzip, json, os, subprocess, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAGGLE = os.path.join(ROOT, ".venv/bin/kaggle")
RAW = os.path.join(ROOT, "mine/raw2")
OUT = os.path.join(ROOT, "mine/top")


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
    for f in glob.glob(os.path.join(RAW, "*.json")):
        os.remove(f)
    subprocess.run([KAGGLE, "competitions", "replay", str(ep), "-p", RAW],
                   capture_output=True, text=True, timeout=1200)
    files = glob.glob(os.path.join(RAW, "*.json"))
    if not files:
        return "nofile"
    try:
        rec = reduce(files[0])
    finally:
        for f in files:
            os.remove(f)
    if rec is None:
        return "unparsed"
    with gzip.open(dest, "wt") as f:
        json.dump(rec, f)
    return "ok %s %s" % (rec["teams"], rec["rewards"])


if __name__ == "__main__":
    os.makedirs(RAW, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    limit = int(os.environ.get("LIMIT", "30"))
    for sub in sys.argv[1:]:
        eps = episode_ids(sub)
        print("submission", sub, "->", len(eps), "episodes", flush=True)
        for ep in eps[:limit]:
            print("  ", ep, fetch(ep), flush=True)
