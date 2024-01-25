import sys
from loguru import logger

from settings import Settings

def get_logger(name):
    logger.remove()
    format = '{time:DD-MM-YYYY hh:mm} | {level} | ' + name + ' | {message}'
    logger.add(
        Settings.LOG_PATH.value,
        level='DEBUG', 
        rotation='1 DAY',
        format=format,
        backtrace=True,
    )
    logger.add(
        sys.stdout,
        level='DEBUG', 
        format=format,
        backtrace=True,
        colorize=None
    )
    return logger
