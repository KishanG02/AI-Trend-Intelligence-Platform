import json
from pathlib import Path
from datetime import datetime

import pandas as pd

# ====================================
# Paths
# ====================================

ANALYTICS_PATH = Path("data-lake/analytics")

TREND_FILE = (
    ANALYTICS_PATH /
    "unified_trend_scores.json"
)

HISTORY_FILE = (
    ANALYTICS_PATH /
    "trend_history.csv"
)

# ====================================
# Load trend scores
# ====================================

with open(TREND_FILE) as f:
    trend_scores = json.load(f)

# ====================================
# Create records
# ====================================

today = datetime.now().strftime(
    "%Y-%m-%d"
)

rows = []

for item in trend_scores:

    rows.append({
        "date": today,
        "keyword": item["keyword"],
        "news_score": item["news_score"],
        "youtube_score": item["youtube_score"],
        "final_score": item["final_score"]
    })

new_df = pd.DataFrame(rows)

# ====================================
# Append history
# ====================================

if HISTORY_FILE.exists():

    history_df = pd.read_csv(
        HISTORY_FILE
    )

    history_df = pd.concat(
        [history_df, new_df],
        ignore_index=True
    )

else:

    history_df = new_df

history_df.to_csv(
    HISTORY_FILE,
    index=False
)

print(
    f"Saved {len(rows)} trend records."
)