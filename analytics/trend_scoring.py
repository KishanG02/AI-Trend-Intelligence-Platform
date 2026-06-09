import json
from collections import defaultdict

# Load sentiment results

with open(
    "data-lake/analytics/sentiment_results.json",
    "r"
) as f:
    sentiment_data = json.load(f)

keyword_stats = defaultdict(
    lambda: {
        "articles": 0,
        "sentiment_total": 0
    }
)

for article in sentiment_data:

    keyword = article["keyword"]

    keyword_stats[keyword]["articles"] += 1

    keyword_stats[keyword]["sentiment_total"] += (
        article["compound_score"]
    )

trend_scores = []

for keyword, stats in keyword_stats.items():

    article_count = stats["articles"]

    avg_sentiment = (
        stats["sentiment_total"] /
        article_count
    )

    # Volume component
    volume_score = article_count * 10

    # Sentiment component
    sentiment_score = (
        avg_sentiment + 1
    ) * 25

    trend_score = round(
        volume_score +
        sentiment_score,
        2
    )

    trend_scores.append({
        "keyword": keyword,
        "article_count": article_count,
        "avg_sentiment": round(
            avg_sentiment,
            3
        ),
        "trend_score": trend_score
    })

trend_scores.sort(
    key=lambda x: x["trend_score"],
    reverse=True
)

with open(
    "data-lake/analytics/trend_scores.json",
    "w"
) as f:

    json.dump(
        trend_scores,
        f,
        indent=4
    )

print(
    json.dumps(
        trend_scores,
        indent=4
    )
)