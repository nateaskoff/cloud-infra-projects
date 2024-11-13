import logging
import json
import requests
from requests.exceptions import RequestException

# Set up logging
logger = logging.getLogger()

# Function to deploy Fly.io machine
def deploy_fly_machine(
    fly_api_endpoint: str,
    fly_api_token: str,
    app_name: str,
    app_config: dict
):
    # Define the API URL and headers
    url = f"{fly_api_endpoint}/v1/apps/{app_name}/machines"
    headers = {
        "Authorization": f"Bearer {fly_api_token}",
        "Content-Type": "application/json",
    }

    # Define the payload
    payload = app_config

    # Create the machine
    try:
        fly_create_machine_response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=10,
        )
        fly_create_machine_response.raise_for_status()  # Raises HTTPError for bad responses
        logger.info("Machine created successfully: %s", fly_create_machine_response.json())
    except RequestException as e:
        logger.error("Error creating machine: %s, %s", e, fly_create_machine_response.text)

    # Parse and return the machine ID
    fly_machine = fly_create_machine_response.json()
    machine_id = fly_machine.get("id")

    if machine_id:
        logger.info("Machine ID: %s", machine_id)
        return machine_id
    else:
        logger.error("Machine ID not found in response")
