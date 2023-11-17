import logging 
from prac_logging import add_module_handler

logger = logging.getLogger(__name__)
add_module_handler(logger=logger)


def func2():
    logger.debug("debug call from utils.func2")
    logger.critical("Critical called from utils.func2")