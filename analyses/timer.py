"""
Handle Timer.
"""
import logging

from supervisor.save_and_restore import finished

logger = logging.getLogger()
TASK_DESCRIPTION = 'we are inferring the timer'

__get_timer_info = []


def by_dot_config(firmware):
    pass


def by_source_code(firmware):
    pass


def by_toh(firmware):
    pass


def by_strings(firmware):
    pass


def register_get_timer_info(func):
    __get_timer_info.append(func)


register_get_timer_info(by_dot_config)
register_get_timer_info(by_source_code)
register_get_timer_info(by_toh)
register_get_timer_info(by_strings)


def get_timer_info(firmware):
    logger.info(TASK_DESCRIPTION)
    timer_model = firmware.get_timer_model()
    if timer_model is not None:
        logger.info('\033[32mtimer model {} found\033[0m [DEVICE TREE]'.format(timer_model))
        return
    for func in __get_timer_info:
        if finished(firmware, 'get_timer_info', func.__name__):
            continue
        func(firmware)
        finished(firmware, 'get_timer_info', func.__name__)
