#!/usr/bin/python
import sys
import yaml
import json
import argparse

sys.path.extend(['../..'])

from slcore.brick import Brick, to_offset, \
    to_upper, to_hex, to_qemu_endian


def burn_brick(b, parameter_file):
    context = yaml.safe_load(open(parameter_file))
    context['machine_name'] = 'test_machine'
    context['to_hex'] = to_hex
    context['to_upper'] = to_upper
    context['to_offset'] = to_offset
    context['to_endian'] = to_qemu_endian
    b_context = b.render(context)
    if isinstance(b_context, str):
        print('cannot suport {} {}, {} is missing'.format(
            args.type, b.effic_compatible, b_context))
        exit(-1)
    print(json.dumps(b_context, indent=4, sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'type',
        choices=['clk', 'cpu', 'ram', 'flash', 'mmio',
                 'intc', 'misc', 'serial', 'timer'],
        help='hardware type')
    parser.add_argument('compatible', nargs='+', help='hardware compatible')
    parser.add_argument('-c', '--context', help='yaml of the context')
    args = parser.parse_args()

    b = Brick(args.type, args.compatible)
    if not b.supported:
        print('{} {} is not supported'.format(args.type, args.compatible))
        exit(-1)

    if args.context is not None:
        burn_brick(b, args.context)
    else:
        print(json.dumps(vars(b), indent=4, sort_keys=True))
