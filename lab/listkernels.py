"""Enumerate every Kaggriculture notebook via Kaggle's internal ListKernels endpoint.

The public CLI caps out and sorts awkwardly; this walks the same paginated endpoint the competition
Code tab uses, so it sees everything including very recent kernels the CLI has not indexed yet.

Credentials come from the session cookie/XSRF pair the user supplied, read from a local file rather
than embedded here. Writes one row per kernel: ref, title, author, votes, last-run time.

Usage:  python listkernels.py [out.json]
"""
import json
import os
import sys
import time
import urllib.request

URL = "https://www.kaggle.com/api/i/kernels.KernelsService/ListKernels"
COMPETITION_ID = 147734
AUTH = "data/kaggle_session.json"       # {"cookie": "...", "xsrf": "...", "build": "..."}


def headers():
    a = json.load(open(AUTH))
    return {
        "accept": "application/json",
        "content-type": "application/json",
        "cookie": a["cookie"],
        "origin": "https://www.kaggle.com",
        "referer": "https://www.kaggle.com/competitions/kaggriculture/code",
        "user-agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"),
        "x-kaggle-build-version": a.get("build", ""),
        "x-xsrf-token": a["xsrf"],
    }


def page(n, sort="HOTNESS", size=100):
    body = {
        "kernelFilterCriteria": {
            "search": "",
            "listRequest": {
                "competitionId": COMPETITION_ID, "sortBy": sort, "pageSize": size,
                "group": "EVERYONE", "page": n, "modelIds": [], "modelInstanceIds": [],
                "excludeKernelIds": [], "tagIds": "", "excludeResultsFilesOutputs": False,
                "wantOutputFiles": False, "excludeNonAccessedDatasources": True,
            },
        },
        "detailFilterCriteria": {
            "deletedAccessBehavior": "RETURN_NOTHING",
            "unauthorizedAccessBehavior": "RETURN_NOTHING",
            "excludeResultsFilesOutputs": False, "wantOutputFiles": False,
            "kernelIds": [], "outputFileTypes": [], "includeInvalidDataSources": False,
        },
        "readMask": "pinnedKernels",
    }
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers=headers())
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def rows(payload):
    out = []
    for k in (payload.get("kernels") or []):
        author = ((k.get("author") or {}).get("displayName")
                  or (k.get("author") or {}).get("userName") or "")
        slug = k.get("scriptUrl") or ""
        out.append(dict(ref=slug.lstrip("/"), title=k.get("title"), author=author,
                        votes=k.get("totalVotes"), last_run=k.get("scriptVersionDateRun"),
                        kernel_id=k.get("id")))
    return out


def main(out_path="data/kernels.json", sorts=("HOTNESS", "DATE_RUN", "VOTE_COUNT")):
    seen = {}
    for sort in sorts:
        for n in range(1, 60):
            try:
                payload = page(n, sort=sort)
            except Exception as e:
                print(f"  {sort} page {n}: {type(e).__name__} {e}", flush=True)
                break
            rs = rows(payload)
            if not rs:
                print(f"  {sort}: exhausted at page {n}", flush=True)
                break
            new = 0
            for r in rs:
                if r["ref"] and r["ref"] not in seen:
                    seen[r["ref"]] = r
                    new += 1
            print(f"  {sort} page {n}: {len(rs)} rows, {new} new (total {len(seen)})", flush=True)
            time.sleep(0.4)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    json.dump(list(seen.values()), open(out_path, "w"), indent=1)
    print(f"\n{len(seen)} distinct kernels -> {out_path}")
    return seen


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/kernels.json")
