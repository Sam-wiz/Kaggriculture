"""Minimal Jev (TypeSafe System One) client for OFFLINE triage in the MoE.

Jev returns calibrated probabilities for typed questions about a TEXT state. It does not generate
text, cannot learn from examples, and cannot be called from a Kaggle submission (no network there).
Use it for cheap labelling/ranking at scale; verify anything that matters with exact engine replay.

    from moe.tools.jev import ask
    ans = ask("state text ...", {
        "family": {"type": "choice", "instructions": "...", "criteria": {"a": "...", "b": "..."}},
        "reactive": {"type": "noul", "instructions": "..."},
        "risk": {"type": "score", "instructions": "...", "criteria": ["low", "mid", "high"]}})

The key is read from ~/.typesafe_env (`export TYPESAFE_API_KEY=...`) or the environment; never logged.
"""
import json, os, re, urllib.request

URL = "https://api.typesafe.ai/v1/systemone"


def _key():
    k = os.environ.get("TYPESAFE_API_KEY")
    if k: return k
    p = os.path.expanduser("~/.typesafe_env")
    m = re.search(r"TYPESAFE_API_KEY=(\S+)", open(p).read()) if os.path.exists(p) else None
    if not m: raise RuntimeError("TYPESAFE_API_KEY not found (env or ~/.typesafe_env)")
    return m.group(1).strip().strip("'\"")


def ask(state, questions, model="jev-latest", timeout=30):
    body = json.dumps({"state": state, "model": model, "questions": questions}).encode()
    req = urllib.request.Request(URL, data=body, method="POST", headers={
        "Authorization": "Bearer " + _key(), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Jev HTTP {e.code}: {e.read()[:300].decode(errors='replace')}") from None


if __name__ == "__main__":
    out = ask("Farm agent opened by buying 5 wheat and selling 0; kept 5 cows and 4 sheep; sold milk "
              "early on days 13-24 in small lots every few turns.",
              {"opening": {"type": "choice", "instructions": "Which opening family does this describe",
                           "criteria": {"five_zero": "buys 5 wheat, sells none at step 1",
                                        "twenty_fifteen": "buys 20 wheat, sells 15",
                                        "eight_three": "buys 8 wheat, sells 3"}},
               "early_seller": {"type": "noul", "instructions": "The agent sells premium goods early rather than holding them"}})
    print(json.dumps(out, indent=1)[:1500])
