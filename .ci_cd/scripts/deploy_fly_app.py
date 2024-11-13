import logging
import os
from fly.app import deploy_fly_app
from fly.deploy import deploy_fly_machine
from fly.secrets import set_fly_app_secret
from fly.utils import generate_fly_io_file_obj

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# default vars
fly_api_endpoint = "https://api.machines.dev"
fly_api_token = os.getenv("FLY_IO_API_TOKEN")

# Get env vars
app_name = os.getenv("FLY_IO_APP_NAME")
app_env = os.getenv("FLY_IO_APP_ENV")

# define files to copy to container
app_files = [
    {
        "src": "app/nw_server.py",
        "dest": "/app/nw_server.py"
    },
    {
        "src": "app/supervisord.conf",
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

def deploy_fly_io():
    deploy_fly_app(
        fly_api_endpoint=fly_api_endpoint,
        fly_api_token=fly_api_token,
        app_name=app_name
    )

    deploy_fly_machine(
        fly_api_endpoint=fly_api_endpoint,
        fly_api_token=fly_api_token,
        app_name=app_name,
        app_config=app_config
    )
