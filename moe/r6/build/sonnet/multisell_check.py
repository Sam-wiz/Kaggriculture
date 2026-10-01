"""Precondition check for porting BRX2 onto C1/C1R2: how often does the live
chassis batch >=2 distinct-item SELL orders in the same market list?  BRX2
(moe/opus/cand_brx2.py) only ever fires on such turns (_BRX_STATS['multi']).
If C1/C1R2 rarely does this, BRX2's mechanism has near-zero surface area here
regardless of how well it gated on the old sir/f55rec pool.

Foreground, single process, nice 10. <=6 seeds/agent to stay cheap.
"""
import sys
sys.path.insert(0, "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture")
import harness

AGENTS = {
    "C1": "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/subY_C1_predict2.py",
    "C1R2": "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/subZ_C1R2.py",
}

SEEDS = [9700001, 9700002, 9700003]


def count_multisell(agent_path, seed, opp_path):
    stats = {"turns": 0, "multi_turns": 0, "max_items": 0, "any_market_turns": 0}

    def on_step(step, state, env):
        for i in (0, 1):
            act = state[i].action
            if not isinstance(act, dict):
                continue
            mkt = act.get("market") or []
            items = set()
            for o in mkt:
                if isinstance(o, (list, tuple)) and len(o) >= 2 and str(o[0]).upper() == "SELL":
                    items.add(str(o[1]).upper())
            if i == 0:
                stats["turns"] += 1
                if mkt:
                    stats["any_market_turns"] += 1
                if len(items) >= 2:
                    stats["multi_turns"] += 1
                stats["max_items"] = max(stats["max_items"], len(items))

    r = harness.run_episode(agent_path, opp_path, seed=seed, on_step=on_step, copy_obs=True)
    return stats, r["reward"], r["status"]


if __name__ == "__main__":
    for name, path in AGENTS.items():
        print(f"=== {name} vs itself ===")
        for seed in SEEDS:
            stats, reward, status = count_multisell(path, seed, path)
            frac = stats["multi_turns"] / max(1, stats["turns"])
            print(f"seed={seed} turns={stats['turns']} any_mkt={stats['any_market_turns']} "
                  f"multi_sell_turns={stats['multi_turns']} ({frac:.1%}) max_items={stats['max_items']} "
                  f"reward={reward} status={status}")
