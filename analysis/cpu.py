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
    logger.info('get ram info by table of hardware')
    pid = firmware.openwrt[0]
    openwrt = get_database('openwrt')
    result = openwrt.select('*', pid=pid, row=True)
    cpu = result[pid][openwrt.header_last_selected.index('packagearchitecture')]
    if cpu != '':
        firmware.metadata['cpu'].append({'value': cpu, 'confidence': 1})
        logger.info('\033[32mget the cpu model: {}, confidence: {}\033[0m'.format(cpu, 1))
    soc = result[pid][openwrt.header_last_selected.index('cpu')]
    if soc != '':
        firmware.metadata['soc'].append({'value': soc, 'confidence': 1})
        logger.info('\033[32mget the soc: {}, confidence: {}\033[0m'.format(soc, 1))
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


__check_qemu_support_for_cpu = []


def register_check_qemu_support_for_cpu(func):
    __check_qemu_support_for_cpu.append(func)


def by_qemu_support_lists(firmware):
    if firmware.cpu is not None:
        return
    if not len(firmware.metadata['cpu']):
        return
    cpu = vote(firmware.metadata['cpu'], 'cpu')
    qemu = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'cpu.yaml')))
    if firmware.arch == 'arm':
        support_list = qemu['arm']
    elif firmware.arch == 'mips':
        support_list = qemu['mips']
    else:
        raise NotImplementedError('have not support other archs except arm and mips')
    support_cpu_priv = None
    for support_cpu in support_list:
        if support_cpu.find('@') != -1:
            support_cpu_priv = support_cpu.split('@')[1]
            support_cpu = support_cpu.split('@')[0]
        if cpu.find(support_cpu) != -1:
            logger.info('\033[32mQEMU {} supports {}\033[0m'.format(support_cpu, cpu))
            firmware.cpu = support_cpu
            if support_cpu_priv is not None:
                firmware.cpu_priv = support_cpu_priv
                logger.info('\033[32mQEMU also supports {}\033[0m'.format(support_cpu_priv))
            break


def by_soc(firmware):
    if firmware.cpu is not None:
        return
    soc = vote(firmware.metadata['soc'], 'soc')
    socs = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'soc.yaml')))
    if soc in socs:
        support_cpu = socs[soc]['cpu']
        logger.info('\033[32mQEMU {} supports {}\033[0m'.format(support_cpu, soc))
        firmware.cpu = support_cpu


register_check_qemu_support_for_cpu(by_qemu_support_lists)
register_check_qemu_support_for_cpu(by_soc)


def check_qemu_support_for_cpu(firmware):
    for func in __check_qemu_support_for_cpu:
        func(firmware)
    if firmware.cpu is None:
        logger.info('\033[32mQEMU does not support {}\033[0m'.format(firmware.metadata['cpu']))


def make_cpu(firmware):
    if firmware.cpu is None:
        return
