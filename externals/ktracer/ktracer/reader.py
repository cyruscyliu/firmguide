#!/usr/bin/python3.7

import os
import sys

import arm
import mips


def main(idx=0):
    ctx = open('/tmp/context.trace', 'rb')
    exec = open('/tmp/execution.trace', 'rb')
    # switch this manually for now
    #arm.parse_one_unit_trace(int(idx), ctx, exec)
    mips.parse_one_unit_trace(int(idx), ctx, exec)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        print (sys.argv[1])
        main(sys.argv[1])
    else:
        main()
