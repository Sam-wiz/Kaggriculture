"""Stream Kaggle's official daily top-episode dumps (kaggle/kaggriculture-episodes-YYYY-MM-DD) into the
compact format, one file at a time (raw ~37 MB each; disk is tight). Output: mine/top10/<ep>.json.gz with
episode_id, date, seed, teams, rewards, agents (submission ids if present), shops (t=150 and final), actions.
usage: fetch_epindex.py DATE [DATE ...]   env WORKERS (default 4), LIMIT (per date, default all)
"""
import gzip, json, os, re, subprocess, sys, tempfile, shutil
from concurrent.futures import ThreadPoolExecutor
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAGGLE = os.path.join(ROOT, ".venv/bin/kaggle")
OUT = os.path.join(ROOT, "mine/top10")


def list_files(slug):
    names, tok = [], None
    while True:
        cmd = [KAGGLE, "datasets", "files", slug, "--page-size", "200", "--csv"]
        if tok: cmd += ["--page-token", tok]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        tok = None
        for line in r.stdout.splitlines():
            m = re.match(r"Next Page Token = (\S+)", line)
            if m: tok = m.group(1); continue
            f = line.split(",")[0].strip()
            if f.endswith(".json"): names.append(f)
        if not tok: return names


def reduce(path, date):
    d = json.load(open(path))
    info = d.get("info", {}); steps = d.get("steps", [])
    teams = info.get("TeamNames") or []
    if len(teams) != 2 or not steps: return None
    def shops(t):
        try: return steps[t][0]["observation"]["town"]["unlocked_shops"]
        except Exception: return None
    return {"episode_id": info.get("EpisodeId"), "date": date, "seed": info.get("seed"), "teams": teams,
            "rewards": d.get("rewards"), "agents": info.get("Agents") or info.get("SubmissionIds"),
            "shops150": shops(min(150, len(steps) - 1)), "shops": shops(len(steps) - 1),
            "actions": [[s[0].get("action"), s[1].get("action")] for s in steps]}


def fetch(arg):
    slug, date, name = arg
    dest = os.path.join(OUT, name.replace(".json", ".json.gz"))
    if os.path.exists(dest): return "cached"
    tmp = tempfile.mkdtemp(dir=os.path.join(ROOT, "mine"))
    try:
        subprocess.run([KAGGLE, "datasets", "download", slug, "-f", name, "-p", tmp, "--force"],
                       capture_output=True, text=True, timeout=1800)
        for z in [f for f in os.listdir(tmp) if f.endswith(".zip")]:
            subprocess.run(["unzip", "-o", "-q", os.path.join(tmp, z), "-d", tmp]); os.remove(os.path.join(tmp, z))
        js = [f for f in os.listdir(tmp) if f.endswith(".json")]
        if not js: return "nofile"
        rec = reduce(os.path.join(tmp, js[0]), date)
        if rec is None: return "unparsed"
        with gzip.open(dest, "wt") as f: json.dump(rec, f)
        return "ok"
    except Exception as e:
        return "err " + repr(e)[:60]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    W = int(os.environ.get("WORKERS", "4")); LIM = int(os.environ.get("LIMIT", "0"))
    for date in sys.argv[1:]:
        slug = f"kaggle/kaggriculture-episodes-{date}"
        names = list_files(slug)
        if LIM: names = names[:LIM]
        print(f"{date}: {len(names)} episodes", flush=True)
        with ThreadPoolExecutor(max_workers=W) as ex:
            for i, r in enumerate(ex.map(fetch, [(slug, date, n) for n in names]), 1):
                if i % 25 == 0 or not r.startswith(("ok", "cached")): print(f"  {date} {i}/{len(names)} {r}", flush=True)
        print(f"{date}: done", flush=True)
