import logging
import os

# Set up logging
logger = logging.getLogger()

# Function to get secrets for a fly app
def get_fly_app_secret(
    app_name: str,
    secret_name: str
    ):
    # Use flyctl to get secret
    try:
        secret_value = os.popen(f"flyctl secrets get {secret_name} --app {app_name}").read()
        logger.info(f"Secret {secret_name} retrieved successfully")
    except Exception as e:
        logger.info(f"Secret {secret_name} does not exist: {e}")
        return

    # return
    return secret_value

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
