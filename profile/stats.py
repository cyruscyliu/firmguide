#!/usr/bin/python

"""
This file statistics how much progress we have made.
"""
import os
import argparse

from profile.convert import load_simple, load_dt, convert_from_dt_to_simple, get_simple


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
    # output


if __name__ == '__main__':
    build = 'build'
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-p', choices=['simple', 'dt'], default='simple')
    parser.add_argument('path', help='path to profile or building directory')
    args = parser.parse_args()
