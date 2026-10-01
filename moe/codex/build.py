"""Build two self-contained, frozen candidates. Never run during a measurement."""
from pathlib import Path
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('--check', action='store_true')
ap.add_argument('names', nargs='*', choices=['delivery', 'capture'])
args = ap.parse_args()
ROOT = Path(__file__).resolve().parents[2]
source = (ROOT / 'subV_sir2.py').read_text()
layer = (ROOT / 'moe/codex/endgame_layer.inc').read_text()
for name, fix in [('delivery', False), ('capture', True)]:
    if args.names and name not in args.names:
        continue
    candidate_layer = layer
    if not fix:
        # Preserve the frozen delivery artifact's original (unused) worker
        # helper. The guarded helper was added before building capture.
        start = candidate_layer.index('def _ec_worker(observation, actor, targets):')
        end = candidate_layer.index('def _ec_agent(', start)
        candidate_layer = candidate_layer[:start] + candidate_layer[end:]
        candidate_layer = candidate_layer.replace('def _ec_worker_impl(', 'def _ec_worker(', 1)
    out = ROOT / ('moe/codex/cand_' + name + '.py')
    expected = source + '\n_EC_FIX_WORKERS = ' + str(fix) + '\n' + candidate_layer
    if args.check:
        assert out.read_text() == expected, str(out) + ' differs from builder'
    else:
        out.write_text(expected)
    print(out.relative_to(ROOT), out.stat().st_size)
