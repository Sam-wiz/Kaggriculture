"""Read-only Kaggle snapshot; never submits or automatically lifts the user hold.

Run from the competition directory: .venv/bin/python moe/r6/monitor_pair.py
Each successful snapshot is retained, appended to HANDOFF, and reflected in AGENTS.
"""
import csv
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'moe/r6/build/resume'
KA = str(ROOT / '.venv/bin/kaggle')
EXPECTED = {'56612454': 'Harvest', '56611551': 'C1R2'}


def fetch(args):
    result = subprocess.run([KA, 'competitions', *args, '-v'], capture_output=True,
                            text=True, timeout=180, cwd=ROOT, check=True)
    return result.stdout, list(csv.DictReader(io.StringIO(result.stdout)))


def main():
    now = datetime.now(timezone.utc)
    stamp = now.strftime('%Y%m%d_%H%M%S')
    raw, rows = fetch(['submissions', 'kaggriculture'])
    pair = rows[:2]
    if {r['ref'] for r in pair} != set(EXPECTED):
        raise RuntimeError('Live pair changed externally; inspect before updating notes.')
    folder = OUT / 'convergence' / stamp
    folder.mkdir(parents=True)
    (folder / 'submissions.csv').write_text(raw)
    facts = []
    for row in pair:
        raw, episodes = fetch(['episodes', row['ref']])
        (folder / (row['ref'] + '_episodes.csv')).write_text(raw)
        uploaded = datetime.fromisoformat(row['date']).replace(tzinfo=timezone.utc)
        facts.append(dict(name=EXPECTED[row['ref']], ref=row['ref'], score=float(row['publicScore']),
                          age_hours=round((now-uploaded).total_seconds()/3600,2),
                          listed_episodes=len(episodes),
                          completed_episodes=sum(r['state']=='EpisodeState.COMPLETED' for r in episodes),
                          status=row['status']))
    status = 'too early' if any(f['age_hours']<48 for f in facts) else 'needs convergence review'
    snapshot = dict(as_of=now.isoformat(), submissions=facts, convergence=status,
                    hold='No uploads until BOTH converge. No automatic release of this hold.')
    (folder / 'snapshot.json').write_text(json.dumps(snapshot, indent=2))
    with (OUT / 'convergence_history.jsonl').open('a') as f:
        f.write(json.dumps(snapshot)+'\n')
    concise = '; '.join(f"{x['name']} {x['score']:.1f}/{x['completed_episodes']} completed episodes ({x['age_hours']:.2f}h old)" for x in facts)
    note = f"> **Convergence snapshot {now.strftime('%m-%d %H:%M UTC')}:** {concise}; {status}."
    agents = ROOT/'AGENTS.md'
    text = agents.read_text()
    text, count = re.subn(r'^> \*\*Convergence snapshot[^\n]*', note, text, count=1, flags=re.M)
    if count != 1:
        raise RuntimeError('AGENTS convergence marker missing; snapshot saved, update notes manually.')
    agents.write_text(text)
    with (ROOT/'HANDOFF.md').open('a') as f:
        f.write(f"\n## Live-pair snapshot — {now.strftime('%Y-%m-%d %H:%M UTC')}\n\n{concise}. Convergence: {status}.\nUser submission hold remains. Evidence: `{folder.relative_to(ROOT)}/snapshot.json`.\n")
    print(json.dumps(snapshot, indent=2))


if __name__ == '__main__':
    main()
