import os
import yaml

from slcore.parser import get_candidates, get_all_strings


def find_machine_id_s(strings):
    """Find the machine id in the image.

    Args:
        strings(list): The strings from the image.

    Returns:
        list: The list of machine ids the image supports.
    """
    machine_ids = yaml.safe_load(open(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'machine_id.yaml')))

    # construct
    target_strings = {}
    votes = {}
    for k, machine_properties in machine_ids.items():
        if isinstance(machine_properties['machine_description'], list):
            target_strings[k] = machine_properties['machine_description']
        else:
            target_strings[k] = [machine_properties['machine_description']]
        votes[k] = 0

    # search
    for string in strings:
        string = string.strip()
        for k, v in target_strings.items():
            if string in v:
                votes[k] += 1

    # vote
    target_machine_id = []
    for k, vote in votes.items():
        if vote >= 1:
            if k.startswith('0x'):
                target_machine_id.append((k, machine_ids[k]))
            else:
                target_machine_id.append((hex(int(k)), machine_ids[k]))

    if len(target_machine_id) > 0:
        return [i[0] for i in target_machine_id]
    return None


def find_machine_id(path_to_kernel):
    """Find the machine id in the image.

    Args:
        path_to_kernel(str): The path to the image.

    Returns:
        list: The list of machine ids the image supports.
    """
    candidates = get_candidates(path_to_kernel)
    strings = get_all_strings(candidates)
    return find_machine_id_s(strings)
