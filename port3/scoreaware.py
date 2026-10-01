"""Play the SCOREBOARD, not the bank.

The ladder scores win/loss only -- measured directly: a $596 loss cost -5.80 rating while a $16,891
loss cost -4.70. So the objective is P(final margin > 0), not expected dollars. With a game-to-game
spread of ~$4,295, those objectives diverge sharply near the end:

  * BEHIND  -> increase variance. A coin flip beats a certain loss. Holding stock is a
               mean-negative, variance-positive action (measured -103 to -2,059 on average) --
               exactly what you want when the average is already losing.
  * AHEAD   -> decrease variance. Convert inventory to banked cash and stop gambling.

Both banks are public every turn, so this is fully observable. As far as we can tell from mined
replays, no agent in this competition -- including the top 3 -- plays conditionally on the score.
"""

SC = dict(enabled=1, from_day=21, behind=-1200, ahead=1200, dump_day=28, max_hold_day=28)


def adjust(obs, market):
    if not SC["enabled"]:
        return market
    try:
        day = int(obs.get("day", 0) or 0)
        if day < SC["from_day"]:
            return market
        me = obs["player"]
        farms = obs["farms"]
        lead = float(farms[me]["money"]) - float(farms[1 - me]["money"])
        shed = (obs.get("private") or {}).get("shed") or {}
        prices = (obs.get("market") or {}).get("prices") or {}

        if lead < SC["behind"] and day < SC["max_hold_day"]:
            # losing on the current line: stop realising it, build a lumpy position instead
            return [o for o in market if not (o and o[0] == "SELL")]

        if lead < SC["behind"] or day >= SC["dump_day"]:
            # cash the held position in
            held = {k: int(v) for k, v in shed.items()
                    if isinstance(v, (int, float)) and v > 0 and k in prices}
            for o in market:
                if o and o[0] == "SELL" and len(o) > 2 and o[1] in held:
                    held[o[1]] = max(0, held[o[1]] - int(o[2]))
            extra = [["SELL", k, v] for k, v in held.items() if v > 0]
            extra.sort(key=lambda o: -(float(prices.get(o[1], 0) or 0) * o[2]))
            return (list(market) + extra)[:10]

        if lead > SC["ahead"]:
            # winning: bank everything, take no further price risk
            held = {k: int(v) for k, v in shed.items()
                    if isinstance(v, (int, float)) and v > 0 and k in prices}
            for o in market:
                if o and o[0] == "SELL" and len(o) > 2 and o[1] in held:
                    held[o[1]] = max(0, held[o[1]] - int(o[2]))
            extra = [["SELL", k, v] for k, v in held.items() if v > 0]
            extra.sort(key=lambda o: -(float(prices.get(o[1], 0) or 0) * o[2]))
            return (list(market) + extra)[:10]
    except Exception:
        pass
    return market
