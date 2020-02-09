from slcore.database.dbf import get_database
from slcore.naive_parsers.machine_id import find_machine_id
from slcore.dt_parsers.compatible import find_compatible

def find_machine_by_compatible(arch, compatibles):
    support = get_database('support') # T4

    for compatible in compatibles:
        profile = support.select('profile', arch=arch, compatible=compatible)
        if profile is not None:
            return profile

def find_machine_by_id(arch, machine_ids):
    support = get_database('support') # T4

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
        # sometimes, a higher version of Linux kernel has device trees
        # TODO find_machine_dir has too much FP
        # machine_dirs = find_machine_dir(components.get_path_to_kernel(), arch) # T1
        # if not len(machine_dirs):
        #     print('error: find the source of this firmware and update machine signature')
        #     return
        # machine_dir = machine_dirs[0]
        # kernel_version = find_kernel_version(components.get_path_to_kernel())
        # if machine_has_device_tree(machine_dir, kernel_version): # T2
        #     compatible = find_compatible(components.get_path_to_kernel())
        #     machine = find_machine_by_compatible(compatible)
        # else:
        #     machine_ids = find_machine_id(components.get_path_to_kernel()) # T3
        #     machine = find_machine_by_id(arch, machine_ids)
    return machine

