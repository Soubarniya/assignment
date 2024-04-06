import boto3
import pandas as pd
from sqlalchemy import create_engine

# AWS credentials
AWS_REGION = "ap-south-1"
AWS_ACCESS_KEY_ID = "access_key_id"
AWS_SECRET_ACCESS_KEY = "secret_access_key"

# RDS credentials
RDS_HOSTNAME = "postgres"
RDS_DB_NAME = "database-1"
RDS_USERNAME = "postgres"
RDS_PASSWORD = "admin123"

# Create S3 client
s3_client = boto3.client('s3', region_name=AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Read data from S3
def read_data_from_s3(bucket_name, file_name):
    obj = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    df = pd.read_csv(obj['Body'])
    return df

# Push data to RDS
def push_data_to_rds(df):
    engine = create_engine(f"postgresql://{RDS_USERNAME}:{RDS_PASSWORD}@{RDS_HOSTNAME}/{RDS_DB_NAME}")
    df.to_sql('data', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    bucket_name = "gotechnologies"
    file_name = "data.csv"
    df = read_data_from_s3(bucket_name, file_name)
    push_data_to_rds(df)
