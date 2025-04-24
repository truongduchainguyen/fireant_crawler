from kafka import KafkaProducer, KafkaConsumer


producer = KafkaProducer(
    bootstrap_servers="localhost:9092"
)

consumer = KafkaConsumer("testing")
