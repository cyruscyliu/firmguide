#!/usr/bin/python
import yaml
import argparse


def sigrefine(args):
    sig_arm = yaml.safe_load(open('signature.arm.yaml'))
    sig_mips = yaml.safe_load(open('signature.mips.yaml'))

    for sig in args.s:
        for k, v in sig_arm.items():
            if sig in v:
                v.remove(sig)
                print('[+] remove {} from signature.arm.yaml'.format(sig))
        for k, v in sig_mips.items():
            if sig in v:
                v.remove(sig)
                print('[+] remove {} from signature.mips.yaml'.format(sig))

    yaml.safe_dump(sig_arm, open('signature.arm.yaml'))
    yaml.safe_dump(sig_mips, open('signature.mips.yaml'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-s', metavar='sig', required=True, nargs='+', help='remove sigs')
    args = parser.parse_args()

    sigrefine(args)
