# MoE r6 — decode the top 20 + the forum, live debate. 2026-09-27 14:45 UTC. Deadline 09-30 23:59 UTC.

Participants: **opus** (Opus 5.5 xhigh), **opusb** (Opus 5.5 xhigh), **sonnet** (Sonnet 5 xhigh),
**astra** (Codex gpt-6-astra xhigh, via ChatGPT login — NO OpenAI API credits may be used; the
moe/tools/oai.py helper is off-limits this round), **claude-code** (orchestrator + participant; the only
one with Kaggle credentials; uploads). You cannot submit. <=2 workers each, nice 10.
Write only `moe/r6/<you>.md`, `moe/r6/build/<you>/`, and posts appended to `moe/r6/THREAD.md`.

## State
- Live pair [C1 `subY_C1_predict2.py` (56560349, ~1672 @~100 games, RR-mapped ~2076), C1R2 `subZ_C1R2.py`
  (56611551, uploaded 14:39 UTC today, RR-mapped 2152 [2021, 2294])]. Bronze ~2210, silver ~2410, #10 2884.
- r5 closed every buildable route to top-family play by 09-30: recorded tapes (raw 8/125, router 0.24,
  TS 3/32, NN 0/8, day-splice 0/20), exec3, and family macro options on C1 (O1/O2 −$9k..−17k/g, O3
  ceiling +$109/g, C1noV233 −$307/g). The only instrument that retrodicts live is opus's lineage RR map
  (`moe/r4/build/opus/rr.py`, `c1map.py`, `moe/r4/screen2.py`). Read `moe/r5/THREAD.md` tail + HANDOFF.md
  from `## 09-26f`.

## The user's asks this round
1. **"Sit and decode all 20."** Top 20 on the current LB: `moe/r6/top20.json`. For EACH team produce a
   dossier from the top-episode dumps: `mine/top10/*.json.gz` (09-23..25, 1,773 games; 09-26 streaming in
   now, ~600 more). Per team: lineage/family (opening fingerprint, shared-code evidence), macro schedule
   (land steps, hires/day, herd, crops by day), market policy (what/when/how much sold, captured price,
   collisions), reactivity (within-team identity; does the plan move with the shop draw / opponent?),
   compute signature if visible, head-to-head record vs the rest of the top 20, and **"what could we
   adopt or exploit"** — concrete and testable. Every replay reproduces to the dollar; exact per-tick
   state is recoverable (tools: `moe/r5/build/opus/macro.py`, `moe/r4/build/opus/`, `moe/r5/build/opusb/`).
2. **"Go through discussions again" — `discussions.md` (Versions 1-5 now; the user may add V6).** Re-read
   ALL of it. Extract every concrete mechanism/strategy claim (who, what, numbers), check each against
   what we measured (HANDOFF.md, MISTAKES.md, moe/r*/) and against the decoded top 20, and list what is
   still untested and could matter by 09-30.
3. **Debate live** in `moe/r6/THREAD.md` (rules as moe/r4/THREAD.md: reply by name, evidence with paths +
   numbers, <=300 words, end with **Next action (<owner>):**). Then converge on "ways": ranked,
   testable-before-deadline changes, each with its kill test on the RR map.

## Lanes (round 1 = your file; then thread rounds)
- **opus:** decode ranks 1-10 -> `moe/r6/opus.md` (+ per-team tables in build/opus/).
- **opusb:** decode ranks 11-20 -> `moe/r6/opusb.md`.
- **astra:** full re-read of discussions.md -> `moe/r6/astra.md`: claim ledger (claim, source line,
  status: confirmed / refuted / untested by us, evidence), and the top untested ideas.
- **sonnet:** red team + synthesis -> `moe/r6/sonnet.md`: which decoded differences are plausibly causal,
  which forum claims are worth a test, and a ranked "ways" list with kill tests and hours.
Foreground only (one-shot session; no background jobs). You MUST write your file before finishing.
End with P(bronze), P(silver), P(top-10) for the final pair under your best plan.

## ADDENDUM (15:10 UTC) — public notebooks refreshed (user request)
19 kernels run/updated since 09-25 20:00 UTC pulled fresh into `rivals9/` (18 ok). Agents: 8 genuinely new
code files (stage-1 screen vs C1 running: `moe/r6/screen9.log`). **Write-ups worth reading for the decode
and forum lanes** (markdown inside the .ipynb): `rivals9/leoprovorov_kaggricult-man-reverse-engineering/`
(141 votes — someone else's reverse-engineering of top agents), `rivals9/georgymamarin_kaggriculture-what-
2600-farms-do-differently/`, `rivals9/destbreso_x-ray-your-agent/`, `rivals9/degnonguidi_kaggriculture-
utils-v1/`, `rivals9/ashok205_top10-replay-dataset-archive/`. Check their claims against your decode.
Note: haideptry's shepherd notebook now ships a DIFFERENT agent (matches code we already hold).

## ADDENDUM 2 (user) — discussions.md VERSION 6 added
New content = from the line "Last version" (**line 8739**) to the end (**line 12272**, ~173 KB, ~3,500 lines).
It opens with dzjiann's "My RL Won, But Also Failed: Two Days of Training on a 196-Core Server".
astra: extend your claim ledger to V6 (tag each claim V6). Everyone: bring V6 evidence into the thread.
