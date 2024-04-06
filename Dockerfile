FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org boto3

CMD ["python", "./s3_to_rds.py"]
