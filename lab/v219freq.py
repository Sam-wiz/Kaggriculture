import importlib.util,concurrent.futures as cf
from kaggle_environments import make
import subV_sirx as _m
def run(seed):
    seen=[None]
    parent=_m._V219_PARENT
    def spy(obs,configuration=None):
        if int(obs.get('step',0))==432:
            farm=obs['farms'][obs['player']]
            shops=sum(s in ('PIZZA_SHOP','FARMERS_MARKET') for s in obs['town']['unlocked_shops'])
            seen[0]=(shops,obs['market']['prices'].get('TOMATO'),farm['money'],
                     _m._v219_qualifies(obs,_m._IMPL.chassis.players[obs['player']]))
        return parent(obs,configuration)
    env=make('kaggriculture',configuration={'episodeSteps':720,'seed':seed},debug=False)
    env.run([spy,_m.agent]);return seed,seen[0]
if __name__=='__main__':
    with cf.ProcessPoolExecutor(max_workers=8) as ex:
        rows=list(ex.map(run,range(700,724)))
    for s,v in rows:
        if v:print('seed',s,'shops',v[0],'price',v[1],'money',v[2],'qualified',v[3])
