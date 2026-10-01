"""Run cbfork_agent under the official env.run (both seats) vs C1, plus a no-fork C1-vs-C1 reference on the same seed.
usage: cbfork_run.py SEED [SEED ...]"""
import io, contextlib, json, os, subprocess, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT)
from kaggle_environments import make
C1 = ROOT + "/subY_C1_predict2.py"
FK = ROOT + "/moe/r5/build/opusb/cbfork_agent.py"


def run(a, b, seed):
    env = make("kaggriculture", configuration={"episodeSteps": 720, "seed": seed}, debug=False)
    t0 = time.time()
    with contextlib.redirect_stdout(io.StringIO()):
        env.run([a, b])
    fin = env.steps[-1]
    return [s.reward for s in fin], [s.status for s in fin], round(time.time() - t0, 1)


for seed in map(int, sys.argv[1:]):
    ref = run(C1, C1, seed)
    f0 = run(FK, C1, seed)
    f1 = run(C1, FK, seed)
    zomb = subprocess.run(["ps", "-o", "pid,stat,comm", "--ppid", str(os.getpid())], capture_output=True, text=True).stdout \
        if sys.platform != "darwin" else subprocess.run(["ps", "-A", "-o", "pid,ppid,stat"], capture_output=True, text=True).stdout
    z = [l for l in zomb.splitlines()[1:] if l.split()[1] == str(os.getpid())]
    print(json.dumps(dict(seed=seed, ref=ref, fork_seat0=f0, fork_seat1=f1,
                          seat0_identical=f0[0] == ref[0], seat1_identical=f1[0] == ref[0], children_left=z)), flush=True)
