#!/usr/bin/env python3
from kafka import KafkaConsumer
from kafka import TopicPartition
import json
import sys
topic_name = sys.argv[3]

# Define the Kafka consumer settings
consumer_settings = {
    'bootstrap_servers': 'localhost:9092',  # Address of the Kafka broker(s)
    'group_id': 'popularity',  # Specify a unique group ID for the consumer
    'auto_offset_reset': 'latest',  # Start consuming from the earliest available offset
    'enable_auto_commit': True,  # Automatically commit offsets
    'key_deserializer': None,  # Deserializer for message keys
    'value_deserializer': lambda x: json.loads(x.decode('utf-8'))  # JSON deserializer for message values
}

# Create a KafkaConsumer instance with the specified settings
consumer = KafkaConsumer(topic_name, **consumer_settings)

popularity = {}

for message in consumer:
    data = message.value

    #Check if the message is a valid
    if data['type'] in ['like', 'share', 'comment']:
        user = data['user_who_posted']

        likes = 1 if data['type'] == 'like' else 0
        shares = len(data.get('shared_to', [])) if data['type'] == 'share' else 0
        comments = 1 if data['type'] == 'comment' else 0

        popularity[user] = round(float(popularity.get(user, 0)) + ((likes + (20 * shares) + (5 * comments)) / 1000), 3)

        
    if data["type"] == "EOF":
    	break
    	
sorted_popularity = {user: popularity[user] for user in sorted(popularity)}
print(json.dumps(sorted_popularity, indent=4, sort_keys=True))

