"""Emit a runnable genome-agent file (loadable via run.load / drop-in
`agent(obs)`) that embeds one genome literal and compiles it at import.

Repo-local candidate: uses the installed islandga package + exec3
blueprint executor at repo root. NOT a self-contained Kaggle bundle —
a real submission would need islandga.compiler + exec3 inlined.
"""
import json
import sys
from pathlib import Path

ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
sys.path.insert(0, ROOT + "/kaggriculture-island-ga")

TEMPLATE = '''"""RL-searched islandga genome agent (gid {gid}). Research candidate —
requires islandga + exec3 on sys.path (repo environment)."""
import sys, json
ROOT = "{root}"
for _p in (ROOT, ROOT + "/kaggriculture-island-ga"):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import exec3
from islandga.compiler import compile_spec

GENOME = {genome}
_BP = compile_spec(json.loads(json.dumps(GENOME)))
_agent = exec3.make_agent(_BP)


def agent(obs):
    return _agent(obs)
'''


def emit(genome, path):
    from islandga.genome import gid_of
    Path(path).write_text(TEMPLATE.format(
        gid=gid_of(genome), root=ROOT,
        genome=json.dumps(genome, indent=1)))
    print(f"wrote {path} (gid {gid_of(genome)})")


if __name__ == "__main__":
    # emit_agent.py <genome.json | state.json> <out.py>
    src = json.loads(Path(sys.argv[1]).read_text())
    g = src.get("genome") or src.get("anchor") or src
    emit(g, sys.argv[2])
