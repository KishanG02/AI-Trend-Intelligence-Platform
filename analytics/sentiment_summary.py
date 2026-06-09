import json
from collections import Counter

with open(
    "data-lake/analytics/sentiment_results.json",
    "r"
) as f:

    data = json.load(f)

counter = Counter()

for item in data:

    counter[item["sentiment"]] += 1

summary = {
    "total_articles": len(data),
    "positive": counter["positive"],
    "neutral": counter["neutral"],
    "negative": counter["negative"]
}

with open(
    "data-lake/analytics/sentiment_summary.json",
    "w"
) as f:

    json.dump(
        summary,
        f,
        indent=4
    )

print(summary)
