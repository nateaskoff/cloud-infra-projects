import logging
import os

# Set up logging
logger = logging.getLogger()

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