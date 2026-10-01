"""W1 telemetry rerun (fixed pick counter): WL+S / WL+R / WL+O vs shepherd on the 14 WLV seeds -> w1_tele.jsonl."""
import sys, json
exec(open("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/build/opus/w1_test.py").read().split('\nif __name__ == "__main__":')[0])
if __name__ == "__main__":
    S = json.load(open(ROOT + "/moe/r3/build/opus/w1_seeds.json"))
    jobs = [("shep", "subW_shepherd.py", on, "moe/r3/build/opus/wl_%s.py" % on[-1], g["seed"], g["seat"])
            for on in ("WL+S", "WL+R", "WL+O") for g in S["wlv"]]
    out = ROOT + "/moe/r3/build/opus/w1_tele.jsonl"; open(out, "w").close()
    pool(w1game, jobs, out)
