"""Read-only source/corpus audit. Writes only to this script's directory."""
from __future__ import annotations

import ast
import hashlib
import json
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent


def fingerprint(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data),
            "logical_lines": len(data.splitlines()), "sha256": hashlib.sha256(data).hexdigest()}


def censor_probe():
    """Run the actual update function with synthetic inputs, without loading the agent.

    This establishes a scoring mechanism, not its frequency or game-level value.
    Event 150 is hidden at the floor. Candidate 0 predicts it; candidate 1 does not.
    The two floor worlds have identical public inventory observations. In the
    no-milk-sale world, eight hidden wool sales can produce the same public bank
    change; the ambiguity is not resolved just by observing total cash.
    """
    source = ROOT / "subZ_C1R2.py"
    tree = ast.parse(source.read_text())
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "_v92_q_update")
    isolated = ast.Module(body=[node], type_ignores=[])
    results = []
    for label, price, delta, latent, other_latent in [
        ("floor_hidden_milk_sale", 1, 0, 8, 0),
        ("floor_no_milk_sale_same_proceeds_from_wool", 1, 0, 0, 8),
        ("observable_milk_sale_control", 160, 8, 8, 0),
    ]:
        items = ("MILK", "WOOL", "STRAWBERRY")
        scope = {"_V92_Q_ITEMS": items, "_V92_Q_PF": 1.0, "_V92_Q_PM": 0.5,
                 "_V9_RACE": {}, "_v9_town_draw": lambda shops, step: {}}
        exec(compile(isolated, str(source), "exec"), scope)
        st = {"step": -1, "obs": {}, "evs": [{(150, 0): 8}, {}],
              "index": {(150, 0): [0]}, "m": [0, 0], "f": [0, 0],
              "near": [0, 0], "score": [0.0, 0.0], "best": 0, "done": 150}
        inventory = {"MILK": 10076, "WOOL": 10059, "STRAWBERRY": 10062} if price == 1 else dict.fromkeys(items, 10000)
        for step in (151, 152):
            before = dict(inventory)
            if step == 151:
                inventory["MILK"] += delta
            prices = dict.fromkeys(items, 1) if price == 1 else {"MILK": 160 if step == 151 else 143, "WOOL": 200, "STRAWBERRY": 120}
            scope["_V9_RACE"][0] = {"prev": {"step": step - 1, "prices": prices,
                                                       "inventory": before, "shops": [], "own": {}}}
            scope["_v92_q_update"]({"player": 0, "step": step, "market": {"inventory": dict(inventory)}}, st)
        results.append({"case": label, "latent_opponent_milk_sale_at_150": latent,
                        "latent_opponent_wool_sale_at_150": other_latent,
                        "public_cash_change_from_floor_sales": latent + other_latent if price == 1 else None,
                        "observed_inventory_delta": delta, "prev_price": price,
                        "scores": st["score"], "best": st["best"], "false_positive_counts": st["f"],
                        "observed_sale_count": len(st["obs"])})
    assert results[0]["scores"] == results[1]["scores"] == [-1.0, 0.0]
    assert results[0]["best"] == results[1]["best"] == 1
    assert results[2]["scores"] == [1.5, 0.0] and results[2]["best"] == 0
    return {"source": fingerprint(source), "function_lines": [node.lineno, node.end_lineno],
            "scope": "synthetic source-level probe; no measured prevalence, payoff or candidate", "cases": results}


def macro_audit():
    top = json.loads((ROOT / "moe/r6/top20.json").read_text())
    by_team = defaultdict(list)
    dates = Counter()
    total = exact = 0
    with (ROOT / "moe/r5/build/opus/macro.jsonl").open() as f:
        for line in f:
            row = json.loads(line)
            total += 1
            exact += all(row["match"])
            dates[row["date"]] += 1
            for seat, name in enumerate(row["teams"]):
                own, other = row["rewards"][seat], row["rewards"][1-seat]
                by_team[name].append((row["ep"], row["date"], own, (own > other) + 0.5 * (own == other)))
    rows = []
    for team in top:
        samples = by_team[team["team"]]
        rows.append({**team, "cached_seats": len(samples), "unique_episodes": len({s[0] for s in samples}),
                     "dates": sorted({s[1] for s in samples}),
                     "mean_bank": statistics.mean(s[2] for s in samples) if samples else None,
                     "win_fraction_ties_half": statistics.mean(s[3] for s in samples) if samples else None})
    return {"source": "moe/r5/build/opus/macro.jsonl", "episodes": total, "both_banks_exact": exact,
            "dates": dates, "matching": "Exact team-name match; no inferred aliases; existing Sep 23-25 cache only.",
            "limits": "Descriptive unequal-opponent sample; replay equality is not a reactive-policy model.", "top20": rows}


def main():
    paths = ["discussions.md", "HANDOFF.md", "MISTAKES.md", "moe/r6/BRIEF.md", "moe/r6/top20.json",
             "moe/r3/BRIEF.md", "moe/r3/opus.md", "moe/r3/build/opus/RESULT.md",
             "moe/r4/BRIEF.md", "moe/r4/THREAD.md", "moe/r4/opus.md", "moe/r4/opusb.md", "moe/r4/sonnet.md",
             "moe/r5/BRIEF.md", "moe/r5/THREAD.md", "moe/r5/opus.md", "moe/r5/opusb.md", "moe/r5/sonnet.md",
             "moe/opus/RESULT.md", "moe/opus/NOTES.md", "moe/codex/RESULT.md", "moe/r6/sonnet.md",
             "subZ_C1R2.py", ".venv/lib/python3.14/site-packages/kaggle_environments/envs/kaggriculture/kaggriculture.py"]
    for name in ["leoprovorov_kaggricult-man-reverse-engineering", "georgymamarin_kaggriculture-what-2600-farms-do-differently",
                 "destbreso_x-ray-your-agent", "degnonguidi_kaggriculture-utils-v1", "ashok205_top10-replay-dataset-archive"]:
        paths.extend(str(p.relative_to(ROOT)) for p in sorted((ROOT / "rivals9" / name).glob("*.ipynb")))
    discussion_lines = (ROOT / "discussions.md").read_text().splitlines()
    assert len(discussion_lines) == 12273, "Corpus changed since full read; inspect the change before updating coverage."
    assert discussion_lines[8738] == "Last version"
    manifest = {"created_utc": datetime.now(timezone.utc).isoformat(),
                "inputs": [fingerprint(ROOT / p) for p in paths if (ROOT / p).exists()],
                "discussion_versions_inclusive": [[1, 1, 1550], [2, 1551, 3201], [3, 3202, 4309],
                                                   [4, 4310, 6012], [5, 6013, 8738], ["Last version", 8739, 12273]],
                "coverage": "Full discussion read; substantive claims grouped in astra.md. Repeated UI/praise not ledger claims."}
    for name, obj in [("source_manifest.json", manifest), ("predict2_censor_probe.json", censor_probe()),
                      ("top20_cache_audit.json", macro_audit())]:
        (OUT / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"probe": "PASS", "outputs": ["source_manifest.json", "predict2_censor_probe.json", "top20_cache_audit.json"]}))


if __name__ == "__main__":
    main()
