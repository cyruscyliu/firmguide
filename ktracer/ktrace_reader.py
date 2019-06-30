#!/usr/local/bin/python3.7

import os
import sys
import struct

ARM = 1


def main(filename):
    trace = open(filename, 'rb')
    while 1:
        try:
            n_regs = struct.unpack('<I', trace.read(4))[0]
            regs = []
            for i in range(n_regs):
                regs.append(struct.unpack('<I', trace.read(4))[0])
            code_size = struct.unpack('<I', trace.read(4))[0]
            code = trace.read(code_size).decode('utf-8')
        except struct.error:
            break
        if ARM:
            for i in range(12):
                if i < 10 and i % 6 != 0:
                    pre = ' r'
                else:
                    pre = 'r'

                if i % 6 == 5:
                    print('{}{}={:0>8x}'.format(pre, i, regs[i]))
                else:
                    print('{}{}={:0>8x}'.format(pre, i, regs[i]), end=' ')
            print('sp={:0>8x}'.format(regs[13]), end=' ')
            print(' cl={:0>8x}'.format(regs[14]), end=' ')
            print(' pc={:0>8x}'.format(regs[15]), end=' ')
            print('cspr={:0>8x}'.format(regs[16]), end=' ')
            print('xspr={:0>8x}'.format(regs[17]))
            print(code, end=' ')
            print('-------------------------------')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage python3.7 {} filename'.format(sys.argv[0]))
        exit(-1)
    filename = sys.argv[1]
    main(filename)
