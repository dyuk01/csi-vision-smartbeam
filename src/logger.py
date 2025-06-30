import os

from datetime import datetime

# Ensure logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_event(message: str) -> None:
    now = datetime.now()
    timestamp = now.strftime("[%Y-%m-%d %H:%M:%S]")
    log_filename = now.strftime("%Y-%m-%d.txt")
    log_path = os.path.join(LOG_DIR, log_filename)

    with open(log_path, "a") as f:
        f.write(f"{timestamp} {message}\n")
