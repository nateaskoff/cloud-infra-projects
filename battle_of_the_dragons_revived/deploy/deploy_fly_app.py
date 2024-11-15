import logging
import os
from fly.app import deploy_fly_app
from fly.deploy import deploy_fly_machine
from fly.secrets import get_fly_app_secrets, set_fly_app_secret
from fly.utils import generate_fly_io_file_obj

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Default variables
fly_api_endpoint = "https://api.machines.dev"
fly_org_slug = "Personal"
fly_api_token = os.getenv("FLY_IO_API_TOKEN")

# Get environment variables
app_name = os.getenv("FLY_IO_APP_NAME")
app_env = os.getenv("TF_VAR_env")
aws_s3_mod_bucket_id = os.getenv("AWS_S3_MOD_BUCKET_ID")
aws_region = os.getenv("FLY_IO_APP_AWS_REGION")

# Define config values for the app
app_config = {
    "config": {
        "image": "docker.io/library/ubuntu:22.04",
        "init": {
            "exec": [
                "python3",
                "/app/nw_server.py"
            ]
        },
        "services": [
            {
                "protocol": "udp",
                "internal_port": 5121,
                "ports": [
                    {
                        "port": 5121,
                        "handlers": [
                            "http"
                        ]
                    }
                ],
                "autostart": True,
                "min_machines_running": 1
            }
        ],
        #"mounts": [
        #    {
        #        "volume": "nwn-data",
        #        "path": "/nwnserver",
        #        "name": "nwn-data",
        #        "size_gb_limit": 10
        #    }
        #],
        "regions": [
            "iad",
            "ord"
        ],
        "auto_destroy": True,
        "env": {
            "APP_ENV": app_env
        },
        "size": "shared-cpu-1x",
        "restart": {
            "policy": "no"
        }
    }
}

app_secrets = [
    {
        "name": "AWS_ACCESS_KEY_ID",
        "value": os.getenv("AWS_ACCESS_KEY_ID")
    },
    {
        "name": "AWS_SECRET_ACCESS_KEY",
        "value": os.getenv("AWS_SECRET_ACCESS_KEY")
    }
]

def deploy_fly_io():
    # Deploy the app
    deploy_fly_app(
        fly_api_endpoint=fly_api_endpoint,
        fly_api_token=fly_api_token,
        app_name=app_name,
        org_slug=fly_org_slug
    )

    # Retrieve existing secrets
    existing_secrets = get_fly_app_secrets(app_name=app_name)
    existing_secret_names = {secret["Name"] for secret in existing_secrets}

    # Set secrets if they don't already exist
    for secret in app_secrets:
        if secret["name"] in existing_secret_names:
            logger.info(f"Secret '{secret['name']}' already exists")
        else:
            set_fly_app_secret(
                app_name=app_name,
                secret_name=secret["name"],
                secret_value=secret["value"]
            )

    # Deploy the Fly.io machine
    deploy_fly_machine(
        fly_api_endpoint=fly_api_endpoint,
        fly_api_token=fly_api_token,
        app_name=app_name,
        app_config=app_config
    )

if __name__ == "__main__":
    deploy_fly_io()
