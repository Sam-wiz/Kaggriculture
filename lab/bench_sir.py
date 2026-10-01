import sys,importlib.util,concurrent.futures as cf,statistics
from kaggle_environments import make
def loadm(p):
    spec=importlib.util.spec_from_file_location(p.replace('.','_'),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def game(ap,bp,seed):
    a=loadm(ap).agent;b=loadm(bp).agent
    env=make('kaggriculture',configuration={'episodeSteps':720,'seed':seed},debug=False)
    env.run([a,b]);return [s.reward for s in env.steps[-1]]
def pair(args):
    ap,bp,seed=args
    r1=game(ap,bp,seed);r2=game(bp,ap,seed)
    return seed,r1,r2,[r1[0]-r1[1],r2[1]-r2[0]]
if __name__=='__main__':
    cand=sys.argv[1];opp=sys.argv[2];seeds=[int(s) for s in sys.argv[3].split(',')]
    with cf.ProcessPoolExecutor(max_workers=8) as ex:
        rows=list(ex.map(pair,[(cand,opp,s) for s in seeds]))
    ms=[m for _,_,_,mm in rows for m in mm]
    w=sum(1 for m in ms if m>0);l=sum(1 for m in ms if m<0)
    print(f'{cand} vs {opp}: {w}-{l} mean={statistics.mean(ms):+.0f} med={statistics.median(ms):+.0f} worst={min(ms):+.0f}')
    for s,r1,r2,mm in rows:print(f'  s{s}: {r1} -> {mm[0]:+.0f} | {r2} -> {mm[1]:+.0f}')
