# logging means -> you can add logs to the failure, error, information, warning to the user

import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("This is information Logs")
    LOGGER.warning("This is warning Logs")
    LOGGER.error("This is error Logs")
    LOGGER.critical("This is critical Logs")

