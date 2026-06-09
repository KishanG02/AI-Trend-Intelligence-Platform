import json
from pathlib import Path
from collections import Counter, defaultdict

RAW_PATH = Path(
"data-lake/raw/youtube"
)

OUTPUT_PATH = Path(
"data-lake/analytics/youtube"
)

OUTPUT_PATH.mkdir(
parents=True,
exist_ok=True
)

video_count_by_keyword = Counter()
channel_count = Counter()

keyword_channels = defaultdict(set)

total_videos = 0

for file in RAW_PATH.glob("*.json"):

    with open(file) as f:

        record = json.load(f)

    keyword = record["keyword"]
    channel = record["channel"]

    total_videos += 1

    video_count_by_keyword[keyword] += 1

    channel_count[channel] += 1

    keyword_channels[keyword].add(channel)

# ------------------------------------

# Summary

# ------------------------------------

summary = {
"total_videos": total_videos,
"unique_keywords":
len(video_count_by_keyword),
"unique_channels":
len(channel_count)
}

with open(
OUTPUT_PATH / "youtube_summary.json",
"w"
) as f:

    json.dump(
        summary,
        f,
        indent=4
    )


# ------------------------------------

# Trends

# ------------------------------------

trends = []

for keyword, count in sorted(
video_count_by_keyword.items(),
key=lambda x: x[1],
reverse=True
):

    trends.append({
        "keyword": keyword,
        "video_count": count,
        "unique_channels":
            len(keyword_channels[keyword])
    })


with open(
OUTPUT_PATH / "youtube_trends.json",
"w"
) as f:

    json.dump(
        trends,
        f,
        indent=4
    )

# ------------------------------------

# Top Channels

# ------------------------------------

top_channels = []

for channel, count in channel_count.most_common(20):

    top_channels.append({
        "channel": channel,
        "video_count": count
    })


with open(
OUTPUT_PATH / "top_channels.json",
"w"
) as f:

    json.dump(
        top_channels,
        f,
        indent=4
    )


print(
f"Processed {total_videos} videos"
)

print(
"Analytics generated successfully"
)
