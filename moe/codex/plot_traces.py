"""Export a compact mechanism figure from measured engine fills."""
import os
os.environ.setdefault('MPLCONFIGDIR', 'moe/codex/.mplconfig')
os.environ.setdefault('XDG_CACHE_HOME', 'moe/codex/.cache')
import json
from pathlib import Path
import statistics
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE = Path(__file__).resolve().parent
fig, axes = plt.subplots(1, 2, figsize=(12, 4), layout='constrained')
colors = {'baseline':'#616161', 'delivery':'#3283b5', 'capture':'#148c60'}
representative = {}
for label in colors:
    rows = [json.loads(l) for l in (HERE/f'trace_{label}.jsonl').read_text().splitlines()]
    rows = [r for r in rows if 'koshinm' in r['opponent']]
    curves = []
    for r in rows:
        data = json.loads(Path(r['path']).read_text())
        p = r['seat']
        curves.append([st['after_money'][p]-st['after_money'][1-p] for st in data['steps']])
        if r['seed']==900902 and p==0:
            representative[label] = data
    means = [statistics.mean(x) for x in zip(*curves)]
    axes[0].plot(range(len(means)), means, label=label, color=colors[label], linewidth=1.8)
axes[0].axvspan(504,718,color='#148c60',alpha=.07)
axes[0].axhline(0,color='#aaaaaa',linewidth=.7)
axes[0].set(xlabel='Action step',ylabel='Bank margin vs koshinm ($)',
            title='Development panel: 6 seeds × both seats')
axes[0].legend(frameon=False)
for label, style in [('baseline','--'),('capture','-')]:
    data = representative[label]
    totals = [0,0]
    curves = [[],[]]
    for st in data['steps'][648:]:
        for p,slot,op,item,price in st['fills']:
            if op=='SELL' and item=='WOOL':
                totals[p]+=price
        for p in (0,1):
            curves[p].append(totals[p])
    for p, name, color in [(0,'ours','#148c60'),(1,'koshinm','#b65e37')]:
        axes[1].step(range(648,719),curves[p],where='post',linestyle=style,
                     color=color,label=f'{label}: {name}',linewidth=1.8)
axes[1].set(xlabel='Action step',ylabel='Cumulative wool receipts ($)',
            title='Seed 900902, seat 0: 62 wool sold per side')
axes[1].legend(frameon=False)
for ax in axes:
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='y',alpha=.15)
fig.savefig(HERE/'endgame_mechanism.png',dpi=180)
fig.savefig(HERE/'endgame_mechanism.pdf')
