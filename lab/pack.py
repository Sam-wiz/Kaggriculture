"""Package a blueprint + exec3 executor into a self-contained main.py.

Usage: python pack.py <bp.json> <out.py>
The output imports nothing outside the stdlib.
"""
import json
import sys
from pathlib import Path

ROOT = Path("/Users/samrudh/Documents/Projects/kaggle/Kaggriculture")
FACTS = ROOT / "kaggriculture-island-ga/islandga/engine_facts.py"
EXEC = ROOT / "exec3.py"


def build(bp_path, out_path):
    bp = json.loads(Path(bp_path).read_text())
    facts_src = FACTS.read_text()
    exec_src = EXEC.read_text()
    # strip the islandga import from exec3 and the docstring header
    exec_src = exec_src.replace(
        "from islandga.engine_facts import ANIMALS, CROPS, SHED_TILES\n", "")
    # keep only the constants from engine_facts (drop price()/shapes —
    # the executor never calls them)
    cut = facts_src.index("def shape(")
    facts_src = facts_src[:cut]
    facts_src = facts_src.split('"""', 2)[2]  # drop module docstring

    out = '"""Kaggriculture agent: compiled blueprint + row-walker executor."""\n'
    out += facts_src
    out += "\nBP = " + repr(bp) + "\n\n"
    out += exec_src
    out += "\n_EX = Executor3(BP)\n\n\ndef agent(obs):\n    return _EX.act(obs)\n"
    Path(out_path).write_text(out)
    print(f"wrote {out_path} ({len(out)} bytes)")


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
