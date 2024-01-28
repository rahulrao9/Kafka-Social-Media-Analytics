# Kafka-Social-Media-Analytics
[![MIT License][license-shield]][license-url]
## Overview
This project involves using Kafka's producer and consumer APIs to analyze a social media dataset and generate output files for three different clients. The dataset consists of user actions such as likes, shares, and comments on posts.

## Requirements
[![Apache Kafka][Apache Kafka.js]][kafka-url]
[![Python][Python.js]][Python-url]
[![Ubuntu][Ubuntu.js]][Ubuntu-url]
* Python 3.x
* Kafka-Python library

## Project Structure
* kafka-producer.py: Python script for producing social media dataset to Kafka topics.
* kafka-consumer1.py: Consumer script for Client 1 - Comments on posts.
* kafka-consumer2.py: Consumer script for Client 2 - Number of likes on posts.
* kafka-consumer3.py: Consumer script for Client 3 - User popularity calculation.

## How to Run
1. Start Kafka server.
2. Create three Kafka topics (replace topicName1, topicName2, topicName3 with actual topic names):
```bash
kafka-topics.sh --create --topic topicName1 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
kafka-topics.sh --create --topic topicName2 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
kafka-topics.sh --create --topic topicName3 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
3. Run consumers in separate terminals:
```bash
python3 kafka-consumer1.py topicName1 topicName2 topicName3 > output1.json
python3 kafka-consumer2.py topicName1 topicName2 topicName3 > output2.json
python3 kafka-consumer3.py topicName1 topicName2 topicName3 > output3.json
```
4. Run the producer in a separate terminal:
```bash
cat dataset.txt | python3 kafka-producer.py topicName1 topicName2 topicName3
```

## Client Specific Outputs
* Client 1
List down all the comments received on posts for all users.

```sh
{
    "@username1" : [
        "comment1",
        "comment2"
    ],
    "@username2" : [
        "comment1",
        "comment2"
    ],
    ...
}
```
* Client 2
List down the number of likes received on different posts for each user.
```sh
{
    "@username1" : {
        "post-id-1" : no_of_likes,
        "post-id-2" : no_of_likes
    },
    ...
}
```
* Client 3
Calculate the popularity of a user based on the number of likes, shares, and comments on the user’s profile.
```sh
{
    "@username_1": popularity,
    "@username_2": popularity,
    ...
}
```
[Apache Kafka.js]: https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka
[kafka-url]: https://kafka.apache.org/
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/rahulrao9/Kafka-Social-Media-Analytics/blob/main/LICENSE
[Python.js]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[Ubuntu.js]: https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white
[Ubuntu-url]: https://ubuntu.com/
