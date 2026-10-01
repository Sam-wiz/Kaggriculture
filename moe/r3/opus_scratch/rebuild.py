import json, os, sys, re
from pathlib import Path
def rebuild(nbpath, out):
    out=Path(out); out.mkdir(parents=True, exist_ok=True)
    nb=json.load(open(nbpath)); g={'NOTEBOOK_WORKDIR':str(out)}
    cwd=os.getcwd(); os.chdir(out)
    try:
        for c in nb['cells']:
            if c['cell_type']!='code': continue
            src=''.join(c['source'])
            if src.startswith('%%writefile'):
                first,rest=src.split('\n',1); fn=first.split()[1]
                (out/fn).write_text(rest); continue
            if 'kaggle_environments' in src or 'subprocess' in src or 'tarfile' in src or src.startswith('!'): continue
            if 'notebook_agent' in src: break
            try: exec(compile(src,'cell','exec'), g)
            except Exception as e: print('cell err', repr(e)[:100])
    finally: os.chdir(cwd)
    print(out, sorted(os.listdir(out)))
for slug in ['kaggriculture-herd-safe-sale-window-lb-2700','kaggriculture-7-turn-rescue-historical-lb-2800','kaggriculture-two-coins-one-sheep-lb-2600']:
    rebuild(f'rivals5/{slug}/{slug}.ipynb', f'/tmp/opus_r3/gz_{slug[14:30]}')
