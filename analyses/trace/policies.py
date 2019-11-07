"""
Policy checking.
"""
import logging

from supervisor.save_and_restore import finished, finish

logger = logging.getLogger()

TASK_DESCRIPTION = 'check whether our profile goes smoothly'

__policy_checking = []


def check_usr_mode(firmware):
    pass


def register_policy_checking(func):
    __policy_checking.append(func)


register_policy_checking(check_usr_mode)


def policy_checking(firmware):
    logger.info(TASK_DESCRIPTION)
    for func in __policy_checking:
        if finished(firmware, 'policy_checking', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'policy_checking', func.__name__)
