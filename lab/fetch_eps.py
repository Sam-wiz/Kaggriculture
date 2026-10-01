import subprocess, json, os
KA=".venv/bin/kaggle"
need=json.load(open('live_eps/need.json'))
os.makedirs('live_eps/replays', exist_ok=True)
done=0
for i,ep in enumerate(need):
    out=f'live_eps/replays/episode-{ep}-replay.json'
    if os.path.exists(out): done+=1; continue
    subprocess.run([KA,"competitions","replay",str(ep),"-p","live_eps/replays"],capture_output=True,text=True)
    if os.path.exists(out): done+=1
    if i%25==0: print(f"{i}/{len(need)} got={done}",flush=True)
print("done", done)
