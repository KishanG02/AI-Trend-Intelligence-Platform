import json
import os
from datetime import datetime

from googleapiclient.discovery import build
from kafka import KafkaProducer

from config.env_loader import *
from config.settings import (
    KAFKA_BROKER,
    YOUTUBE_TOPIC,
    KEYWORDS
)

YOUTUBE_API_KEY = os.getenv(
    "YOUTUBE_API_KEY"
)

youtube = build(
    "youtube",
    "v3",
    developerKey=YOUTUBE_API_KEY
)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v:
    json.dumps(v).encode("utf-8")
)


for keyword in KEYWORDS:

    request = youtube.search().list(
        q=keyword,
        part="snippet",
        maxResults=5,
        type="video"
    )

    response = request.execute()

    for item in response.get("items", []):

        try:

            video_id = (
                item
                .get("id", {})
                .get("videoId")
            )

            if not video_id:
                continue

            record = {
                "keyword": keyword,
                "video_id": video_id,
                "title":
                    item["snippet"]["title"],
                "channel":
                    item["snippet"]["channelTitle"],
                "published_at":
                    item["snippet"]["publishedAt"]
            }

            producer.send(
                YOUTUBE_TOPIC,
                value=record
            )

            print(
                f"Sent: {record['title']}"
            )

        except Exception as e:

            print(
                f"Skipping record: {e}"
            )

producer.flush()

print(
    "\nYouTube ingestion completed."
)