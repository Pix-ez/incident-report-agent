import logging
import sys
from pythonjsonlogger import jsonlogger

def setup_logger(service_name: str):

    logger = logging.getLogger(service_name)

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)

    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )

    handler.setFormatter(formatter)

    logger.handlers.clear()
    logger.addHandler(handler)

    return logger