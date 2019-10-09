"""
Handle CPU.
"""
import logging

from manager import finished, finish

logger = logging.getLogger()
TASK_DESCRIPTION = 'we\'re gonna infer what CPU model the firmware use'

__get_cpu_model_info = []


def by_dot_config(firmware):
    pass


def by_source_code(firmware):
    pass


def by_toh(firmware):
    LOG_SUFFIX = '[ToH]'
    cpu, soc = firmware.get_toh('packagearchitecture', 'cpu')
    if cpu is not None and cpu != '':
        firmware.set_cpu_model(cpu)
        logger.info('\033[32mget the cpu model: {}\033[0m {}'.format(cpu, LOG_SUFFIX))
    if soc is not None and cpu != '':
        firmware.set_soc_model(soc)
        logger.info('\033[32mget the soc model: {}\033[0m {}'.format(soc, LOG_SUFFIX))


def by_strings(firmware):
    pass


def register_get_cpu_model_info(func):
    __get_cpu_model_info.append(func)


register_get_cpu_model_info(by_dot_config)
register_get_cpu_model_info(by_source_code)
register_get_cpu_model_info(by_toh)
register_get_cpu_model_info(by_strings)


def get_cpu_model_info(firmware):
    logger.info(TASK_DESCRIPTION)
    cpu_model = firmware.get_cpu_model()
    if cpu_model is not None:
        logger.info('\033[32mcpu model {} found\033[0m [DEVICE TREE]'.format(cpu_model))
        return
    for func in __get_cpu_model_info:
        if finished(firmware, 'get_cpu_model_info', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'get_cpu_model_info', func.__name__)
