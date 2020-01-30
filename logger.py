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


def logger_info(uuid, group, object_, msg, status):
    logger.info(' - '.join([uuid, group, object_, msg]))


def logger_warning(uuid, group, object_, msg, status):
    logger.warning(' - '.join([uuid, group, object_, msg]))


def logger_debug(uuid, group, object_, msg, status):
    logger.debug(' - '.join([uuid, group, object_, msg]))

