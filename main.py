import argparse

from db import get_database
from analysis.metadata import get_metadata
from analysis.abstract import extract_kernel_and_dtb, get_kernel_and_dtb


def run(args):
    if args.dbt is None:
        raise ValueError('no database available')
    dbi = get_database(args.dbt)
    count = dbi.get_count()
    if not count:
        return ValueError('no firmware available')
    if count > 100:
        raise NotImplementedError('multi threads not implemented yet')
    for firmware in dbi.get_firmware():
        if not args.s1:
            exit(0)
        extract_kernel_and_dtb(firmware)
        get_metadata(firmware)
        # get_source_code(firmware)
        if not args.s2:
            exit(0)
        get_kernel_and_dtb(firmware)
        if not args.s5:
            exit(0)
        # infer_cpu(firmware)
        if not args.s6:
            exit(0)
        # generate_cpu(firmware)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-dbt', required=True, choices=['text'], type=str,
                        help='assign the firmware db type')
    parser.add_argument('-s1', action='store_true', help='s1: get metadata and source code')
    parser.add_argument('-s2', action='store_true', help='s2: extract kernel, dtb if any')
    parser.add_argument('-s5', action='store_true', help='s5: get all info for cpu')
    parser.add_argument('-s6', action='store_true', help='s6: implement cpu')
    args = parser.parse_args()
    run(args)
