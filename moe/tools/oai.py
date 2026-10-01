"""OpenAI API helper with a HARD spend cap (user budget: $6.00 of their $16 balance).

Every call's usage is appended to moe/tools/openai_ledger.json; a call is refused once recorded spend
reaches CAP. Key read from ~/.openai_env (`export OPENAI_API_KEY=...`) or env; never printed/logged.
    from moe.tools.oai import chat, spent
    text = chat("gpt-6-luna", "system prompt", "user prompt", max_output_tokens=8000)
"""
import json, os, re, time, urllib.request

CAP = 6.00
LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "openai_ledger.json")
PRICE = {  # $ per 1M tokens (input, output) — Sep 2026 list prices
    "gpt-6-luna": (0.10, 0.50), "gpt-6-sol": (2.00, 10.00),
    "gpt-5.6-luna": (0.20, 1.20), "gpt-5.6-sol": (4.00, 20.00), "gpt-5.6-terra": (2.00, 8.00)}


def _key():
    k = os.environ.get("OPENAI_API_KEY")
    if k: return k
    p = os.path.expanduser("~/.openai_env")
    m = re.search(r"OPENAI_API_KEY=(\S+)", open(p).read()) if os.path.exists(p) else None
    if not m: raise RuntimeError("OPENAI_API_KEY not found")
    return m.group(1).strip().strip("'\"")


def _ledger():
    return json.load(open(LEDGER)) if os.path.exists(LEDGER) else []


def spent():
    return round(sum(r["cost"] for r in _ledger()), 4)


def _req(path, body=None):
    req = urllib.request.Request("https://api.openai.com/v1/" + path, method="POST" if body else "GET",
                                 data=json.dumps(body).encode() if body else None,
                                 headers={"Authorization": "Bearer " + _key(), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=900) as r: return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"OpenAI HTTP {e.code}: {e.read()[:400].decode(errors='replace')}") from None


def models():
    return sorted(m["id"] for m in _req("models")["data"])


def chat(model, system, user, max_output_tokens=8000, effort="high", tag=""):
    if model not in PRICE: raise RuntimeError(f"no price for {model}; add it to PRICE first")
    pin, pout = PRICE[model]
    worst = len((system + user)) / 3.5 / 1e6 * pin + max_output_tokens / 1e6 * pout
    if spent() + worst > CAP:
        raise RuntimeError(f"refused: spent ${spent():.2f} + worst-case ${worst:.2f} would exceed cap ${CAP:.2f}")
    body = {"model": model, "max_output_tokens": max_output_tokens, "reasoning": {"effort": effort},
            "input": [{"role": "system", "content": system}, {"role": "user", "content": user}]}
    r = _req("responses", body)
    u = r.get("usage", {}); ti, to = u.get("input_tokens", 0), u.get("output_tokens", 0)
    cost = ti / 1e6 * pin + to / 1e6 * pout
    L = _ledger(); L.append({"t": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "model": model, "tag": tag,
                              "in": ti, "out": to, "cost": round(cost, 5)})
    json.dump(L, open(LEDGER, "w"), indent=1)
    text = r.get("output_text") or "".join(c.get("text", "") for o in r.get("output", []) if o.get("type") == "message"
                                            for c in o.get("content", []))
    return text


if __name__ == "__main__":
    ids = models()
    print("sol/luna/terra/astra ids:", [i for i in ids if any(s in i for s in ("sol", "luna", "terra", "astra"))])
