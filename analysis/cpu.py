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
    dtb = firmware.get('dtb')
    if dtb is None:
        return
    logger.info('get cpu model info by device tree')
    dtc = firmware.get('dtc')
    cpus = dtc.get_node('/cpus')
    for cpu in cpus.nodes:
        cpu_compatible = dtc.get_property('compatible', '/cpus/{}'.format(cpu.name)).data[0]
        firmware.set('cpu', key='model', value=cpu_compatible, confidence=1)


def by_dot_config(firmware):
    pass


def by_source_code(firmware):
    pass


def by_toh(firmware):
    toh = firmware.get('toh')
    if toh is None:
        return
    logger.info('get ram info by table of hardware')
    pid = toh[0]
    openwrt = get_database('openwrt')
    result = openwrt.select('*', pid=pid, row=True)
    cpu = result[pid][openwrt.header_last_selected.index('packagearchitecture')]
    if cpu != '':
        firmware.set('cpu', key='model', value=cpu, confidence=1)
    soc = result[pid][openwrt.header_last_selected.index('cpu')]
    if soc != '':
        firmware.set('soc', key='model', value=soc, confidence=1)
    openwrt.table.close()


def by_strings(firmware):
    pass


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


def by_qemu_support_lists(firmware):
    cpu = firmware.get('cpu', key='model')
    if cpu is not None:
        return
    qemu = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'cpu.yaml')))
    arch = firmware.get('arch')
    if arch == 'arm':
        support_list = qemu['arm']
    elif arch == 'mips':
        support_list = qemu['mips']
    else:
        raise NotImplementedError('have not support other archs except arm and mips')
    support_cpu_priv = None
    for support_cpu in support_list:
        if support_cpu.find('@') != -1:
            support_cpu_priv = support_cpu.split('@')[1]
            support_cpu = support_cpu.split('@')[0]
        if cpu.find(support_cpu) != -1:
            firmware.set('cpu', key='qemu', value=support_cpu, confidence=1)
            if support_cpu_priv is not None:
                firmware.set('cpu_priv', key='qemu', value=support_cpu_priv, confidence=1)
            break


def by_soc(firmware):
    cpu = firmware.get('cpu', key='model')
    if cpu is not None:
        return
    soc = firmware.get('soc', key='model')
    socs = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'soc.yaml')))
    if soc in socs:
        support_cpu = socs[soc]['cpu']
        firmware.set('cpu', key='qemu', value=support_cpu, confidence=1)


def register_check_qemu_support_for_cpu(func):
    __check_qemu_support_for_cpu.append(func)


register_check_qemu_support_for_cpu(by_qemu_support_lists)
register_check_qemu_support_for_cpu(by_soc)


def check_qemu_support_for_cpu(firmware):
    for func in __check_qemu_support_for_cpu:
        func(firmware)
