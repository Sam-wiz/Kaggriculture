"""A/B the two live arms on what matters: bank-0 rate and win rate."""
import json, glob, subprocess, sys, os, statistics

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
K = os.path.join(ROOT, ".venv/bin/kaggle")


def episodes(sub, n):
    out = subprocess.run([K, "competitions", "episodes", str(sub), "-v"],
                         capture_output=True, text=True, timeout=600).stdout
    ids = [l.split(",")[0].strip() for l in out.splitlines()[1:]
           if l.split(",")[0].strip().isdigit()]
    return ids[:n]


def result(ep):
    raw = os.path.join(ROOT, "mine/raw")
    subprocess.run(["rm", "-rf", raw])
    os.makedirs(raw, exist_ok=True)
    subprocess.run([K, "competitions", "replay", str(ep), "-p", raw],
                   capture_output=True, text=True, timeout=1200)
    f = glob.glob(os.path.join(raw, "*.json"))
    if not f:
        return None
    d = json.load(open(f[0]))
    t = d["info"]["TeamNames"]
    me = 0 if t[0] == "Sam-wiz" else 1
    return d["rewards"][me], d["rewards"][1 - me], t[1 - me]


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    for sub, name in (("56007048", "control (no guard)"), ("56007047", "guard")):
        rows = []
        for ep in episodes(sub, n):
            r = result(ep)
            if r:
                rows.append(r)
        if not rows:
            continue
        z = sum(1 for a, b, _ in rows if a == 0)
        w = sum(1 for a, b, _ in rows if a > b)
        l = sum(1 for a, b, _ in rows if a < b)
        print(f"{name:<22} n={len(rows):<3} W{w} L{l}   bank-0: {z} ({100*z/len(rows):.0f}%)"
              f"   mean bank {statistics.mean(a for a, _, _ in rows):>9,.0f}"
              f"   vs {statistics.mean(b for _, b, _ in rows):>9,.0f}")
