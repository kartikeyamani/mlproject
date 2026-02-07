import logging
import os
import sys
from datetime import datetime

from src.exception import CustomException

# 1. Create a naming convention for the log file (e.g., 02_05_2026_16_30_00.log)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the path where the log file will be stored
# This creates a 'logs' folder in your current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# 3. Create the directory even if it already exists
os.makedirs(os.path.join(os.getcwd(), "logs"), exist_ok=True)

# 4. Full path for the log file
LOG_FILE_PATH = os.path.join(logs_path)

# 5. Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Test code (Optional: you can delete this after testing)
if __name__ == "__main__":
    pass