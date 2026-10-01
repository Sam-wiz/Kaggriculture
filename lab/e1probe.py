import importlib.util,concurrent.futures as cf,collections
from kaggle_environments import make
import subV_sirx as _m
def run(seed):
    parent=_m._prm_base
    stats=collections.Counter()
    def spy(obs,configuration=None):
        a=parent(obs,configuration)
        day=int(obs.get('day',0))
        if day>=24:
            mkt=(a or {}).get('market') or []
            shed=(obs.get('private') or {}).get('shed') or {}
            # tape sells = sells already in list; overlay adds appended sells for items not already selling
            for o in mkt:
                if o and o[0]=='SELL':
                    stats[f'd{min(day,29)}_{o[1]}']+=o[2]
            stats['turns']+=1
        return a
    env=make('kaggriculture',configuration={'episodeSteps':720,'seed':seed},debug=False)
    env.run([spy,_m.agent])
    return dict(stats)
if __name__=='__main__':
    tot=collections.Counter()
    with cf.ProcessPoolExecutor(max_workers=8) as ex:
        for d in ex.map(run,range(700,708)):tot.update(d)
    for k in sorted(tot):
        if not k=='turns':print(k,tot[k])
