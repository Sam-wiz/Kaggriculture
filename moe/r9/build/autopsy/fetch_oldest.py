import json, sys
sys.path.insert(0, ".")
from fetch import fetch_one
from concurrent.futures import ThreadPoolExecutor

ids = [int(x) for x in open("oldest.txt").read().split()]
with ThreadPoolExecutor(max_workers=5) as ex, open("episodes.jsonl", "a") as sf:
    for rec in ex.map(fetch_one, ids):
        slim = {k: v for k, v in rec.items() if k != "actions"}
        sf.write(json.dumps(slim) + "\n")
        print(slim.get("ep"), slim.get("teams"), slim.get("rewards"), slim.get("statuses"), flush=True)
