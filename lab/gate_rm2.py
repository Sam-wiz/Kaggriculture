import sys
sys.path.insert(0,'.')
import bench_vs, harness
def kload(p):
    e={}; exec(compile(open(p).read(),p,'exec'),e); return e['agent']
A = kload('subV_sirxL96_rm2.py'); B = kload('subV_sirxL96.py')
w=l=t=0; tot=0; worst=0
for s in range(5000,5040):
    for aa,bb,sgn in ((A,B,1),(B,A,-1)):
        r = harness.run_episode(aa,bb,seed=s,catch_errors=True)
        m = sgn*(r['reward'][0]-r['reward'][1]); tot+=m; worst=min(worst,m)
        w += m>0; l += m<0; t += m==0
        print(f"s{s} {'AB' if sgn>0 else 'BA'}: {m:+.0f}", flush=True)
print(f"rm2 vs L96: W{w}-L{l}-T{t} margin={tot/80:+.0f} worst={worst}")
