import logging
import requests

# Set up logging
logger = logging.getLogger()

# Function to deploy fly app
def deploy_fly_machine(
    fly_api_endpoint: str,
    fly_api_token: str,
    app_name: str,
    app_config: dict
    ):
    # define api url and headers
    url = f"{fly_api_endpoint}/api/v1/apps/{app_name}/machines"

    # define headers
    headers = {
        "Authorization": f"Bearer {fly_api_token}",
        "Content-Type": "application/json",
    }

    # define payload
    payload = app_config

    # create machine
    try:
        fly_create_machine_response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=10,
        )
        fly_create_machine_response.raise_for_status()
        logger.info("Machine created successfully")
    except Exception as e:
        logger.error("Error creating machine: %s", e)
        return

    # get machine id
    fly_machine = fly_create_machine_response.json()

    # return machine id
    return fly_machine["id"]
