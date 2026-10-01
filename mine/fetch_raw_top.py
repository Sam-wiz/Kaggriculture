"""Fetch RAW replays for top teams' mined episode IDs + our live-loss opponents."""
import gzip, json, os, subprocess, sys, glob, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAGGLE = os.path.join(ROOT, ".venv/bin/kaggle")
RAW = os.path.join(ROOT, "mine/rawkeep"); os.makedirs(RAW, exist_ok=True)
tf = json.load(open(os.path.join(ROOT, "mine/top/team_files.json")))
want = {}
for team, n in [("mtmr_s1",40),("Unknown Mother-Goose",40),("Vadim Vasilenko",40),
                ("Majkel1337",40),("THIRD FARM CLUB",40),("SpaTaro",40),
                ("Otter Vibe",40),("KawattaTaido",30),("ymg_aq",30)]:
    for f in tf.get(team, [])[:n]:
        ep = int(re.search(r"(\d+)\.json\.gz", f).group(1)); want[ep]=team
# our live-loss replays (keiz family, 豆包, etc.)
for f in glob.glob(os.path.join(ROOT,"mine/loss/*.json.gz")):
    ep = int(re.search(r"(\d+)\.json\.gz", f).group(1))
    want.setdefault(ep, "lossopp")
todo = [(ep,team) for ep,team in want.items() if not os.path.exists(os.path.join(RAW,f"{ep}.json.gz"))]
print("to fetch:", len(todo), flush=True)
done=fail=0
for i,(ep,team) in enumerate(todo):
    dest = os.path.join(RAW, f"{ep}.json.gz")
    for f in glob.glob(os.path.join(RAW,"episode-*")): os.remove(f)
    subprocess.run([KAGGLE,"competitions","replay",str(ep),"-p",RAW],capture_output=True,text=True,timeout=1200)
    files=[f for f in glob.glob(os.path.join(RAW,"*.json")) if "episode-" in f]
    if not files:
        fail+=1; print(ep,team,"nofile",flush=True); continue
    open(dest,"wb").write(gzip.compress(open(files[0],"rb").read()))
    os.remove(files[0]); done+=1
    if done%10==0: print(f"{done}/{len(todo)}",flush=True)
print("done:",done,"fail:",fail)
