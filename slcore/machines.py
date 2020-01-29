from logger import logger_info, logger_debug
from slcore.database.dbf import get_database
from slcore.naive_parsers.machine_id import find_machine_id
from slcore.dt_parsers.compatible import find_compatible

def find_machine_by_compatible(arch, compatible):
    support = get_database('support')

    for machine_id in machine_ids:
        profile = support.select('profile', arch=arch, compatible=compatible)
        if profile is not None:
            return profile

def find_machine_by_id(arch, machine_ids):
    support = get_database('support')

    for machine_id in machine_ids:
        profile = support.select('profile', arch=arch, machine_id=machine_id)
        if profile is not None:
            return profile

def find_machine(components):
    if components.has_device_tree():
        compatible = find_compatible(components.get_dtb())
        logger_info(components.uuid, 'machines', 'find_machine', 'compatible: {}'.format(compatible), 1)
        machine = find_machine_by_compatible(components.arch, compatble)
    else:
        machine_ids = find_machine_id(components.get_kernel())
        logger_info(components.uuid, 'machines', 'find_machine', 'machine_ids: {}'.format(machine_ids), 1)
        machine = find_machine_by_id(components.arch, machine_ids)

    if machine:
        logger_info(components.uuid, 'machines', 'find_machine', 'machine at {}'.format(machine), 1)
    else:
        logger_debug(components.uuid, 'machines', 'find_machine', 'no machine available', 0)

    return machine

