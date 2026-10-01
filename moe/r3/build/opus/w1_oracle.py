"""W1 ceiling: record shepherd's stream (as recovered by yummers) on each of the 14 WLV seeds at the recorded seat,
build WL+S+own-seed-stream (oracle library), then shepherd vs it on the same 14 games -> w1_oracle.jsonl."""
import sys, json
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/w1_record.py").read().split('\nif __name__ == "__main__":')[0])
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/w1_test.py").read().split('\nif __name__ == "__main__":')[0])
from lib import read_src, decode, encode, write_src, pair_index
if __name__ == "__main__":
    S = json.load(open(ROOT + "/moe/r3/build/opus/w1_seeds.json"))
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=2) as ex:
        recs = list(ex.map(record, [("shep", "subW_shepherd.py", g["seed"], g["seat"]) for g in S["wlv"]]))
    json.dump(recs, open(ROOT + "/moe/r3/build/opus/w1_oracle_streams.json", "w"))
    src, blob, index = read_src(ROOT + "/moe/r3/build/opus/wl_S.py"); lib = decode(blob, index)
    for r in recs:
        lib[pair_index(r["pair"])].append({tuple(map(int, k.split(","))): min(255, int(q)) for k, q in r["ev"].items()})
    b2, i2 = encode(lib); write_src(src, b2, i2, ROOT + "/moe/r3/build/opus/wl_Sorc.py")
    jobs = [("shep", "subW_shepherd.py", "WL+S+oracle", "moe/r3/build/opus/wl_Sorc.py", g["seed"], g["seat"]) for g in S["wlv"]]
    out = ROOT + "/moe/r3/build/opus/w1_oracle.jsonl"; open(out, "w").close()
    pool(w1game, jobs, out)
