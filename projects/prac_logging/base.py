import logging 
from prac_logging import add_module_handler

logger = logging.getLogger(__name__)
add_module_handler(logger=logger)


def func1():
    logger.debug("debug call from base.func1")
    logger.critical("Critical called from base.func1")