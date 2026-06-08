from kafka import KafkaProducer
import json
import time

from config.settings import KAFKA_BROKER
from config.settings import KAFKA_TOPIC

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

for i in range(10):

    message = {
        "source": "test",
        "text": f"Message {i}"
    }

    producer.send(KAFKA_TOPIC, message)

    print("Sent:", message)

    time.sleep(1)

producer.flush()