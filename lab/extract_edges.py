"""Parse the daily dumps ONCE and cache the tiny bits we need (teams, rewards, seed)."""
import zipfile, json, glob, os, sys
OUT="data/edges.jsonl"
done=set()
if os.path.exists(OUT):
    for l in open(OUT):
        try: done.add(json.loads(l)["ep"])
        except Exception: pass
n=0
with open(OUT,"a") as out:
    for zp in sorted(glob.glob("data/ep*/*.zip")):
        try: z=zipfile.ZipFile(zp)
        except Exception: continue
        for name in z.namelist():
            if not name.endswith(".json"): continue
            ep=name.split(".")[0]
            if ep in done: continue
            try:
                with z.open(name) as f: d=json.load(f)
            except Exception: continue
            t=d.get("info",{}).get("TeamNames"); r=d.get("rewards")
            if not t or not r or len(t)!=2: continue
            out.write(json.dumps(dict(ep=ep, teams=t, rewards=r,
                                      seed=d.get("info",{}).get("seed")))+"\n")
            done.add(ep); n+=1
            if n%100==0: print(f"  {n} cached", flush=True)
print(f"cached {n} new episodes -> {OUT} (total {len(done)})")
