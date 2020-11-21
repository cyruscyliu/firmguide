import os
import yaml

from slcore.parser import get_candidates, get_all_strings


def find_board_dir_s(strings, arch):
    """Find which Linux kernel board the image belongs to.

    Args:
        strings (list): Strings from the image.
        arch (str)    : The architecture. It's required because of the db interface.

    Returns:
        list: A list of Linux kernel boards the image may belongs to.
    """
    # TODO the signature should be refined because of too much FP
    signature = yaml.safe_load(open(os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'by_board_dir', 'signature.{}.yaml'.format(arch))))

    # construct
    target_strings = {}
    votes = {}
    hit_strings = {}
    for k, strs in signature.items():
        target_strings[k] = strs
        votes[k] = 0
        hit_strings[k] = []

    # search
    for string in strings:
        string = string.strip()
        for k, v in target_strings.items():
            if string in v:
                votes[k] += 1
                hit_strings[k].append(string)

    # vote
    target_board_dir = []
    max_to_min = sorted(votes, key=votes.get, reverse=True)
    for vote in max_to_min:
        if votes[vote] > 1:
            target_board_dir.append((vote, hit_strings[vote]))

    return target_board_dir


def find_board_dir(path_to_kernel, arch):
    """Find which Linux kernel board the image belongs to.

    Args:
        path_to_kernel(str): Path to the kernel. We will get strings from it.
        arch (str)         : The architecture. It's required because of the db interface.

    Returns:
        list: A list of Linux kernel boards the image may belongs to.
    """
    candidates = get_candidates(path_to_kernel)
    strings = get_all_strings(candidates)
    return find_board_dir_s(strings, arch)
