#!/usr/bin/python

import os
import fdt
import yaml
import argparse


def write_list_to_path(path, values, target_profile):
    node = target_profile.get_node(path, create=True)
    for i, value in enumerate(values):
        sub_node = target_profile.get_node(node.path + '/' + node.name + '/' + str(i), create=True)
        for p, v in value.items():
            if isinstance(v, list):
                write_list_to_path(sub_node.path + '/' + sub_node.name + '/' + p, v, target_profile)
            else:
                sub_node.append(fdt.PropStrings(p, v))


def convert_from_simple_to_dt(profile, target_profile):
    for key, values in profile.items():
        node = target_profile.get_node('/' + key, create=True)
        if isinstance(values, list):
            write_list_to_path('/bamboo', values, target_profile)
            continue
        for pr, values in values.items():
            if isinstance(values, list):
                write_list_to_path(node.path + node.name + '/' + pr, values, target_profile)
            else:
                node.append(fdt.PropStrings(pr, values))
    return target_profile


def convert_from_dt_to_simple(profile, target_profile):
    pass


def convert(profile, target_profile):
    if isinstance(profile, dict) and isinstance(target_profile, fdt.FDT):
        return convert_from_simple_to_dt(profile, target_profile)
    elif isinstance(profile, fdt.FDT) and isinstance(target_profile, dict):
        return convert_from_dt_to_simple(profile, target_profile)
    else:
        print('cannot support converting from {} to {}'.format(type(profile), type(target_profile)))
        exit(-1)


def get_dt():
    return fdt.parse_dts('/dts-v1/;\n\n/ {\n};\n')


def load_dt(path_to_profile):
    with open(path_to_profile, 'r') as f:
        profile = fdt.parse_dts(f.read())
    return profile


def save_dt(path_to_profile, target_profile):
    with open(path_to_profile, 'w') as f:
        f.write(target_profile.to_dts())


def get_simple():
    return {}


def load_simple(path_to_profile):
    with open(path_to_profile, 'r') as f:
        profile = yaml.safe_load(f)
    return profile


def save_simple(path_to_profile, target_profile):
    with open(path_to_profile, 'w') as f:
        yaml.safe_dump(target_profile, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-I', choices=['simple', 'dt'], required=True, help='input format of the profile')
    parser.add_argument('-O', choices=['simple', 'dt'], required=True, help='target format of the profile')
    parser.add_argument('input', metavar='path/to/profile')
    parser.add_argument('-o', metavar='path/to/target_profile')
    args = parser.parse_args()

    from_profile = args.I
    to_profile = args.O
    path_to_profile = args.input

    # no need to convert if they are same
    if from_profile == to_profile:
        print('input format and target format cannot be same')
        exit(-1)

    # load the input
    if from_profile == 'simple':
        profile = load_simple(path_to_profile)
    elif from_profile == 'dt':
        profile = load_dt(path_to_profile)
    else:
        print('input format {} is not valid'.format(from_profile))
        exit(-1)

    # get the output
    if args.o:
        path_to_target_profile = args.o
        if to_profile == 'simple':
            target_profile = get_simple()
        elif to_profile == 'dt':
            target_profile = get_dt()
        else:
            print('output format {} is not valid'.format(from_profile))
            exit(-1)
    else:
        name = os.path.join(
            os.path.dirname(path_to_profile), os.path.basename(path_to_profile).split('.')[0])
        if to_profile == 'simple':
            path_to_target_profile = name + '.yaml'
            target_profile = get_simple()
        elif to_profile == 'dt':
            path_to_target_profile = name + '.dt'
            target_profile = get_dt()
        else:
            print('input format {} is not valid'.format(from_profile))
            exit(-1)

    # convert
    target_profile = convert(profile, target_profile)

    # save to the output
    if to_profile == 'simple':
        save_simple(path_to_target_profile, target_profile)
    elif to_profile == 'dt':
        save_dt(path_to_target_profile, target_profile)
    else:
        print('output format {} is not valid'.format(from_profile))
        exit(-1)
