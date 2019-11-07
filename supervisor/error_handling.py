import logging

logger = logging.getLogger()


def error_callback(e):
    try:
        raise e
    except Exception as e:
        logger.exception(e)
