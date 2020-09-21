import logging
import sys

import urllib3

from config import Config

log_level = Config.log_level
logging.basicConfig(level=log_level)
logger = logging.getLogger('stinger')
logger.propagate = False

INFO_FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s'
DEBUG_FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s ' \
               '[in %(pathname)s:%(lineno)d]'
TIMESTAMP_FORMAT = '%d-%m-%Y %H:%M:%S %z'

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(
    logging.Formatter(DEBUG_FORMAT, TIMESTAMP_FORMAT),
)
logger.addHandler(stream_handler)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_logger():
    return logger
