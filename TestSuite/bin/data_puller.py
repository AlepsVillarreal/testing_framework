"""
Script to extract data from different origins

Features
1. Extract the desired tables of SQL Server
2. Extract the desired information from an S3 Bucket
3. Extract the data from snowflake
"""
import logging
import boto3
from botocore.exceptions import ClientError

def download_files(bucket_name, object_name, file_name):
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, object_name, file_name)

# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')