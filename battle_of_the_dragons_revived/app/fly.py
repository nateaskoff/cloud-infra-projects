import os
import logging
import asyncio
from fly_python_sdk.fly import Fly

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# get env vars
fly_api_token = os.getenv('FLY_IO_API_TOKEN')
app_name = os.getenv('FLY_IO_APP_NAME')
app_region = os.getenv('FLY_IO_APP_REGION', 'iad')
app_org = os.getenv('FLY_IO_ORG')
app_port = os.getenv('FLY_IO_PORT', 5121)
app_kill_signal = os.getenv('FLY_IO_KILL_SIGNAL', 'SIGTERM')
app_kill_timeout = os.getenv('FLY_IO_KILL_TIMEOUT', 300)
fly_cpus = os.getenv('FLY_IO_CPUS', 0.25)
fly_memory = os.getenv('FLY_IO_MEMORY', 128)
dockerfile_path = os.getenv('FLY_IO_DOCKERFILE_PATH', 'Dockerfile')
app_volumes = os.getenv('FLY_IO_VOLUMES', [])

# create a Fly instance
fly = Fly(fly_api_token)

# list apps to see if the app already exists
fly_apps = asyncio.run(fly.Org(app_org).list_apps())

# if the app doesn't exist, create it, otherwise deploy a new version
if app_name not in fly_apps:
    logger.info(f'Creating app {app_name}')
    app = asyncio.run(fly.Org(app_org).create_app(
        app_name=app_name,
        region=app_region,
        port=app_port,
        cpus=fly_cpus,
        memory=fly_memory,
        kill_signal=app_kill_signal,
        kill_timeout=app_kill_timeout,
        dockerfile_path=dockerfile_path,
        volumes=app_volumes
    ))
    logger.info(f'App {app_name} created')
else:
    logger.info(f'App {app_name} already exists')
    app = asyncio.run(fly.Org(app_org).get_app(app_name))

    # deploy the app
    logger.info(f'Deploying app {app_name}')
    deploy = asyncio.run(app.deploy())
    logger.info(f'App {app_name} deployed')
    logger.info(f'Deployment: {deploy}')
