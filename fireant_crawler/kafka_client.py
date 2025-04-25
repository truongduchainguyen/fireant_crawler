from kafka import KafkaAdminClient, KafkaProducer, KafkaConsumer


producer = KafkaProducer(
    bootstrap_servers="localhost:9092,localhost:9093"
)

consumer = KafkaConsumer("testing")
