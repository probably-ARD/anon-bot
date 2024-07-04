import logging
import sys
import settings


class _ColoredFormatter(logging.Formatter):
    COLORS = {
            'DEBUG': '\033[94m', 
            'INFO': '\033[92m', 
            'WARNING': '\033[93m',
            'ERROR': '\033[91m', 
            'CRITICAL': '\033[95m'
        }

    def format(self,  record):
        log_fmt_cmd = self._fmt.\
            replace('%(levelname)s', f'{self.COLORS.get(record.levelname, "")}%(levelname)s\033[0m').\
            replace('%(message)s', f'{self.COLORS.get(record.levelname, "")}%(message)s\033[0m')
        formatter = logging.Formatter(log_fmt_cmd)
        return formatter.format(record)

def getLogger(name: str | None) -> logging.Logger:
    fmt = '%(name)s | %(levelname)s | %(message)s'
    
    logger = logging.getLogger(name)
    logger.level = settings.LOG_LEVEL
    logger.handlers = [
        logging.FileHandler(settings.LOG_PATH, encoding='utf8'),
        logging.StreamHandler(stream=sys.stdout)
    ]
    logger.handlers[0].setFormatter(logging.Formatter(fmt))
    logger.handlers[-1].setFormatter(_ColoredFormatter(fmt))
    return logger
