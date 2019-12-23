import os
import logging
import logging.config

import yaml

logger = logging.getLogger()


def setup_logging(default_path="logging.yaml", default_level=logging.INFO):
    path = default_path
    if os.path.exists(path):
        with open(path, "r") as f:
            logging.config.dictConfig(yaml.safe_load(f))
    else:
        logging.basicConfig(level=default_level)


def logger_info(uuid, group, object, msg, status):
    if uuid is None:
        uuid = 'diagnosis'
    logger.info(' - '.join([uuid, group, object, msg]))


def logger_warning(uuid, group, object, msg, status):
    if uuid is None:
        uuid = 'diagnosis'
    logger.warning(' - '.join([uuid, group, object, msg]))


def logger_debugging(uuid, group, object, msg, status):
    if uuid is None:
        uuid = 'diagnosis'
    logger.debug(' - '.join([uuid, group, object, msg]))
