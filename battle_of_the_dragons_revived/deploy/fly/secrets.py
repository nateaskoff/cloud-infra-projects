import logging
import os
import subprocess
import re

# Set up logging
logger = logging.getLogger()

# Function to get a secret for a Fly.io app
def get_fly_app_secret(app_name: str, secret_name: str):
    try:
        # Run the flyctl command to get the secret
        command = ["flyctl", "secrets", "get", secret_name, "-a", app_name]
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Search for the secret value in the command output
        match = re.search(rf"{secret_name}:\s+(.*)", result.stdout)
        if match:
            secret_value = match.group(1).strip()
            logger.info(f"Secret '{secret_name}' retrieved successfully")
            return secret_value
        else:
            logger.warning(f"Secret '{secret_name}' not found in output")
            return None
    except subprocess.CalledProcessError as e:
        logger.warning(f"Error retrieving secret '{secret_name}': {e.stderr}")
        return None
    except Exception as e:
        logger.warning(f"Unexpected error: {e}")
        return None

# Function to set secrets for a fly app
def set_fly_app_secret(
    app_name: str,
    secret_name: str,
    secret_value: str
    ):
    # Use flyctl to set secret
    try:
        os.system(f"flyctl secrets set {secret_name}={secret_value} --app {app_name}")
        logger.info(f"Secret {secret_name} set successfully")
    except Exception as e:
        logger.error(f"Error setting secret {secret_name}: {e}")
        return

    # return
    return True
