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
* student_dataset.txt: Sample input dataset for testing.

## How to Run
1. Start Kafka server.
2. Create three Kafka topics (replace topicName1, topicName2, topicName3 with actual topic names):


[Apache Kafka.js]: https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka
[kafka-url]: https://kafka.apache.org/
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/pranav-ambig/YADLTS/blob/main/MIT-LICENSE.txt
[Python.js]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[Ubuntu.js]: https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white
[Ubuntu-url]: https://ubuntu.com/
