from kafka import KafkaConsumer
import json

from config.settings import KAFKA_BROKER
from config.settings import KAFKA_TOPIC

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Listening...")

for msg in consumer:
    print(msg.value)