import json
import re
import glob
from collections import Counter
from itertools import combinations
from config.settings import TREND_CATEGORIES

TECH_TERMS = set()

for keywords in TREND_CATEGORIES.values():
    TECH_TERMS.update(keywords)

STOPWORDS = {
    "and",
    "the",
    "for",
    "from",
    "that",
    "this",
    "with",
    "will",
    "into",
    "are",
    "can",
    "https",
    "comments",
    "comment",
    "inc",
    "build",
    "power",
    "about",
    "their",
    "they",
    "been",
    "have",
    "has",
    "more",
    "than",
    "over",
    "after",
    "using"
}

TECH_TERMS = {
    "Artificial Intelligence",
    "OpenAI",
    "ChatGPT",
    "Claude",
    "Gemini",
    "Mistral",
    "NVIDIA",

    "AWS",
    "Azure",
    "GCP",
    "Kubernetes",
    "Docker",

    "Kafka",
    "Databricks",
    "Spark",
    "Snowflake",
    "Airflow",

    "Python",
    "LangGraph",
    "CrewAI"
}

news_files = glob.glob(
    "data-lake/raw/news/*.json"
)

all_articles = []

for file in news_files:

    try:
        with open(file) as f:
            data = json.load(f)

            if isinstance(data, list):
                all_articles.extend(data)

            elif isinstance(data, dict):
                all_articles.append(data)

    except Exception:
        pass

print(
    f"Loaded {len(all_articles)} articles"
)

phrase_counter = Counter()

for article in all_articles:

    title = article.get("title", "")
    description = article.get("description", "")

    text = f"{title} {description}"

    found_terms = []

    for term in TECH_TERMS:

        if term.lower() in text.lower():
            found_terms.append(term)

    for pair in combinations(
        sorted(found_terms),
        2
    ):

        phrase_counter[
            f"{pair[0]} + {pair[1]}"
        ] += 1

top_keywords = phrase_counter.most_common(50)

output = []

for keyword, count in top_keywords:

    output.append(
        {
            "keyword": keyword,
            "count": count
        }
    )

with open(
    "data-lake/analytics/discovered_keywords.json",
    "w"
) as f:

    json.dump(
        output,
        f,
        indent=4
    )

print(
    f"Saved {len(output)} keywords"
)