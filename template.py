import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:  %(message)s')

list_of_files = [
    ".github/workflows/.gitkeep",
    "backend/generate_blog.py",
    "app.py",
    "endpoint.py",
    ".env",
    "requirements.txt",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent
    filename = filepath.name

    # Create directory if it doesn't exist
    if filedir != Path("."):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    # Create file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists and is not empty.")
