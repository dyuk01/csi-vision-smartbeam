import logging

logging.basicConfig(
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO  # You can change to DEBUG for more verbose output
)


def log_event(message: str) -> None:
    logging.info(message)