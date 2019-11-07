"""
Handle CPU.
"""
import os
import yaml
import logging

from analyses.asm.gnu import parser_proc_info_init
from analyses.lib.strings import get_strings
from analyses.makefile import obj_definition_filter
from supervisor.save_and_restore import finished, finish

logger = logging.getLogger()
TASK_DESCRIPTION = 'we\'re gonna infer what CPU model the firmware use'

__get_cpu_model_info = []


def cpu_done(firmware):
    cpus = firmware.find_cpu_nodes()
    if len(cpus):
        return True
    else:
        return False


def by_dot_config(firmware):
    # TODO must pre-process .S file, expand macro etc.
    if cpu_done(firmware):
        return
    LOG_PREFIX = '[.config]'
    architecture = firmware.get_architecture()
    if architecture != 'arm':
        return
    path_to_source_code = firmware.get_path_to_source_code()
    if path_to_source_code is None:
        return
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
    if cpu_done(firmware):
        return
    LOG_SUFFIX = '[ToH]'
    cpu, soc = firmware.get_toh('packagearchitecture', 'cpu')
    if cpu is not None and cpu != '':
        firmware.set_cpu_model(cpu)
        logger.info('\033[32mget cpu model: {}\033[0m {}'.format(cpu, LOG_SUFFIX))
    if soc is not None and cpu != '':
        firmware.set_soc_model(soc)
        logger.info('\033[32mget soc model: {}\033[0m {}'.format(soc, LOG_SUFFIX))


def by_strings(firmware):
    if cpu_done(firmware):
        return
    architecture = firmware.get_architecture()
    if architecture != 'arm':
        return
    LOG_SUFFIX = '[STRINGS]'
    candidates = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'arm32.cpu.yaml')))
    # construct
    target_strings = {}
    votes = {}
    for k, cpus in candidates.items():
        target_strings[k] = []
        votes[k] = 0
        for cpu in cpus:
            target_strings[k].append(cpu['cpu_arch_name'])
            target_strings[k].append(cpu['cpu_name'])
        target_strings[k] = list(set(target_strings[k]))
    strings = get_strings(firmware)
    if strings is None:
        return
    for string in strings:
        string = string.strip()
        for k, v in target_strings.items():
            if string in v:
                votes[k] += 1
    vote = 0
    model = ''
    for k, v in votes.items():
        if v > vote:
            vote = v
            model = k
    logger.info('\033[32mget cpu model: {} \033[0m {}'.format(candidates[model], LOG_SUFFIX))
    for cpu in candidates[model]:
        path_to_cpu = firmware.find_cpu_nodes(new=True)
        for k, v in cpu.items():
            firmware.set_node_property(path_to_cpu, k, v)


def register_get_cpu_model_info(func):
    __get_cpu_model_info.append(func)


register_get_cpu_model_info(by_dot_config)
register_get_cpu_model_info(by_toh)
register_get_cpu_model_info(by_strings)


def get_cpu_model_info(firmware):
    logger.info(TASK_DESCRIPTION)
    for func in __get_cpu_model_info:
        if finished(firmware, 'get_cpu_model_info', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'get_cpu_model_info', func.__name__)
