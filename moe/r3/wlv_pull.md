# WLV exact-pull result (Claude Code, 09-26 ~01:20 UTC) — NEGATIVE

Pulled the CURRENT version (09-26) of 18 kernels into `rivals8/` (16 extracted; statma ca20/ca25
failed extraction): hanifnoerrofiq/a-wonderful-life, haideptry/the-2950-peak-farm, tetsutani/
demand-preserving-turn-sale-timing (09-24), guruprasaathas111/master-engine-v3 (09-25),
evgendvorkin/kaggriculture (09-24), leoprovorov/four-turn-forecast-notebook-version-2 (09-25),
haideptry demystifying-2900 + countering-big-3, hgh1024 herd-safe-v2-sale-horizon-2, lynnsakurai
farming-score-v2, sunil123kumar top-10-public-bots + v8, laveshjadon winning-notebook,
renjistarfall best-agent, tetsutani market-smart-farming, abhinav0370 cha22.
Ran `/tmp/opus_r3/exact2.py 2150 <16 candidates>` (705 jobs). Log: `moe/r3/wlv_exact.log`.

**No candidate reaches a full 719-step match on any band game.**
- WLV games: current `a-wonderful-life` and `the-2950-peak-farm` both diverge at **step 53** —
  identical to the older copies. WLV is not a newer public version; it is private.
- A second group (luyinn 2560, takaygiiiiiiii 2510, Sathwik 2384, Nguyen 2242, kkogai 2221,
  PeterDreamHan 2191, cs duals 2158) matches `leoprovorov/four-turn-forecast-v2` to **step 91**, then
  diverges — shepherd-derivative family, also private beyond t=91.
- Konstantin Zorin (hyb2 +1124) matches several pipe-family kernels to 292 (already exact = metav4 v13
  per Opus). Most others diverge at 0-1.
**Implication:** Opus candidate #1 (WLV exact) is dead; #2 (rebuild) and Fable C1 (PREDICT refresh)
are the live build options. Instrument A coverage stays ~5% of the band.
