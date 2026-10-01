import gzip, json, os, subprocess, sys, glob
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
KAGGLE = ROOT + "/.venv/bin/kaggle"
RAW = "/tmp/m30b_raw"; OUT = ROOT + "/mine/loss"
os.makedirs(RAW, exist_ok=True); os.makedirs(OUT, exist_ok=True)
def reduce(path):
    d = json.load(open(path))
    info = d.get("info", {})
    teams = info.get("TeamNames") or []
    if len(teams) != 2: return None
    steps = d.get("steps", [])
    return {"episode_id": info.get("EpisodeId"), "seed": info.get("seed"),
            "teams": teams, "rewards": d.get("rewards"),
            "actions": [[s[0].get("action"), s[1].get("action")] for s in steps]}
for ep in sys.argv[1:]:
    dest = f"{OUT}/{ep}.json.gz"
    if os.path.exists(dest): continue
    for f in glob.glob(RAW + "/*.json"): os.remove(f)
    subprocess.run([KAGGLE, "competitions", "replay", str(ep), "-p", RAW], capture_output=True, timeout=1200)
    files = glob.glob(RAW + "/*.json")
    if not files: print(ep, "nofile", flush=True); continue
    rec = reduce(files[0])
    for f in files: os.remove(f)
    if rec is None: print(ep, "unparsed"); continue
    with gzip.open(dest, "wt") as f: json.dump(rec, f)
    print(ep, "ok", rec["teams"], rec["rewards"], flush=True)
