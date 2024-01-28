#!/usr/bin/env python3
import sys
from kafka import KafkaProducer
import json
#Kafka server and topic names
topics = sys.argv[1:]

# lets define a function to push the message according to the topics
def to_producer(producer, topic, message):
    producer.flush()
    producer.send(topic, value=json.dumps(message).encode('utf-8'))

#initiate the producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for line in sys.stdin:
	line = line.strip()
	
	if line == 'EOF':
		message = {"type": "EOF"}
		to_producer(producer, topics[0], message)
		to_producer(producer, topics[1], message)
		to_producer(producer, topics[2], message)
		break

	message = {}
	line = line.split()
	if line[0]=='comment':
		message['type'] = 'comment'
		message["user_who_posted"] = line[2]
		message['comment'] = line[4:]
		message['comment'][0] = message['comment'][0].lstrip('"')
		message['comment'][len(message['comment'])-1] = message['comment'][len(message['comment'])-1].rstrip('"')
		message['comment'] = " ".join(message['comment']) 
		topics_send = [topics[0],topics[2]]
	elif line[0] == 'like':
		message['type'] = 'like'
		message["user_who_posted"] = line[2]
		message['post_id'] = int(line[3])
		topics_send = [topics[1],topics[2]]
	elif line[0] == 'share':
                message['type'] = 'share'
                message["user_who_posted"] = line[2]
                message['shared_to'] = line[4:]
                topics_send = [topics[2]]

	
	if len(topics_send) == 2:
		to_producer(producer, topics_send[0], message)
		to_producer(producer, topics_send[1], message)
	elif len(topics_send) == 1:
		to_producer(producer, topics_send[0], message)

print("sorted_comments")
producer.flush()
producer.close()


