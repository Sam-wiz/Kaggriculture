"""Check the completed round-one report and emit its structured claim ledger."""
import ast
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPORT = HERE.parents[1] / "astra.md"
ROOT = HERE.parents[3]
text = REPORT.read_text()
rows = []
for line_no, line in enumerate(text.splitlines(), 1):
    if re.match(r"\| (?:T|M|I|V)\d{2} \|", line):
        cells = [v.strip() for v in line.split("|")[1:-1]]
        assert len(cells) == 4, (line_no, cells)
        rows.append(dict(id=cells[0], source=cells[1], claim=cells[2],
                         status_and_evidence=cells[3], report_line=line_no))
assert len(rows) == len({r["id"] for r in rows}) == 145
assert "ASTRA_FINAL_SECTIONS" not in text and "Report is being completed" not in text
links = re.findall(r"\]\(([^)]+)\)", text)
assert all(p.startswith(("http:", "https:", "#")) or (REPORT.parent / p).exists() for p in links)
for file in ("audit.py", "validate.py"):
    ast.parse((HERE / file).read_text())
manifest = json.loads((HERE / "source_manifest.json").read_text())
discussion = next(x for x in manifest["inputs"] if x["path"] == "discussions.md")
assert hashlib.sha256((ROOT / "discussions.md").read_bytes()).hexdigest() == discussion["sha256"]
probe = json.loads((HERE / "predict2_censor_probe.json").read_text())
assert [r["best"] for r in probe["cases"]] == [1, 1, 0]
cache = json.loads((HERE / "top20_cache_audit.json").read_text())
assert cache["episodes"] == cache["both_banks_exact"] == 1773
assert len(cache["top20"]) == 20
assert sum(r["cached_seats"] == 0 for r in cache["top20"]) == 8
summary = {"report_lines": len(text.splitlines()), "report_words": len(text.split()),
           "report_sha256": hashlib.sha256(REPORT.read_bytes()).hexdigest(),
           "ledger_rows": len(rows), "unique_ids": len(rows), "relative_links_checked": links,
           "unresolved_placeholders": False, "python_syntax": "PASS", "censor_probe": "PASS",
           "discussion_snapshot_unchanged": True, "top20_cache_audit": "PASS",
           "game_strength_tests": "not run in this lane"}
(HERE / "claim_ledger.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n")
(HERE / "validation.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
