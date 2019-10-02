"""
Handle CPU.
"""
import os
import yaml
import logging

from analysis.common import vote
from database.dbf import get_database

logger = logging.getLogger()

__get_cpu_model_info = []


def by_device_tree(firmware):
    if firmware.dtb is None:
        return
    logger.info('get cpu model info by device tree')
    cpus = firmware.dtc.get_node('/cpus')
    for cpu in cpus.nodes:
        cpu_compatible = firmware.dtc.get_property('compatible', '/cpus/{}'.format(cpu.name)).data[0]
        firmware.metadata['cpu'].append({'value': cpu_compatible, 'confidence': 1})
        logger.info('\033[32mget the cpu model: {}, confidence: {}\033[0m'.format(cpu_compatible, 1))


def by_dot_config(firmware):
    if firmware.src is None:
        return


def by_source_code(firmware):
    if firmware.src is None:
        return


def by_toh(firmware):
    if firmware.openwrt is None:
        return
    pid = firmware.openwrt[0]
    openwrt = get_database('openwrt')
    result = openwrt.select('*', pid=pid, row=True)
    cpu = result[pid][openwrt.header_last_selected.index('cpu')]
    firmware.metadata['cpu'].append({'value': cpu, 'confidence': 1})
    logger.info('\033[32mget the cpu model: {}, confidence: {}\033[0m'.format(cpu, 1))
    openwrt.table.close()


def by_strings(firmware):
    if firmware.src is not None:
        return


def register_get_cpu_model_info(func):
    __get_cpu_model_info.append(func)


register_get_cpu_model_info(by_device_tree)
register_get_cpu_model_info(by_dot_config)
register_get_cpu_model_info(by_source_code)
register_get_cpu_model_info(by_toh)
register_get_cpu_model_info(by_strings)


def get_cpu_model_info(firmware):
    for func in __get_cpu_model_info:
        func(firmware)


def check_qemu_support_for_cpu(firmware):
    cpu = vote(firmware.metadata['cpu'], 'cpu')
    qemu = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'cpu.yaml')))
    if firmware.arch == 'arm':
        support_list = qemu['arm']
    elif firmware.arch == 'mips':
        support_list = qemu['mips']
    else:
        raise NotImplementedError('have not support other archs except arm and mips')
    for support_cpu in support_list:
        if cpu.find(support_cpu) != -1:
            logger.info('\033[32mQEMU {} supports {}\033[0m'.format(support_cpu, cpu))
            firmware.cpu = support_cpu
            break
    if firmware.cpu is None:
        logger.info('\033[32mQEMU does not support {}\033[0m'.format(cpu))


def make_cpu(firmware):
    pass
