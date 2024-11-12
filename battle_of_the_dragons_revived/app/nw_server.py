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
mod_s3_key = "Battle Of The Dragons Revived.mod"
mod_default_location = "/home/nwserver-user/.local/share/Neverwinter Nights/modules/Battle Of The Dragons Revived.mod"

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
        subprocess.run(["sudo", "supervisord", "-c", "/etc/supervisor/supervisord.conf"])
        logger.info("Supervisor service started")
    except Exception as e:
        logger.error(f"Error starting supervisor service: {e}")

# Download nwn modules from s3 to user directory location
def download_mod_from_s3():
    try:
        # Download mod from s3
        logger.info(f"Downloading mod from s3 bucket: {mod_s3_bucket}")
        s3.download_file(mod_s3_bucket, mod_s3_key, mod_default_location)
        logger.info("Mod downloaded successfully")
    except ClientError as e:
        logger.error(f"Error downloading mod from s3: {e}")

if __name__ == "__main__":
    # Download mod from s3
    download_mod_from_s3()

    # Start supervisor
    start_supervisor()
