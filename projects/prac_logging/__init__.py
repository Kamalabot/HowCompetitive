import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

levels = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")

# This module is imported when the project package is imported. You add a handler for each level in DEBUG through CRITICAL, then attach it to a single logger at the top of the hierarchy

for level in levels:
    handler = logging.FileHandler(f"level-{level.lower()}.log")
    handler.setLevel(getattr(logging, level))
    logger.addHandler(handler)

# You also define a utility function that adds one more FileHandler to a logger, where the filename of the handler corresponds to the module name where the logger is defined. (This assumes the logger is defined with __name__.)


def add_module_handler(logger, level=logging.DEBUG):
    handler = logging.FileHandler(f"module-{logger.name.replace('.','-')}.log")
    handler.setLevel(level)
    logger.addHandler(handler)
