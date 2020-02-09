from slcore.parser import get_candidates, get_all_strings
from settings import *

import os
import yaml

def find_machine_dir(path_to_kernel, arch):
    candidates = get_candidates(path_to_kernel)
    strings = get_all_strings(candidates)

    # TODO the signature should be refined because of too much FP
    signature = yaml.safe_load(open(os.path.join(
        BASE_DIR, 'slcore/naive_parsers/signature.{}.yaml'.format(arch))))

    # construct
    target_strings = {}
    votes = {}
    for k, strings in signature.items():
        target_strings[k] = strings
        votes[k] = 0

    # search
    for string in strings:
        string = string.strip()
        for k, v in target_strings.items():
            if string in v:
                votes[k] += 1

    # vote
    target_machine_dir = []
    max_to_min = sorted(votes, key=votes.get, reverse=True)
    for vote in max_to_min:
        if votes[vote] > 1:
            target_machine_dir.append(vote)

    return target_machine_dir

