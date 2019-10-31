"""
Handle CPU.
"""
import os
import logging

from analyses.asm.gnu import parser_proc_info_init
from analyses.makefile import obj_definition_filter
from manager import finished, finish

logger = logging.getLogger()
TASK_DESCRIPTION = 'we\'re gonna infer what CPU model the firmware use'

__get_cpu_model_info = []


def by_dot_config(firmware):
    LOG_PREFIX = '[.config]'
    architecture = firmware.get_architecture()
    if architecture != 'arm':
        return
    path_to_source_code = firmware.get_path_to_source_code()
    path_to_mm = os.path.join(path_to_source_code, 'arch/{}/mm'.format(architecture))
    path_to_mm_makefile = os.path.join(path_to_mm, 'Makefile')
    path_to_dot_config = os.path.join(path_to_source_code, '.config')
    configs = []
    with open(path_to_dot_config) as f:
        for line in f:
            if line.startswith('#'):  # comment
                continue
            if line.find('=') == -1:  # is not set
                continue
            if line.find('CPU') == -1:  # not related to this task
                continue
            config = line.strip().split('=')
            configs.append(config[0])
    stmts = obj_definition_filter(path_to_mm_makefile, configs)
    targets = []
    for stmt in stmts:
        targets.append(stmt.value[:-2])
    for file_ in os.listdir(path_to_mm):
        if file_.find('.') == -1:
            continue
        name, extent = file_.split('.')
        if name in targets:
            cpus = parser_proc_info_init(os.path.join(path_to_mm, file_))
            if cpus is None:
                continue
            for cpu, properties in cpus.items():
                logger.info('\033[32mget cpu model: {} \033[0m {}'.format(properties, LOG_PREFIX))
                path_to_cpu = firmware.find_cpu_nodes(new=True)
                for k, v in properties.items():
                    firmware.set_node_property(path_to_cpu, k, v)


def by_toh(firmware):
    LOG_SUFFIX = '[ToH]'
    cpu, soc = firmware.get_toh('packagearchitecture', 'cpu')
    if cpu is not None and cpu != '':
        firmware.set_cpu_model(cpu)
        logger.info('\033[32mget cpu model: {}\033[0m {}'.format(cpu, LOG_SUFFIX))
    if soc is not None and cpu != '':
        firmware.set_soc_model(soc)
        logger.info('\033[32mget soc model: {}\033[0m {}'.format(soc, LOG_SUFFIX))


def register_get_cpu_model_info(func):
    __get_cpu_model_info.append(func)


register_get_cpu_model_info(by_dot_config)
register_get_cpu_model_info(by_toh)


def get_cpu_model_info(firmware):
    logger.info(TASK_DESCRIPTION)
    cpus = firmware.find_cpu_nodes()
    if len(cpus):
        logger.info('\033[32mcpu model has been already found\033[0m')
        return
    for func in __get_cpu_model_info:
        if finished(firmware, 'get_cpu_model_info', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'get_cpu_model_info', func.__name__)
