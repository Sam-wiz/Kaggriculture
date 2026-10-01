"""One-game wiring diagnostic; no policy modifications or strength estimate."""
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / "moe/r3/build/opus"))
from run import load
import kagsim


def fingerprint(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def functions(path):
    tree = ast.parse(path.read_text())
    return {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}


def trim_tail(orders):
    result = list(orders or [])
    while result and not result[-1]:
        result.pop()
    return result


def main():
    started = time.monotonic()
    try:
        os.nice(10)
        priority = "nice +10"
    except PermissionError:
        priority = "nice denied; single foreground diagnostic"
    names = ["subAA_harvest.py", "subZ_C1R2.py"]
    source = [functions(ROOT / n) for n in names]
    discussion = (ROOT / "discussions.md").read_text()
    pattern = r"guru|v76|v78|harvest[ _-]*ledger|master[ _-]*engine[ _-]*v4"
    report = {
        "scope": "one seed, no holdout, wiring only; not a strength or causal estimate",
        "priority": priority,
        "input_sha256": {n: fingerprint(ROOT / n) for n in names + ["discussions.md"]},
        "discussion_lines": len(discussion.splitlines()),
        "discussion_pattern": pattern,
        "discussion_matches": len(re.findall(pattern, discussion, re.I)),
        "predict2_update_ast_equal": ast.dump(source[0]["_v92_q_update"]) == ast.dump(source[1]["_v92_q_update"]),
        "predict2_update_lines": {n: [s["_v92_q_update"].lineno, s["_v92_q_update"].end_lineno] for n, s in zip(names, source)},
    }
    a, ma = load(names[0], "astra_harvest_diag")
    b, mb = load(names[1], "astra_c1r2_diag")
    report["predict2_stream_counts"] = [len(m._v92_q_streams()) for m in (ma, mb)]
    seed = 9100001
    g = kagsim.Game(seed=seed)
    counts = {"market_diffs_trim_tail": 0, "market_diffs_remove_all_empty": 0,
              "masked_differences": 0, "tile_differences": 0}
    examples = []
    for step in range(719):
        aa = a(g.observe(0))
        bb = b(g.observe(1))
        assert isinstance(aa, dict) and isinstance(bb, dict)
        am, bm = trim_tail(aa.get("market")), trim_tail(bb.get("market"))
        real = am != bm
        stripped = [o for o in am if o] != [o for o in bm if o]
        counts["market_diffs_trim_tail"] += real
        counts["market_diffs_remove_all_empty"] += stripped
        counts["masked_differences"] += real and not stripped
        counts["tile_differences"] += (aa.get("farmer"), aa.get("hands") or []) != (bb.get("farmer"), bb.get("hands") or [])
        if real and not stripped and len(examples) < 4:
            examples.append({"step": step, "harvest": am, "c1r2": bm})
        g.step(aa, bb)
    report["game"] = {"seed": seed, "seats": names, "steps": 719,
                      "banks": [g.reward(i) for i in range(2)], "counts": counts,
                      "masked_examples": examples}
    report["harvest_telemetry"] = {k: v for k, v in vars(ma).items()
        if k.endswith("_REPORT") and isinstance(v, dict)}
    report["c1r2_predict2_telemetry"] = mb._V92_Q_REPORT
    report["elapsed_seconds"] = time.monotonic() - started
    target = OUT / "thread_harvest_check.json"
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "harvest_telemetry"}, indent=2))
    print("harvest key telemetry", json.dumps({k: report["harvest_telemetry"].get(k)
        for k in ("_V92_Q_REPORT", "_V44Y_REPORT", "_CXD_REPORT", "_S793_REPORT", "_S1009_REPORT")}))


if __name__ == "__main__":
    main()
