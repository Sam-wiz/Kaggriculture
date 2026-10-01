"""A benchmark made of REAL ladder opponents, not of ourselves.

Every tuning decision so far was scored in the mirror -- candidate vs our own build. That optimises
"better than our previous self", which is not the same as "better against the field", and it has
already misled us once: the slot exploit read +3,474 in the mirror while the entire field already
sold from slot 0, so most of that gain did not exist.

This replays mined opponent tapes as opponents. Their farms rebuild coherently from their own
actions (that is why our own tape ports at all); reactive players degrade, so treat the pool as a
diverse sparring set rather than a faithful reproduction of any one player.
"""
import os, sys, gzip, glob, json, collections, statistics
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "mine"))


def load_pool(max_per_team=1, limit=24):
    """One tape per opponent team, preferring their strongest recorded game."""
    best = {}
    for f in glob.glob(os.path.join(ROOT, "mine/opp/*.json.gz")):
        with gzip.open(f, "rt") as fh:
            d = json.load(fh)
        t = d["teams"]
        me = 0 if t[0] == "Sam-wiz" else 1
        opp = t[1 - me]
        bank = d["rewards"][1 - me]
        if opp not in best or bank > best[opp][0]:
            best[opp] = (bank, [a[1 - me] for a in d["actions"]])
    rows = sorted(best.items(), key=lambda kv: -kv[1][0])[:limit]
    return [(name, acts) for name, (bank, acts) in rows]


def agent_for(acts):
    import tape_agent
    ta = tape_agent.make_agent(acts)
    return lambda obs, cfg=None: ta(obs)


if __name__ == "__main__":
    pool = load_pool()
    print(f"pool: {len(pool)} opponent tapes")
    for n, a in pool[:8]:
        print(f"   {n}")
