import sys,json
exec(open('/tmp/opus_r3b/ablate.py').read().rsplit('\nif __name__', 1)[0])
if __name__=="__main__":
    games=json.load(open('/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r3/opus_scratch/wl_games.json'))
    Y='rivals4/kaggriculture-yummers/_entry.py'
    jobs=[]
    for g in games:
        jobs.append(('shep_wllib','/tmp/opus_r3b/shep_wllib.py','yummers',Y,g['seed'],g['seat']))
        jobs.append(('shep','subW_shepherd.py','wl_ourlib','/tmp/opus_r3b/wl_ourlib.py',g['seed'],g['seat']))
    with ProcessPoolExecutor(max_workers=2) as ex, open('/tmp/opus_r3b/swap.jsonl','w') as f:
        for res in ex.map(game2, jobs, chunksize=1):
            f.write(json.dumps(res)+"\n"); f.flush()
