import json
from pathlib import Path

ANALYTICS_PATH = Path(
"data-lake/analytics"
)

# -----------------------------

# Load News Trends

# -----------------------------

with open(
ANALYTICS_PATH / "trend_scores.json"
) as f:

    news_trends = json.load(f)


# -----------------------------

# Load YouTube Trends

# -----------------------------

with open(
ANALYTICS_PATH
/ "youtube"
/ "youtube_trends.json"
) as f:

    youtube_trends = json.load(f)

youtube_lookup = {
row["keyword"]: row["video_count"]
for row in youtube_trends
}

# -----------------------------

# Unified Score

# -----------------------------

results = []

for item in news_trends:

    keyword = item["keyword"]

    news_score = item["trend_score"]

    youtube_score = (
        youtube_lookup.get(
            keyword,
            0
        ) * 5
    )

    final_score = round(
        news_score +
        youtube_score,
        2
    )

    results.append({
        "keyword": keyword,
        "news_score":
            news_score,
        "youtube_score":
            youtube_score,
        "final_score":
            final_score
    })


results = sorted(
results,
key=lambda x:
x["final_score"],
reverse=True
)

# -----------------------------

# Save

# -----------------------------

with open(
ANALYTICS_PATH
/ "unified_trend_scores.json",
"w"
) as f:

    json.dump(
        results,
        f,
        indent=4
    )

print(
"Unified trend scores generated"
)