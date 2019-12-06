import os
import json
import struct

ARM = 0x00000001
arch = [None, 'arm']


class Reader(object):
    def __init__(self, filename=None, fd=None, arch=ARM):
        if filename is not None and fd is not None:
            raise ValueError("filename and fd can be assigned at the same time")
        self.fd = None
        if filename is not None:
            self.fd = open(filename, 'rb')
        if fd is not None:
            self.fd = fd
        self.arch = arch

    def get_record(self):
        """
        An iterator to read next record in the trace.
        The record is deserialized to JSON  format.

        :return: None if no more record.
        """
        while 1:
            record_ = {'arch': arch[self.arch]}
            try:
                n_regs = struct.unpack('<I', self.fd.read(4))[0]
                regs = []
                for i in range(n_regs):
                    regs.append(struct.unpack('<I', self.fd.read(4))[0])
                code_size = struct.unpack('<I', self.fd.read(4))[0]
                code = self.fd.read(code_size).decode('utf-8')
                record_['n_regs'] = n_regs
                record_['regs'] = regs
                record_['code_size'] = code_size
                record_['code'] = code
                yield record_
            except struct.error:
                break
        return None


if __name__ == '__main__':
    cwd = os.getcwd()
    wd = os.path.dirname(cwd)
    reader = Reader(os.path.join(wd, 'trace', 'log'))
    for record in reader.get_record():
        print(record)
