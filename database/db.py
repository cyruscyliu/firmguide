import os
import re
import abc
import csv

from database.dbi import DatabaseInterface


class Database(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def select(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def add(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def update(self, *args, **kwargs):
        pass


class DatabasePaused(DatabaseInterface):

    def parse_pre(self, line, **kwargs):
        pass

    def handle_post(self, firmware, **kwargs):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dbtype = 'paused'


class DatabaseFirmadyne(DatabaseInterface):

    def parse_pre(self, line, **kwargs):
        items = line.split(',')
        if self.header is None:
            self.header = items
            return
        kernel_extracted = items[self.header.index('kernel_extracted')]
        if kernel_extracted != 't':
            return
        uuid = items[self.header.index('id')]
        name = os.path.basename(items[self.header.index('filename')])
        path = items[self.header.index('filename')]
        brand = items[self.header.index('brand')]
        if not len(items[self.header.index('arch')]):
            arch = None
            endian = None
        else:
            arch = items[self.header.index('arch')][:-2]
            endian = items[self.header.index('arch')][-1:]
        # kernel_version: hard to use
        # kernel_version = items[self.header.index('kernel_version')]
        # if kernel_version:
        #     kernel_version = re.search(r'Linux kernel version (\d+\.\d+\.\d+)', kernel_version)
        # if kernel_version:
        #     kernel_version = kernel_version.groups()[0]
        description = items[self.header.index('description')]
        url = items[self.header.index('url')]
        self.items = {
            'uuid': uuid, 'name': name, 'path': path,
            'brand': brand, 'arch': arch, 'endian': endian,
            'description': description, 'url': url
        }
        return self.items

    def handle_post(self, firmware, **kwargs):
        firmware.set_brand(self.items['brand'])
        arch = self.items['arch']
        if arch is not None:
            firmware.set_architecture(arch)
            firmware.set_endian(self.items['endian'])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dbtype = 'firmadyne'


class DatabaseText(DatabaseInterface):
    def handle_post(self, firmware, **kwargs):
        firmware.set_brand(self.items['brand'])
        firmware.set_architecture(self.items['arch'])
        firmware.set_endian(self.items['endian'])
        firmware.set_description(self.items['description'])
        firmware.set_url(self.items['url'])

    def parse_pre(self, line, **kwargs):
        items = line.split()
        if self.header is None:
            self.header = items
            return
        uuid = items[self.header.index('uuid')]
        name = os.path.basename(items[self.header.index('path')])
        path = items[self.header.index('path')]
        brand = items[self.header.index('brand')]
        arch = items[self.header.index('arch')]
        endian = items[self.header.index('endian')]
        self.items = {
            'uuid': uuid, 'name': name, 'path': path,
            'brand': brand, 'arch': arch, 'endian': endian
        }
        return self.items

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dbtype = 'text'


class DatabaseOpenWrt(Database):
    """
    Will load openwrt.csv which is the official table of hardware from OpenWrt.
    Download it from https://openwrt.org/_media/toh_dump_tab_separated_csv.zip.
    We rename toh_dump_tab_separated_csv.csv to simple openwrt.csv.

    Note: the delimiter is '\t'.
    """

    def __init__(self):
        self.table = open(os.path.join(os.getcwd(), 'database', 'openwrt.csv'))
        self.header = None
        self.header_last_selected = None

    def select(self, *args, **kwargs):
        columns = []
        results = {}
        conditions = {
            'target': kwargs.pop('target', None),
            'pid': kwargs.pop('target', None),
        }
        return_column = kwargs.pop('column', True)
        return_row = kwargs.pop('row', False)
        deduplicated = kwargs.pop('deduplicated', False)
        if return_row:
            return_column = False
            assert not deduplicated, 'deduplicated only for returning format of column'
        for line in csv.reader(self.table, delimiter='\t'):
            if self.header is None:
                self.header = line
                continue
            if not len(columns):
                if len(args) == 1 and args[0] == '*':
                    args = ['pid', 'devicetype', 'brand', 'model', 'supportedsincerel', 'supportedcurrentrel',
                            'target', 'subtarget', 'packagearchitecture', 'bootloader', 'cpu', 'flashmb', 'rammb']
                for arg in args:
                    columns.append(self.header.index(arg))
                self.header_last_selected = args
            valid = 1
            for k, v in conditions.items():
                if v is None:
                    continue
                if line[self.header.index(k)] != v:
                    valid = 0
                    break
            if not valid:
                continue
            if return_row:
                results[line[0]] = [line[column] for column in columns]
            if return_column:
                for column in columns:
                    item = line[column]
                    if column not in results:
                        results[column] = []
                    results[column].append(item)
        if deduplicated:
            for k, v in results.items():
                results[k] = list(set(v))
        self.table.seek(0)
        return results

    def add(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass
