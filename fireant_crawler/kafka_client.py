from kafka import KafkaAdminClient, KafkaProducer, KafkaConsumer
import json


producer = KafkaProducer(
    bootstrap_servers="localhost:9092,localhost:9093",
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)


consumer = KafkaConsumer(
    "testing",
    bootstrap_servers="localhost:9092,localhost:9093",
    auto_offset_reset='earliest', # Start reading from the beginning of the topic
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8')) # Deserialize message values from JSON
)
