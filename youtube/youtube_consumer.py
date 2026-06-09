import json
from pathlib import Path

from kafka import KafkaConsumer

from config.settings import (
KAFKA_BROKER,
YOUTUBE_TOPIC
)

RAW_PATH = Path(
"data-lake/raw/youtube"
)

RAW_PATH.mkdir(
parents=True,
exist_ok=True
)

consumer = KafkaConsumer(
YOUTUBE_TOPIC,
bootstrap_servers=KAFKA_BROKER,
auto_offset_reset="earliest",
value_deserializer=lambda m:
json.loads(m.decode("utf-8"))
)

print(
"Listening for YouTube records..."
)

for message in consumer:

    record = message.value

    file_name = (
        f"{record['video_id']}.json"
    )

    output_file = (
        RAW_PATH / file_name
    )

    with open(
        output_file,
        "w"
    ) as f:

        json.dump(
            record,
            f,
            indent=4
        )

    print(
        f"Saved: {file_name}"
    )