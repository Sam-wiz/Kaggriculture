import sys,importlib.util,concurrent.futures as cf
sys.path.insert(0,'.venv/lib/python3.14/site-packages')
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
    return seed,[r1[0]-r1[1],r2[1]-r2[0]]

def mirror(args):
    ap,seed=args
    a=loadm(ap).agent
    env=make('kaggriculture',configuration={'episodeSteps':720,'seed':seed},debug=False)
    env.run([a,a]);return [s.reward for s in env.steps[-1]]

if __name__=='__main__':
    cand=sys.argv[1] if len(sys.argv)>1 else 'subV_cattleD.py'
    seeds=[int(x) for x in sys.argv[2].split(',')] if len(sys.argv)>2 else list(range(200,212))
    opps=sys.argv[3].split(',') if len(sys.argv)>3 else ['subK_pipe16.py','subN_metav4.py']
    with cf.ProcessPoolExecutor(6) as ex:
        for opp in opps:
            res=list(ex.map(pair,[(cand,opp,s) for s in seeds]))
            d=[x for _,r in res for x in r]
            w=sum(1 for x in d if x>0)
            print(f'{cand} vs {opp}: W{w}/{len(d)} avg {sum(d)/len(d):+.0f} min {min(d):+.0f}',flush=True)
        res=list(ex.map(mirror,[(cand,s) for s in seeds]))
        mb=[x for r in res for x in r]
        print(f'{cand} mirror banks: avg {sum(mb)/len(mb):.0f}',flush=True)
