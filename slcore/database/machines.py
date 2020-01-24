from slcore.naive_parsers.machine_id import find_machine_id
from slcore.dt_parsers.compatible import find_compatible

def find_machine_by_compatible(compatible):
    pass

def find_machine_by_id(machine_id):
    pass

def find_machine(components):
    if components.has_device_tree():
        compatible = find_compatible(components.get_dtb())
        machine = find_machine_by_compatible(compatble)
    else:
        machine_id = find_machine_id(components.get_kernel())
        machine = find_machine_by_id(machine_id)

    return machine

