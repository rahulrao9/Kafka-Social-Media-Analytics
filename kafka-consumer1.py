#!/usr/bin/env python3

from kafka import KafkaConsumer
import json
import sys

# Specify the topic as a command-line argument
topic_name = sys.argv[1]

# Define the Kafka consumer settings
consumer_settings = {
    'bootstrap_servers': 'localhost:9092',  # Address of the Kafka broker(s)
    'group_id': 'comments',  # Specify a unique group ID for the consumer
    'auto_offset_reset': 'latest',  # Start consuming from the earliest available offset
    'enable_auto_commit': True,  # Automatically commit offsets
    'key_deserializer': None,  # Deserializer for message keys
    'value_deserializer': lambda x: json.loads(x.decode('utf-8'))  # JSON deserializer for message values
}

# Create a KafkaConsumer instance with the specified settings
consumer = KafkaConsumer(topic_name, **consumer_settings)

# Loop to consume messages
comments = {}
for message in consumer:

    data = message.value  # The message value is already deserialized

    # Check if the message is of type 'comment'
    if data['type'] == 'comment':
        user_who_posted = data['user_who_posted']
        comment = data['comment']

        # Append the comment to the respective user
        if user_who_posted not in comments:
            comments[user_who_posted] = []
        comments[user_who_posted].append(comment)
        
    if data["type"] == "EOF":
    	break
    	
sorted_comments = {user: comments[user] for user in sorted(comments)}
print(json.dumps(sorted_comments, indent=4, sort_keys=True))

