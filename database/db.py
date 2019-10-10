import abc
import csv
import os

from database.dbi import DatabaseInterface, Firmware
from profile.dt import DTFirmware
from profile.ipxact import IPXACTFirmware
from profile.simple import SimpleFirmware


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


class DatabaseText(Database, DatabaseInterface):
    def get_count(self, *args, **kwargs):
        return self.count

    def get_firmware(self, *args, **kwargs):
        for firmware in self.records:
            yield firmware

    def select(self, *args, **kwargs):
        pass

    def add(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass

    def __init__(self, path, **kwargs):
        super().__init__()
        self.dbtype = 'text'
        self.path = os.path.join(os.getcwd(), path)
        self.lazy_loading = False
        self.records = []
        self.count = None
        self.header = None
        self.profile = kwargs.pop('profile')

        if not self.lazy_loading:
            self.load()

    def load(self):
        # format for a record
        with open(self.path) as f:
            for id, line in enumerate(f):
                items = line.strip().split()
                if self.header is None:
                    self.header = items
                    continue
                uuid = items[self.header.index('uuid')]
                name = os.path.basename(items[self.header.index('path')])
                path = items[self.header.index('path')]
                size = os.path.getsize(path)
                if self.profile == 'simple':
                    firmware = SimpleFirmware(uuid=uuid, name=name, path=path, size=size)
                elif self.profile == 'dt':
                    firmware = DTFirmware(uuid=uuid, name=name, path=path, size=size)
                elif self.profile == 'ipxact':
                    firmware = IPXACTFirmware(uuid=uuid, name=name, path=path, size=size)
                else:
                    raise NotImplementedError

                brand = items[self.header.index('brand')]
                arch = items[self.header.index('arch')]
                endian = items[self.header.index('endian')]
                firmware.set_brand(brand)
                firmware.set_architecture(arch)
                firmware.set_endian(endian)
                firmware.id = id
                self.records.append(firmware)
        self.count = self.records.__len__()


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
