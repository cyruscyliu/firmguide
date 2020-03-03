#!/usr/bin/python
import os
import sys
import tempfile
sys.path.extend(['.', '..', '../..'])

from slcore.compositor import unpack

def scan_dt(argv):
    fs = []

    # scan_dt.py -d dir
    if len(argv) == 3 and argv[1] == '-d':
        for f in os.listdir(argv[2]):
            ff = os.path.join(argv[2], f)
            if os.path.isfile(ff):
                fs.append(ff)
    # scan_dt.py -f file
    elif len(argv) == 3 and argv[1] == '-f':
        f = argv[2]
        if os.path.exists(f):
            fs = [f]
    else:
        print('usage: scan_dt.py -d dir or scan_dt -f file')
        exit(-1)

    total, dt = 0, 0
    for i, f in enumerate(fs):
        components = unpack(f, target_dir=tempfile.gettempdir())
        print(components.__dict__)
        if components.has_device_tree():
            print('{:05}:Y:{}'.format(i, f))
            dt += 1
        else:
            print('{:05}:N:{}'.format(i, f))
        total += 1
    print('-----:Y:{}({})'.format(dt, total))

if __name__ == '__main__':
    scan_dt(sys.argv)

