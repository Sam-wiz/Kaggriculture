import sys,importlib.util,concurrent.futures as cf
sys.path.insert(0,'.venv/lib/python3.14/site-packages')
from kaggle_environments import make

def loadm(p):
    spec=importlib.util.spec_from_file_location(p.replace('.','_'),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def scan(seed):
    a=loadm('subV_f55rec.py').agent
    env=make('kaggriculture',configuration={'episodeSteps':720,'seed':seed},debug=False)
    env.run([a,a])
    out=[]
    for seat in (0,1):
        placed=set();maxstray=0;straydays=0
        for t in range(1,719):
            obs=env.steps[t][seat].get('observation') or {}
            farm=(obs.get('farms') or [{}])[seat]
            for y,row in enumerate(farm.get('tiles') or []):
                for x,tile in enumerate(row):
                    if isinstance(tile,dict) and 'animal' in tile: placed.add((x,y))
            prv=obs.get('private') or {}
            stray=sum((prv.get('shed') or {}).get(x,0) for x in ('COW','SHEEP','GOOSE'))
            stray+=sum(sum(i.get(x,0) for x in ('COW','SHEEP','GOOSE')) for i in (prv.get('inventories') or []))
            maxstray=max(maxstray,stray)
            if stray and t%24==23: straydays+=1
        out.append((len(placed),maxstray,straydays))
    return seed,out

if __name__=='__main__':
    seeds=[int(x) for x in sys.argv[1].split(',')] if len(sys.argv)>1 else list(range(200,220))
    with cf.ProcessPoolExecutor(6) as ex:
        for seed,out in ex.map(scan,seeds):
            print(seed,out,flush=True)
