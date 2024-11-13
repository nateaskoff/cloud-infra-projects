import logging
import json
import requests
from requests.exceptions import HTTPError

# Set up logging
logger = logging.getLogger()

# Function to deploy fly app
def deploy_fly_app(
    fly_api_endpoint: str,
    fly_api_token: str,
    app_name: str
    ):
    logger.info("Deploying app: %s", app_name)
    # define api url and headers
    url = f"{fly_api_endpoint}/api/v1/apps"
    headers = {
        "Authorization": f"Bearer {fly_api_token}",
        "Content-Type": "application/json",
    }

    # see if app exists
    fly_app = None
    try:
        fly_app_response = requests.get(f"{url}/{app_name}", headers=headers, timeout=10)
        logger.info("App response: %s", fly_app_response)
    except HTTPError as e:
        if e.response.status_code == 404:
            logger.info("App does not exist")
        else:
            logger.error("Error getting app: %s", e)
            return

    if fly_app_response.status_code == 200:
        fly_app = json.loads(fly_app_response.content)
        logger.info("App exists: %s", fly_app)

    # if does not exist, create app
    if fly_app is None:
        logger.info("Creating app: %s", app_name)
        try:
            fly_create_app_response = requests.post(
                url,
                headers=headers,
                json={"name": app_name},
                timeout=10,
            )
            fly_create_app_response.raise_for_status()
            logger.info("App created successfully: %s", fly_create_app_response)
            fly_create_app = json.loads(fly_create_app_response.content)
            logger.info("App created successfully")
        except HTTPError as e:
            logger.error("Error creating app: %s", e)
            return

        # get app id
        fly_app = fly_create_app

    # return app id
    logger.info("App id: %s", fly_app["id"])
    return fly_app["id"]
