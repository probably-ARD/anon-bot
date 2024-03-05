import logging

import colorama
from colorama import Fore, Back


colorama.init(autoreset=True)

class _ColoredFormatter(logging.Formatter):
    '''
    Pretty colored formatter (only levels)
    check self.format
    Made by probably-ARD
    '''
    LOG_COLORS = {
    'DEBUG': Back.GREEN,
    'INFO': Back.CYAN,
    'WARNING': Back.MAGENTA,
    'ERROR': Back.YELLOW,
    'CRITICAL': Back.RED,
    'RESET': Back.RESET
    }
    
    def format(self, record: logging.LogRecord) -> str:
        # if need to remake log format -> 24, or 25 string
        log_fmt = f'''%(asctime)s | %(name)s | {self.LOG_COLORS.get(record.levelname, '')}{record.levelname.center(10) + colorama.Back.RESET} -> %(message)s'''
        formatter = logging.Formatter(log_fmt, datefmt='%d.%m.%Y --- %H:%M')

        return formatter.format(record)

def get_pretty_logger(name: str | None = None, path: str | None = None, level: str = logging.DEBUG) -> logging.Logger:
    '''
    returns logger with pretty formatter
    (check _ColoredFormatter.format to change format)
    level: logging._Level - where 10 - debug, 50 - critical
    name: str - the logger name in logs
    path: str - path to logging file
    '''
    plogger = logging.Logger(name.center(8))
    
    plogger.addHandler(logging.StreamHandler())
    plogger.handlers[0].setFormatter(_ColoredFormatter())

    if path is not None:
        plogger.addHandler(logging.FileHandler(path))
        plogger.handlers[1].setFormatter(
            logging.Formatter(
                '%(asctime)s | %(name)s | %(levelname)s -> %(message)s',
                datefmt='%d.%m.%Y --- %H:%M'
            )
        )
    
    return plogger

# ? мб запилить basicConfig
