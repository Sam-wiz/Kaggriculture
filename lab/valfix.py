import sys; sys.path.insert(0,'.')
import inco, kagsim
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
        if swapped: g.step(op(o0),ag(o1))   # op on seat0, candidate on seat1
        else: g.step(ag(o0),op(o1))
    return (a_path,b_path,seed,swapped,
            g.reward(1) if swapped else g.reward(0),
            g.reward(0) if swapped else g.reward(1))
if __name__=='__main__':
    cands={'2802':'rivals/jaxa623_2802/main.py',
           '2780':'rivals/2780-beyond-48-0-128-128-worlds-with-95-cis/main.py',
           '2945':'rivals/the-2945-farm-96-vs-the-top-10-public-bots/main.py'}
    tasks=[]
    for name,A in cands.items():
        for opp in ('subI_pipe7.py','subH_v48.py'):
            for s in range(8600,8610):
                tasks.append((A,opp,s,False)); tasks.append((A,opp,s,True))
    agg=defaultdict(lambda:[0,0,0])
    seats=defaultdict(lambda:[0,0,0])
    with Pool(6) as p:
        for r in p.imap_unordered(game,tasks):
            a,b,s,sw,ra,rb=r
            k=(a.split('/')[1][:20],b[:12])
            agg[k][0]+=ra-rb; agg[k][1]+=ra>rb; agg[k][2]+=1
            sk=k+('s1' if sw else 's0',)
            seats[sk][0]+=ra-rb; seats[sk][1]+=ra>rb; seats[sk][2]+=1
    for k,(mg,w,n) in sorted(agg.items()):
        print(f'{k[0]:22s} vs {k[1]:12s}: W{w:2d}-L{n-w:2d} {mg/n:+7.0f}', end='')
        for seat in ('s0','s1'):
            sk=k+(seat,)
            if sk in seats: print(f'  [{seat}:{seats[sk][0]/seats[sk][2]:+6.0f} W{seats[sk][1]}]',end='')
        print(flush=True)
