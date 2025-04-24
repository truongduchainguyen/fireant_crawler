from kafka_client import consumer

for msg in consumer:
    print(msg)
