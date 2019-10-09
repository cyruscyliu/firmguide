import os

import yaml

from manager import finished, finish

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
        if finished(firmware, 'check_qemu_support_for_cpu', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'check_qemu_support_for_cpu', func.__name__)


__check_qemu_support_for_flash = []


def by_qemu_support_list(firmware):
    flash_type = firmware.get('flash', key='type')
    if flash_type is None:
        return
    qemu = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'flash.yaml')))
    support_list = qemu[flash_type]


def reigster_check_qemu_support_for_flash(func):
    __check_qemu_support_for_flash.append(func)


def check_qemu_support_for_flash(firmware):
    for func in __check_qemu_support_for_flash:
        if finished(firmware, 'check_qemu_support_for_flash', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'check_qemu_support_for_flash', func.__name__)


def check_qemu_support_for_uart(firmware):
    uart_model = firmware.get('uart', key='model')
    if uart_model is None:
        return
    qemu = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'uart.yaml')))
    for k, v in qemu.items():
        if v is None:
            continue
        conditions = v['condition_or']
        __flag = 0
        for key in conditions:
            if uart_model.find(key) != -1:
                __flag = 1
                firmware.set('uart', key='qemu', value=k, confidence=1)
                break
        if __flag:
            break