"""
Q1 evidence: what separates 3000+ agents from 2800-2900 ones, at scale.

Uses meta/{episodes,agents,episode_features}.csv (georgymamarin dump, pre-lock,
covers 2026-07-30..2026-09-20). Joins per-episode-per-seat features to that
seat's rating_after, buckets by rating band, and reports feature means.

Two views:
  (A) episode-level: every (episode, seat) row, bucketed by its own rating_after.
      Large N, but a single submission contributes many rows across its
      convergence trajectory (climbing from ~600 up).
  (B) submission-level: one row per submission_id, using its PEAK observed
      rating_after to assign a band, and MEDIAN features across all its
      episodes. Avoids double-counting a climb; answers "what do agents that
      reached 3000+ actually do" vs "what do 2800-2900 agents do".
"""
import pandas as pd
import numpy as np

pd.set_option("display.width", 160)
pd.set_option("display.max_columns", 30)

AG = pd.read_csv("meta/agents.csv")
EF = pd.read_csv("meta/episode_features.csv")

# agents.csv: episode_id, agent_index, submission_id, team_id, final_bank, rating_after
# episode_features.csv: episode_id, seat, engine_version, final_money, peak_crew,
#   total_hires, first_land_day, elbow_day, tiles_planted, plants_*, price_*_max/min
df = AG.merge(EF, left_on=["episode_id", "agent_index"], right_on=["episode_id", "seat"], how="inner")
print(f"merged rows: {len(df)} (AG={len(AG)}, EF={len(EF)})")
print("engine_version counts:\n", df["engine_version"].value_counts())

# restrict to the current engine line to avoid mixing rule versions
df = df[df["engine_version"].astype(str).str.startswith("1.32")].copy()
print(f"after engine filter: {len(df)}")

BANDS = [(-1, 2000), (2000, 2400), (2400, 2800), (2800, 2900), (2900, 3000), (3000, 3100), (3100, 100000)]
def band_label(r):
    for lo, hi in BANDS:
        if lo < r <= hi:
            return f"({lo},{hi}]"
    return "?"

df["band"] = df["rating_after"].apply(band_label)

FEATS = ["final_money", "peak_crew", "total_hires", "first_land_day", "elbow_day",
          "tiles_planted", "plants_carrot", "plants_melon", "plants_strawberry",
          "plants_tomato", "plants_wheat"]

print("\n=== (A) episode-level means by rating band ===")
order = [band_label((lo + hi) / 2) for lo, hi in BANDS]
gA = df.groupby("band")[FEATS].mean().reindex(order)
gA["n"] = df.groupby("band").size().reindex(order)
print(gA.round(2).to_string())

# crop mix as fraction of tiles_planted
for c in ["plants_carrot", "plants_melon", "plants_strawberry", "plants_tomato", "plants_wheat"]:
    df[c + "_frac"] = df[c] / df["tiles_planted"].replace(0, np.nan)
FRAC = [c + "_frac" for c in ["plants_carrot", "plants_melon", "plants_strawberry", "plants_tomato", "plants_wheat"]]
print("\n=== (A) crop-mix fractions by rating band ===")
gAf = df.groupby("band")[FRAC].mean().reindex(order)
print(gAf.round(3).to_string())

print("\n=== (A) price range (max-min) observed, by band (proxy for market activity/impact) ===")
for item in ["carrot", "melon", "strawberry", "tomato", "wheat", "wool", "milk", "egg", "fertilizer"]:
    hi, lo = f"price_{item}_max", f"price_{item}_min"
    if hi in df.columns:
        df[f"range_{item}"] = df[hi] - df[lo]
RCOLS = [c for c in df.columns if c.startswith("range_")]
gR = df.groupby("band")[RCOLS].mean().reindex(order)
print(gR.round(1).to_string())

# --- (B) submission-level ---
print("\n\n=== (B) submission-level (peak rating band, median features) ===")
sub_peak = df.groupby("submission_id")["rating_after"].max().rename("peak_rating")
sub_med = df.groupby("submission_id")[FEATS + FRAC].median()
sub_n = df.groupby("submission_id").size().rename("n_episodes")
S = sub_med.join(sub_peak).join(sub_n)
S["band"] = S["peak_rating"].apply(band_label)
gB = S.groupby("band")[FEATS].mean().reindex(order)
gB["n_submissions"] = S.groupby("band").size().reindex(order)
print(gB.round(2).to_string())

print("\n=== (B) crop-mix fractions, submission-level ===")
gBf = S.groupby("band")[FRAC].mean().reindex(order)
print(gBf.round(3).to_string())

# focus contrast: 2800-2900 vs 3000+
lo_band = "(2800,2900]"
hi_bands = ["(3000,3100]", "(3100,100000]"]
print(f"\n=== Focus: {lo_band} vs {hi_bands} (submission-level, median of medians) ===")
lo = S[S["band"] == lo_band]
hi = S[S["band"].isin(hi_bands)]
print(f"n_submissions: lo={len(lo)}, hi={len(hi)}")
for f in FEATS + FRAC:
    print(f"  {f:20s} lo={lo[f].median():10.3f}  hi={hi[f].median():10.3f}")

S.to_csv("moe/r4/build/sonnet/submission_level.csv")
df.sample(min(20000, len(df)), random_state=0).to_csv("moe/r4/build/sonnet/episode_level_sample.csv", index=False)
print("\nwrote submission_level.csv and episode_level_sample.csv")
