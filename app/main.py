import logging
from .core.logging import setup_logging
from app.request.request import worker_request

logger = logging.getLogger(__name__)
setup_logging()

def main()->None:
    logger.info("Start app background")
    worker_request.run()
    logger.info("Stop app background")

if __name__ == "__main__":
    main()