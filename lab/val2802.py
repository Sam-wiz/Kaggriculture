import sys; sys.path.insert(0,'.')
import inco, kagsim, json
from multiprocessing import Pool
from collections import defaultdict
ROOT='/Users/samrudh/Documents/Projects/kaggle/Kaggriculture'
def game(args):
    a_path,b_path,seed,swapped=args
    sys.path.insert(0,ROOT)
    import inco, kagsim
    ag=inco.load_agent(ROOT+'/'+a_path); op=inco.load_agent(ROOT+'/'+b_path)
    g=kagsim.Game(seed=seed)
    for t in range(720):
        o0,o1=g.observe(0),g.observe(1)
        if swapped: g.step(op(o1),ag(o0))
        else: g.step(ag(o0),op(o1))
    return (a_path,b_path,seed,swapped,
            g.reward(1) if swapped else g.reward(0),
            g.reward(0) if swapped else g.reward(1))
if __name__=='__main__':
    A='rivals/jaxa623_2802/main.py'
    tasks=[]
    for opp in ('subI_pipe7.py','subH_v48.py'):
        for s in range(8400,8412):
            tasks.append((A,opp,s,False)); tasks.append((A,opp,s,True))
    with Pool(6) as p:
        for r in p.imap_unordered(game,tasks):
            a,b,s,sw,ra,rb=r
            print(f'{b[:12]} seed{s} {"s1" if sw else "s0"}: {ra:7.0f} vs {rb:7.0f}  {ra-rb:+7.0f}',flush=True)
