#!/usr/bin/python

"""
This file statistics how much progress we have made.
"""
import os
import argparse

from profile.convert import load_simple, load_dt, convert_from_dt_to_simple, get_simple

expectation = {
        'components': {
            'path_to_image':{'required':True},
            'path_to_uimage':{'required':True},
            'path_to_dtb':{'required':False},
        }, 'basics': {
            'machine_name':{'required':True},
            'machine_description':{'required':True},
            'board_id':{'required':True},
        }, 'cpu': {
            'model': {'required':True},
        }, 'ram': {
            'base': {'required':False},
            'size': {'required':True},
            'priority': {'required':True},
        }, 'interrupt_controller': {
            'name': {'required':True},
            'mmio_base': {'required':True},
            'mmio_size': {'required':True},
        }, 'bridge': {
            'name': {'required':True},
            'mmio_base': {'required':True},
            'mmio_size': {'required':True},
        }, 'timer': {
            'name': {'required':True},
            'mmio_base': {'required':True},
            'mmio_size': {'required':True},
        },'uart': {
            'name': {'required':True},
            'mmio_base': {'required':True},
            'mmio_size': {'required':False},
            'baud_rate': {'required':True},
            'reg_shift': {'required':2},
            'irq': {'required':False},
            },'flash': {
            'type': {'required':True},
            'base': {'required':True},
            'section_size': {'required':False},
            'size': {'required':True},
                }
            }

def handle_file(path):
    stat = {}
    if args.p == 'simple':
        profile = load_simple(path)
    else:
        dt_profile = load_dt(path)
        profile = get_simple()
        # use simple profile finally
        profile = convert_from_dt_to_simple(dt_profile, profile)
    return stat


def run(args):
    path = args.path
    if os.path.isfile(path):
        mode = 'file'
    else:
        mode = 'recursive'

    stats = []
    # in different mode
    if mode == 'file':
        stat = handle_file(path)
        stats.append(stat)
    else:
        if args.p == 'simple':
            extend = 'yaml'
        else:
            extend = 'dt'
        for root, dirs, files in os.walk(path):
            if len(dirs):
                continue
            for filename in files:
                full_path = os.path.join(root, filename)
                if not full_path.endswith(extend):
                    continue
                stat = handle_file(full_path)
                stats.append(stat)
    print(stats)


if __name__ == '__main__':
    build = 'build'
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-p', choices=['simple', 'dt'], default='simple')
    parser.add_argument('path', help='path to profile or building directory')
    args = parser.parse_args()
    run(args)
