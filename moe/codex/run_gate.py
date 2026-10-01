"""Run the mandated gate plus same-seed live controls, at most two workers."""
import os
import json
from pathlib import Path
import subprocess
import time
ROOT = Path(__file__).resolve().parents[2]
os.chdir(ROOT)
RUNS = [
    ('candidates', ['delivery=moe/codex/cand_delivery.py', 'capture=moe/codex/cand_capture.py']),
    ('controls', ['sir_control=subV_sir2.py', 'f55_control=subV2_f55rec.py']),
]
manifest = []
for tag, agents in RUNS:
    cmd = [str(ROOT / '.venv/bin/python'), 'moe/gate.py', '--only-candidates',
           '--workers', '2', '--seeds', '906', '24', '--out',
           'moe/codex/gate_' + tag + '.json'] + agents
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    with open('moe/codex/gate_' + tag + '.log', 'w') as log:
        proc = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT, env=env)
        run = {'tag': tag, 'command': cmd, 'pid': proc.pid, 'start': time.time()}
        manifest.append(run)
        Path('moe/codex/gate_manifest.json').write_text(json.dumps(manifest, indent=2))
        print('START', tag, 'pid', proc.pid, flush=True)
        code = proc.wait()
        run.update(exit_code=code, seconds=time.time()-run['start'])
        Path('moe/codex/gate_manifest.json').write_text(json.dumps(manifest, indent=2))
        print('DONE', tag, code, round(run['seconds'], 1), flush=True)
        if code:
            raise SystemExit(code)
