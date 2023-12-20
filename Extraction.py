import boto3
import os


aws_access_key_id = 'AK2STSDQYRMWAHOIC'
aws_secret_access_key = 'WLbsU6nqfXpDs2EZBEJ4bKZ0aimpV2Fdl3P9'
region_name = 'us-east-1'


s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)


bucket_name = 'dcsc-raw-data'

# Mapping of file prefixes to S3 directories
file_prefixes = {
    'CA': 'youtube/raw_statistics/region=ca/',
    'DE': 'youtube/raw_statistics/region=de/',
    'FR': 'youtube/raw_statistics/region=fr/',
    'GB': 'youtube/raw_statistics/region=gb/',
    'IN': 'youtube/raw_statistics/region=in/',
    'JP': 'youtube/raw_statistics/region=jp/',
    'KR': 'youtube/raw_statistics/region=kr/',
    'MX': 'youtube/raw_statistics/region=mx/',
    'RU': 'youtube/raw_statistics/region=ru/',
    'US': 'youtube/raw_statistics/region=us/'
}

# Local directory path with 'downloads' included
local_directory = 'Downloads/DCSC_Project/Data'

# List all files in the local directory
for root, dirs, files in os.walk(local_directory):
    for file in files:
        local_path = os.path.join(root, file)
        
        # Upload JSON files to respective directories
        if file.endswith('.json'):
            s3_directory = 'youtube/raw_statistics_reference_data/'
            s3_path = s3_directory + os.path.relpath(local_path, local_directory).replace("\\", "/")
            s3.upload_file(local_path, bucket_name, s3_path)
            print(f"Uploaded {local_path} to S3 bucket {bucket_name} at {s3_path}")
        
        # Upload CSV files to respective directories
        elif file.endswith('.csv'):
            file_prefix = file[:2]  # Extract the first two characters as the prefix
            if file_prefix in file_prefixes:
                s3_directory = file_prefixes[file_prefix]
                s3_path = s3_directory + file
                s3.upload_file(local_path, bucket_name, s3_path)
                print(f"Uploaded {local_path} to S3 bucket {bucket_name} at {s3_path}")
