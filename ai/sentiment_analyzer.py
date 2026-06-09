import json
from pathlib import Path

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

PROCESSED_PATH = Path(
    "data-lake/processed/news"
)

OUTPUT_PATH = Path(
    "data-lake/analytics"
)

OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)

analyzer = SentimentIntensityAnalyzer()

results = []

for file in PROCESSED_PATH.glob("*.json"):

    try:

        with open(file, "r") as f:
            article = json.load(f)

        title = article.get("title", "")
        description = article.get("description", "")

        text = f"{title} {description}"

        scores = analyzer.polarity_scores(text)

        compound = scores["compound"]

        if compound >= 0.05:
            sentiment = "positive"

        elif compound <= -0.05:
            sentiment = "negative"

        else:
            sentiment = "neutral"

        results.append({
            "keyword": article.get("keyword"),
            "title": title,
            "sentiment": sentiment,
            "compound_score": compound
        })

    except Exception as e:

        print(f"Error processing {file.name}")
        print(e)

output_file = (
    OUTPUT_PATH /
    "sentiment_results.json"
)

with open(output_file, "w") as f:

    json.dump(
        results,
        f,
        indent=4
    )

print(
    f"Processed {len(results)} articles"
)

print(
    f"Output saved to {output_file}"
)