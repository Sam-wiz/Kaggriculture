"""Fetch RAW replay JSONs (keep observations) for episodes in mine/top belonging to target teams."""
import gzip, json, os, subprocess, sys, glob, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAGGLE = os.path.join(ROOT, ".venv/bin/kaggle")
RAW = os.path.join(ROOT, "mine/rawkeep")
os.makedirs(RAW, exist_ok=True)

team_files = json.load(open(os.path.join(ROOT, "mine/top/team_files.json")))
targets = sys.argv[1:] or ["DSM"]
n_per = int(os.environ.get("N_PER", "60"))

todo = []
for team in targets:
    for f in team_files.get(team, [])[:n_per]:
        ep = int(re.search(r"(\d+)\.json\.gz", f).group(1))
        if not os.path.exists(os.path.join(RAW, f"{ep}.json.gz")):
            todo.append((team, ep))
print("to fetch:", len(todo))
done = fail = 0
for i,(team,ep) in enumerate(todo):
    dest = os.path.join(RAW, f"{ep}.json.gz")
    for f in glob.glob(os.path.join(RAW, "episode-*")):
        os.remove(f)
    r = subprocess.run([KAGGLE, "competitions", "replay", str(ep), "-p", RAW],
                       capture_output=True, text=True, timeout=1200)
    files = [f for f in glob.glob(os.path.join(RAW, "*.json")) if "episode-" in f]
    if not files:
        fail += 1
        print(ep, "nofile", r.stderr[:100])
        continue
    os.rename(files[0], dest) if files[0].endswith(".gz") else None
    if not files[0].endswith(".gz"):
        raw = open(files[0],"rb").read()
        open(dest,"wb").write(gzip.compress(raw))
        os.remove(files[0])
    done += 1
    if i % 10 == 0: print(f"{i}/{len(todo)} done")
print("done:", done, "fail:", fail)
