#!/usr/local/bin/python3.7

import os
import sys

from record import Reader

ARM = 1


def main(filename):
    reader = Reader(filename=filename)
    for record in reader.get_record():
        if ARM:
            for i in range(12):
                if i < 10 and i % 6 != 0:
                    pre = ' r'
                else:
                    pre = 'r'

                if i % 6 == 5:
                    print('{}{}={:0>8x}'.format(pre, i, record['regs'][i]))
                else:
                    print('{}{}={:0>8x}'.format(pre, i, record['regs'][i]), end=' ')
            print('ip={:0>8x}'.format(record['regs'][12]), end=' ')
            print(' sp={:0>8x}'.format(record['regs'][13]), end=' ')
            print(' cl={:0>8x}'.format(record['regs'][14]), end=' ')
            print(' pc={:0>8x}'.format(record['regs'][15]), end=' ')
            print('cspr={:0>8x}'.format(record['regs'][16]), end=' ')
            print('xspr={:0>8x}'.format(record['regs'][17]))
            print(record['code'], end=' ')
            print('-------------------------------')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage python3.7 {} filename'.format(sys.argv[0]))
        exit(-1)
    filename = sys.argv[1]
    main(filename)
