from kafka_client import producer


while True:
    producer.send("testing", b"lmao")
    producer.flush()
