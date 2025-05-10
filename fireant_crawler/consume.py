from kafka_client import consumer
import json
import datetime

messages = []
obj = {}
now = datetime.datetime.now()
prefix = datetime_string = now.strftime("%Y-%m-%d_%H:%M:%S")

for message in consumer:
    obj["message"] = message.value
    obj["sentiment"] = ""
    print(obj)
    messages.append(obj)
    if len(messages) == 30:
        with open(f"{prefix}_message.json", "w+") as output:
            json.dump(messages, output, indent=4)
        messages = []

