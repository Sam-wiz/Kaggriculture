"""Download our ladder episodes, reduce each replay to the opponent's action tape, delete the raw.

A Kaggriculture replay stores the full 719-turn action list for BOTH players plus the seed, team
names and final banks. Raw replays are ~30 MB; the actions are a tiny fraction of that, so we reduce
and delete as we go.
"""
import gzip, json, os, subprocess, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAGGLE = os.path.join(ROOT, ".venv/bin/kaggle")
RAW = os.path.join(ROOT, "mine/raw")
OUT = os.path.join(ROOT, "mine/tapes")
US = "Sam-wiz"


def episode_ids(submission_id):
    r = subprocess.run([KAGGLE, "competitions", "episodes", str(submission_id), "-v"],
                       capture_output=True, text=True, timeout=300)
    ids = []
    for line in r.stdout.splitlines()[1:]:
        parts = line.split(",")
        if parts and parts[0].strip().isdigit():
            ids.append(int(parts[0]))
    return ids


def reduce_replay(path):
    with open(path) as f:
        d = json.load(f)
    info = d.get("info", {})
    teams = info.get("TeamNames") or [a.get("Name") for a in info.get("Agents", [])]
    if not teams or len(teams) != 2:
        return None
    our = 0 if teams[0] == US else 1
    opp = 1 - our
    steps = d.get("steps", [])
    return {
        "episode_id": d.get("id") or info.get("EpisodeId"),
        "seed": info.get("seed"),
        "teams": teams,
        "rewards": d.get("rewards"),
        "our_seat": our,
        "opponent": teams[opp],
        "our_bank": (d.get("rewards") or [None, None])[our],
        "opp_bank": (d.get("rewards") or [None, None])[opp],
        "opp_actions": [s[opp].get("action") for s in steps if len(s) > opp],
    }


def fetch(ep):
    dest = os.path.join(OUT, "%d.json.gz" % ep)
    if os.path.exists(dest):
        return "cached"
    for f in glob.glob(os.path.join(RAW, "*.json")):
        os.remove(f)
    r = subprocess.run([KAGGLE, "competitions", "replay", str(ep), "-p", RAW],
                       capture_output=True, text=True, timeout=900)
    files = glob.glob(os.path.join(RAW, "*.json"))
    if not files:
        return "nofile: " + (r.stderr or r.stdout)[:120]
    try:
        rec = reduce_replay(files[0])
    finally:
        for f in files:
            os.remove(f)
    if rec is None:
        return "unparsed"
    with gzip.open(dest, "wt") as f:
        json.dump(rec, f)
    return "ok %s %s vs %s" % (rec["seed"], rec["our_bank"], rec["opp_bank"])


if __name__ == "__main__":
    subs = sys.argv[1:] or ["55969521"]
    limit = int(os.environ.get("LIMIT", "40"))
    seen = set()
    for sub in subs:
        eps = episode_ids(sub)
        print("submission", sub, "episodes", len(eps), flush=True)
        n = 0
        for ep in eps:
            if ep in seen:
                continue
            seen.add(ep)
            if n >= limit:
                break
            msg = fetch(ep)
            n += 1
            print("  %d %s" % (ep, msg), flush=True)
            if "nofile" in msg and "Authentication" in msg:
                print("AUTH EXPIRED - stopping", flush=True)
                sys.exit(1)
