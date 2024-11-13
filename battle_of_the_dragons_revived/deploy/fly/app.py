import logging
import json
import requests
from requests.exceptions import RequestException

# Set up logging
logger = logging.getLogger()

# Function to deploy Fly.io app
def deploy_fly_app(
    fly_api_endpoint: str,
    fly_api_token: str,
    app_name: str,
    org_slug: str,
    network: str = None  # Optional network parameter
):
    logger.info("Deploying app: %s", app_name)
    # Define API URL and headers
    url = f"{fly_api_endpoint}/v1/apps"  # Ensure the endpoint path is correct
    headers = {
        "Authorization": f"Bearer {fly_api_token}",
        "Content-Type": "application/json",
    }

    # Check if the app exists
    fly_app = None
    try:
        fly_app_response = requests.get(f"{url}/{app_name}", headers=headers, timeout=10)
        fly_app_response.raise_for_status()  # Raises HTTPError for bad responses
        logger.info("App response: %s", fly_app_response)
        if fly_app_response.status_code == 200:
            fly_app = fly_app_response.json()
            logger.info("App exists: %s", fly_app)
    except RequestException as e:
        if fly_app_response and fly_app_response.status_code == 404:
            logger.info("App does not exist")
        else:
            logger.error("Error getting app: %s", e)
            return

    # If the app does not exist, create it
    if fly_app is None:
        logger.info("Creating app: %s", app_name)
        # Construct the request body
        create_app_payload = {
            "app_name": app_name,
            "org_slug": org_slug
        }
        if network:
            create_app_payload["network"] = network

        try:
            fly_create_app_response = requests.post(
                url,
                headers=headers,
                json=create_app_payload,
                timeout=10,
            )
            fly_create_app_response.raise_for_status()  # Ensure exception is raised for errors
            fly_create_app = fly_create_app_response.json()
            logger.info("App created successfully: %s", fly_create_app)
            fly_app = fly_create_app
        except RequestException as e:
            logger.error("Error creating app: %s", e)
            return

    # Return app id
    logger.info("App id: %s", fly_app["id"])
    return fly_app["id"]
