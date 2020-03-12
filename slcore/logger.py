import os
import yaml
import logging
import logging.config

logger = logging.getLogger()
path_to_config = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.yaml')
log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'log')


def setup_logging(default_path=path_to_config, default_level=logging.INFO, uuid='salamander'):
    path = default_path
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.safe_load(f)
        config['handlers']['file']['filename'] = os.path.join(log_dir, '{}.log'.format(uuid))
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


# remove uuid because we log uuid by uuid
def logger_info2(group, object_, msg, status):
    logger.info(' - '.join([group, object_, msg]))


def logger_warning2(group, object_, msg, status):
    logger.warning(' - '.join([group, object_, msg]))


def logger_debug2(group, object_, msg, status):
    logger.debug(' - '.join([group, object_, msg]))

