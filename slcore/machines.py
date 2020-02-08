from slcore.database.dbf import get_database
from slcore.naive_parsers.machine_id import find_machine_id
from slcore.dt_parsers.compatible import find_compatible

def find_machine_by_compatible(arch, compatibles):
    support = get_database('support')

    for compatible in compatibles:
        profile = support.select('profile', arch=arch, compatible=compatible)
        if profile is not None:
            return profile

def find_machine_by_id(arch, machine_ids):
    support = get_database('support')

    for machine_id in machine_ids:
        profile = support.select('profile', arch=arch, machine_id=machine_id)
        if profile is not None:
            return profile

def find_machine(components, arch):
    if components is None:
        return None

    if components.has_device_tree():
        compatible = find_compatible(components.get_path_to_dtb())
        machine = find_machine_by_compatible(arch, compatible)
    else:
        machine_ids = find_machine_id(components.get_path_to_kernel())
        machine = find_machine_by_id(arch, machine_ids)

    return machine

