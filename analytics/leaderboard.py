import json

with open(
    "data-lake/analytics/trend_scores.json",
    "r"
) as f:

    data = json.load(f)

leaderboard = []

for rank, item in enumerate(
    data,
    start=1
):

    leaderboard.append({
        "rank": rank,
        "keyword": item["keyword"],
        "trend_score": item["trend_score"]
    })

with open(
    "data-lake/analytics/trending_keywords.json",
    "w"
) as f:

    json.dump(
        leaderboard,
        f,
        indent=4
    )

print(
    json.dumps(
        leaderboard,
        indent=4
    )
)