import subprocess
import os
import logging
import boto3
from botocore.exceptions import ClientError

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Get env vars
aws_region = os.getenv("AWS_REGION")
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
mod_s3_bucket = os.getenv("AWS_S3_MOD_BUCKET_ID")

# Set up s3 client
s3 = boto3.client(
    "s3",
    region_name=aws_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

# function to start supervisor
def start_supervisor():
    try:
        # Start the supervisor service
        logger.info("Starting supervisor service...")
        subprocess.run(["supervisord", "-c", "/etc/supervisor/supervisord.conf"])
        logger.info("Supervisor service started")
    except Exception as e:
        logger.error(f"Error starting supervisor service: {e}")

# Test s3 connection
def test_s3_connection():
    try:
        # Test s3 connection
        logger.info("Testing s3 connection...")
        s3.list_buckets()
        logger.info("S3 connection successful")
    except ClientError as e:
        logger.error(f"Error testing s3 connection: {e}")

if __name__ == "__main__":
    # Test s3 connection
    test_s3_connection()
