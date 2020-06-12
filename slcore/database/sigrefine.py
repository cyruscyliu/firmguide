#!/usr/bin/python
import os
import yaml
import argparse


def sigrefine(sigs):
    sig_arm = yaml.safe_load(open('signature.arm.yaml'))
    sig_mips = yaml.safe_load(open('signature.mips.yaml'))

    for sig in sigs:
        for k, v in sig_arm.items():
            if sig in v:
                v.remove(sig)
                print('[+] remove {} from signature.arm.yaml'.format(sig))
        for k, v in sig_mips.items():
            if sig in v:
                v.remove(sig)
                print('[+] remove {} from signature.mips.yaml'.format(sig))

    yaml.safe_dump(sig_arm, open('signature.arm.yaml', 'w'))
    yaml.safe_dump(sig_mips, open('signature.mips.yaml', 'w'))

    with open('sigrefined', 'a') as f:
        for sig in sigs:
            f.write('{}\n'.format(sig))


def sigrefine_all():
    sig_arm = yaml.safe_load(open('signature.arm.yaml'))
    sig_mips = yaml.safe_load(open('signature.mips.yaml'))

    sig_refined = []
    for k1, v1 in sig_arm.items():
        for sig in v1:
            for k2, v2 in sig_arm.items():
                if k2 == k1:
                    continue
                if sig in v2:
                    sig_refined.append(sig)

    for k1, v1 in sig_mips.items():
        for sig in v1:
            for k2, v2 in sig_mips.items():
                if k2 == k1:
                    continue
                if sig in v2:
                    sig_refined.append(sig)
    sigrefine(sig_refined)

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-s', metavar='sig', required=False, nargs='+', help='remove sigs')
    args = parser.parse_args()

    if args.s:
        sigrefine(args.s)
    else:
        sigrefine_all()
