import logging
import os
import re
from fly.app import deploy_fly_app
from fly.deploy import deploy_fly_machine
from fly.secrets import get_fly_app_secrets, set_fly_app_secret
from fly.utils import generate_fly_io_file_obj

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# default vars
fly_api_endpoint = "https://api.machines.dev"
fly_org_slug = "Personal"
fly_api_token = os.getenv("FLY_IO_API_TOKEN")

# Get env vars
app_name = os.getenv("FLY_IO_APP_NAME")
app_env = os.getenv("TF_VAR_env")
aws_s3_mod_bucket_id = os.getenv("AWS_S3_MOD_BUCKET_ID")
aws_region = os.getenv("FLY_IO_APP_AWS_REGION")

# define files to copy to container
app_files = [
    {
        "src": "../app/nw_server.py",
        "dest": "/app/nw_server.py"
    },
    {
        "src": "../app/supervisord.conf",
        "dest": "/etc/supervisor/supervisord.conf"
    }
]

app_files_config = []

for file in app_files:
    # generate file object
    file_obj = generate_fly_io_file_obj(
        file_path=file["src"],
        guest_path=file["dest"]
    )

    # append to files config
    app_files_config.append(file_obj)

# define config values for app
app_config = {
    "image": "docker.io/library/ubuntu:22.04",
    "init": {
        "exec": [
            "/usr/bin/python3",
            "/app/nw_server.py"
        ]
    },
    "services": {
        "protocol": "udp",
        "internal_port": 5121,
        "ports": {
            "port": 5121
        },
        "autostart": True,
        "min_machines_running": 1
    },
    "mounts": [
        {
            "volume": "nwn-data",
            "path": "/nwnserver",
            "name": "nwn-data",
            "size_gb_limit": 10
        }
    ],
    "regions": [
        "iad",
        "ord"
    ],
    "auto_destroy": True,
    "env": {
        "APP_ENV": app_env
    },
    "files": app_files_config,
    "size": "shared-cpu-1x",
    "restart": {
        "policy": "never"
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
    deploy_fly_app(
        fly_api_endpoint=fly_api_endpoint,
        fly_api_token=fly_api_token,
        app_name=app_name,
        org_slug=fly_org_slug
    )

    # set secrets
    for secret in app_secrets:
        # get the secret
        secrets_output = get_fly_app_secrets(app_name=app_name)

        # regex to find secret
        secret_regex = re.compile(f"{secret['name']}=(.*)")

        # if secret does not exist, set it
        if not secret_regex.search(secrets_output):
            set_fly_app_secret(
                app_name=app_name,
                secret_name=secret["name"],
                secret_value=secret["value"]
            )

    deploy_fly_machine(
        fly_api_endpoint=fly_api_endpoint,
        fly_api_token=fly_api_token,
        app_name=app_name,
        app_config=app_config
    )

if __name__ == "__main__":
    deploy_fly_io()
