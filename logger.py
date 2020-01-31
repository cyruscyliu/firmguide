import os
import yaml
import logging
import logging.config

from settings import *


logger = logging.getLogger()

def setup_logging(default_path="logging.yaml", default_level=logging.INFO, uuid='salamander'):
    path = default_path
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.safe_load(f)
        config['handlers']['file']['filename'] = os.path.join(BASE_DIR, 'log/{}.log'.format(uuid))
        config['root']['level'] = default_level
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def logger_info(uuid, group, object_, msg, status):
    logger.info(' - '.join([uuid, group, object_, msg]))


def logger_warning(uuid, group, object_, msg, status):
    logger.warning(' - '.join([uuid, group, object_, msg]))


def logger_debug(uuid, group, object_, msg, status):
    logger.debug(' - '.join([uuid, group, object_, msg]))

