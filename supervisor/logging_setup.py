import os
import logging
import logging.config

import yaml

logger = logging.getLogger()


def setup_logging(default_path="logging.yaml", default_level=logging.INFO, env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            logging.config.dictConfig(yaml.safe_load(f))
    else:
        logging.basicConfig(level=default_level)


def logger_info(uuid, group, object, msg, status):
    logger.info(' - '.join([uuid, group, object, msg]))


def logger_warning(uuid, group, object, msg, status):
    logger.warning(' - '.join([uuid, group, object, msg]))
