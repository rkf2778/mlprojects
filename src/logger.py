import logging
import os
from datetime import datetime

# Correctly format the current time to name the log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory for logs
logs_dir = os.path.join(os.getcwd(), "logs")

# Ensure the directory exists
os.makedirs(logs_dir, exist_ok=True)

# Correct the LOG_FILE_PATH to point to the file within the logs directory
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Starting logging")
