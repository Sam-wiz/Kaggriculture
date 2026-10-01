"""Count units actually harvested, by product, and tiles that ended as weeds."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

def run(path, opp="pass", seed=1):
    got = collections.Counter()
    prev = {}
    planted = collections.Counter()
    weeded = collections.Counter()
    seen = {}
    def on_step(step, state, env):
        obs0 = state[0].observation
        priv = state[0].observation.private
        cur = collections.Counter()
        for iv in priv["inventories"]:
            for k, v in iv.items(): cur[k] += v
        for k, v in priv["shed"].items(): cur[k] += v
        for k, v in cur.items():
            d = v - prev.get(k, 0)
            if d > 0: got[k] += d
        prev.clear(); prev.update(cur)
        # track tile lifecycle
        for y, row in enumerate(obs0.farms[0]["tiles"]):
            for x, t in enumerate(row):
                key = (x, y)
                was = seen.get(key)
                now = None
                if isinstance(t, dict):
                    now = t.get("crop") if t.get("kind") == "PLANT" else t.get("kind")
                if now != was:
                    if now and now not in ("WEED",) and was != now and isinstance(t, dict) and t.get("kind") == "PLANT":
                        planted[now] += 1
                    if now == "WEED" and was and was not in ("WEED",):
                        weeded[was] += 1
                    seen[key] = now
    r = harness.run_episode(path, opp, seed=seed, on_step=on_step, catch_errors=False)
    print(f"{path} seed={seed} bank={r['reward'][0]:.0f}")
    print("planted:", dict(planted))
    print("died as weed:", dict(weeded))
    print("harvested units:", {k: v for k, v in got.most_common()})
    for c in ("STRAWBERRY","TOMATO","MELON","CARROT","WHEAT"):
        if planted[c]:
            print(f"   {c}: {got[c]/planted[c]:.2f} units/tile  ({planted[c]} planted, {weeded[c]} died)")

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else "pass",
        int(sys.argv[3]) if len(sys.argv)>3 else 1)
