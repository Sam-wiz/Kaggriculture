"""Harvest Kaggriculture agent files from recently pushed GitHub repos (list in /tmp/gh_new.txt).
Selects .py files 5 KB-3 MB whose path looks like an agent/submission, downloads raw, keeps those that
define an agent callable and reference the game (farms/market/unlocked_shops), dedupes by md5 against
every agent we already hold, writes rivalsGH/<owner>_<repo>/<path-with-underscores>.py + index json."""
import base64, glob, hashlib, json, os, re, subprocess
OUT = "rivalsGH"; os.makedirs(OUT, exist_ok=True)
SKIPREPO = ("casmi26", "mamba-trainer", "TRANCEatables", "DecisionCraft", "Shadowell/Shadowell",
            "yasumorishima/yasumorishima", "jaygautam-creator/jaygautam", "kimgy5756581/git-practice")
known = {hashlib.md5(open(f, "rb").read()).hexdigest() for f in glob.glob("rivals*/*/_entry.py") + glob.glob("sub*.py")}
repos = [l.split()[3] for l in open("/tmp/gh_new.txt") if len(l.split()) >= 4]
def gh(path): 
    r = subprocess.run(["gh", "api", "-X", "GET", path], capture_output=True, text=True, timeout=300)
    return json.loads(r.stdout) if r.returncode == 0 and r.stdout.strip() else None
found = []
for repo in repos:
    if any(s in repo for s in SKIPREPO): continue
    meta = gh(f"repos/{repo}")
    if not meta: continue
    tree = gh(f"repos/{repo}/git/trees/{meta['default_branch']}?recursive=1") or {}
    cands = [t for t in tree.get("tree", []) if t["type"] == "blob" and t["path"].endswith(".py")
             and 5_000 <= (t.get("size") or 0) <= 3_000_000
             and re.search(r"(main|submission|agent|sub_|entry|bot|policy)", t["path"], re.I)]
    kept = 0
    for t in sorted(cands, key=lambda t: -t["size"])[:25]:
        blob = gh(f"repos/{repo}/git/blobs/{t['sha']}")
        if not blob: continue
        src = base64.b64decode(blob["content"]).decode("utf-8", "replace")
        if not (re.search(r"^def (agent|kaggle_submission_agent|my_agent)\s*\(", src, re.M) and
                ("unlocked_shops" in src or "'farms'" in src or '"farms"' in src)): continue
        h = hashlib.md5(src.encode()).hexdigest()
        if h in known: continue
        known.add(h); kept += 1
        d = os.path.join(OUT, repo.replace("/", "_")); os.makedirs(d, exist_ok=True)
        p = os.path.join(d, re.sub(r"[/ ]", "_", t["path"]))
        open(p, "w").write(src)
        found.append((f"{repo.split('/')[0][:14]}/{os.path.basename(t['path'])[:24]}", p, t["size"]))
    print(f"{repo:<48} candidates {len(cands):>3}  new agents {kept}", flush=True)
json.dump([(n, p) for n, p, _ in found], open("moe/r6/screen_candsGH.json", "w"), indent=0)
print(len(found), "new agent files ->", OUT)
