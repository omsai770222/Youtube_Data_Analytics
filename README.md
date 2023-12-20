# Youtube_Data_Analytics

## Project Overview

The goal of this project is to effectively manage, streamline, and analyze structured and semi-structured YouTube video data. This involves categorizing videos and analyzing trending metrics in a secure and efficient manner.

## Objectives
1. Data Ingestion: Develop a robust mechanism to collect data from diverse sources.
2. ETL System: Transform raw data into a structured format suitable for analysis.
3. Data Lake: Establish a centralized repository to store data collected from multiple sources.
4. Scalability: Ensure that our system scales seamlessly as the volume of data grows.
5. Cloud Integration: Leverage cloud services (specifically AWS) for processing vast amounts of data efficiently.
7. Reporting: Create a dashboard to derive insights and answer analytical questions.

## Services Utilized
1. Amazon S3: Object storage service offering scalability, data availability, security, and high performance.
2. AWS IAM: Identity and Access Management for secure management of access to AWS services and resources.
3. Amazon QuickSight: Serverless, scalable, machine learning-powered BI service designed for cloud-based analytics.
4. AWS Glue: Serverless data integration service facilitating data discovery, preparation, and aggregation for analytics and machine learning.
5. AWS Lambda: Serverless computing service enabling code execution without server management.
6. AWS Athena: Interactive query service for S3, allowing querying of data directly without the need for data loading.

## Architecture

![image](https://github.com/omsai770222/Youtube_Data_Analytics/assets/67456061/6abbe4a4-1dae-42d9-bb3f-82eed149a36a)


## Data
The dataset sourced from Kaggle contains daily statistics in CSV format for popular YouTube videos spanning multiple months. Each day may have up to 200 trending videos per location, with each region having its data file. Information includes video titles, channel titles, publication times, tags, views, likes, dislikes, descriptions, comment 
counts, and region-specific category IDs in linked JSON files.

[Dataset Link](https://www.kaggle.com/datasets/datasnaek/youtube-new)

