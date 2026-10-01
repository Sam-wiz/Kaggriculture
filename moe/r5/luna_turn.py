"""One discussion turn for an OpenAI participant (default gpt-6-luna) — capped via moe/tools/oai.py.
Reads THREAD.md + round-1 positions, asks for exactly one post, appends it. usage: luna_turn.py [model] [name]"""
import os, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, ROOT); os.chdir(ROOT)
from moe.tools.oai import chat, spent
model = sys.argv[1] if len(sys.argv) > 1 else "gpt-6-luna"; name = sys.argv[2] if len(sys.argv) > 2 else "luna"
def rd(p, n=60000):
    return open(p).read()[:n] if os.path.exists(p) else "(not written yet)"
ctx = "\n\n".join(f"===== {p} =====\n{rd(p)}" for p in
                  ("moe/r5/BRIEF.md", "moe/r5/sonnet.md", "moe/r5/opus.md", "moe/r5/opusb.md"))
thread = rd("moe/r5/THREAD.md", 120000)
system = (f"You are '{name}', a sharp, skeptical expert in a live mixture-of-experts discussion about a Kaggle "
          "farming-simulation agent competition (Kaggriculture). You cannot run code; you reason from the "
          "evidence quoted. Your job: find the weakest claims, missing controls, and the highest-value next "
          "experiment. Be concrete and brief. Never invent numbers; cite the file/number you are using.")
user = (f"Context files:\n{ctx}\n\n===== THREAD SO FAR =====\n{thread}\n\n"
        f"Write exactly ONE new post for the thread, following its rules. Start with the header line "
        f"`### [{name}] {time.strftime('%H:%M', time.gmtime())} UTC — re: <who/what>`. <= 300 words. "
        "Include AGREE / DISPUTE / NEW POINT as relevant, reply to participants by name, and end with "
        "**Next action (<owner>):** one concrete, checkable step. Output only the post.")
post = chat(model, system, user, max_output_tokens=4000, effort="high", tag=f"thread-{name}").strip()
with open("moe/r5/THREAD.md", "a") as f: f.write("\n\n" + post + "\n")
print(post); print(f"\n[ledger total ${spent():.4f}]")
