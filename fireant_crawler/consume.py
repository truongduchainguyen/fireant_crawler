from kafka_client import consumer

messages = []
for msg in consumer:
    print(msg.value)
    messages.append(msg.value)
    print(len(messages))
