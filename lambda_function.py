import boto3
import pandas as pd
from sqlalchemy import create_engine

# AWS credentials
AWS_REGION = "ap-south-1"
AWS_ACCESS_KEY_ID = "your_access_key_id"
AWS_SECRET_ACCESS_KEY = "your_secret_access_key"

# RDS credentials
RDS_HOSTNAME = "postgres"
RDS_DB_NAME = "database-1"
RDS_USERNAME = "postgres"
RDS_PASSWORD = "admin-1"

def lambda_handler(event, context):
    s3_client = boto3.client('s3', region_name=AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    
    bucket_name = "gotechnologies"
    file_name = "data.csv"
    obj = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    df = pd.read_csv(obj['Body'])
    
    engine = create_engine(f"postgresql://{RDS_USERNAME}:{RDS_PASSWORD}@{RDS_HOSTNAME}/{RDS_DB_NAME}")
    df.to_sql('your_table_name', engine, if_exists='replace', index=False)
    
    return {
        'statusCode': 200,
        'body': 'Data pushed to RDS successfully'
    }
