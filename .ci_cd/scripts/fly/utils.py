import base64
import logging

# Set up logging
logger = logging.getLogger()

# Function to create guest file object to append to 'files' section in config
def generate_fly_io_file_obj(
    file_path: str,
    guest_path: str
    ):
    # read file into base64 encoded string
    with open(file_path, "rb") as f:
        file_content = f.read()

    # encode file content to base64
    file_content_base64 = base64.b64encode(file_content).decode("utf-8")

    # create file object
    file_obj = {
        "guest_path": guest_path,
        "raw_value": file_content_base64
    }

    # return file object
    return file_obj
