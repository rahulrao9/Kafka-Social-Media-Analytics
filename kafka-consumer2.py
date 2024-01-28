#!/usr/bin/env python3
from kafka import KafkaConsumer
from kafka import TopicPartition
import json
import sys
topic_name = sys.argv[2]

# Define the Kafka consumer settings
consumer_settings = {
    'bootstrap_servers': 'localhost:9092',  # Address of the Kafka broker(s)
    'group_id': 'likes',  # Specify a unique group ID for the consumer
    'auto_offset_reset': 'latest',  # Start consuming from the earliest available offset
    'enable_auto_commit': True,  # Automatically commit offsets
    'key_deserializer': None,  # Deserializer for message keys
    'value_deserializer': lambda x: json.loads(x.decode('utf-8'))  # JSON deserializer for message values
}

# Create a KafkaConsumer instance with the specified settings
consumer = KafkaConsumer(topic_name, **consumer_settings)

likes = {}

for message in consumer:
    data = message.value

    if data['type'] == 'like':
        user_who_posted = data['user_who_posted']
        post_id = data['post_id']

        if user_who_posted not in likes:
            likes[user_who_posted] = {}
        likes[user_who_posted][str(post_id)] = likes[user_who_posted].get(str(post_id), 0) + 1
        
    if data["type"] == "EOF":
    	break
    	
sorted_likes = {user: likes[user] for user in sorted(likes)}
print(json.dumps(sorted_likes, indent=4, sort_keys=False))
    	
    	

