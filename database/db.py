import abc
import csv
import os

from database.dbi import DatabaseInterface, Firmware


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
        self.path = os.path.join(os.getcwd(), 'database', path)
        self.lazy_loading = False
        self.records = []
        self.count = None

        if not self.lazy_loading:
            self.load()

    def load(self):
        # format for a record
        # uuid, relative path, brand, architecture, endian
        with open(self.path) as f:
            for line in f:
                items = line.strip().split()
                record = {
                    'uuid': items[0],
                    'name': os.path.basename(items[1]),
                    'path': items[1],
                    'brand': 'OpenWrt',
                    'arch': 'arm',
                    'endian': 'el',
                }
                self.records.append(Firmware(**record))
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

    def select(self, *args, **kwargs):
        columns = []
        results = {}
        for line in csv.reader(self.table, delimiter='\t'):
            if self.header is None:
                self.header = line
                for arg in args:
                    columns.append(self.header.index(arg))
            else:
                for column in columns:
                    item = line[column]
                    if column not in results:
                        results[column] = []
                    results[column].append(item)
        deduplicated = kwargs.pop('deduplicated', False)
        if deduplicated:
            for k, v in results.items():
                results[k] = list(set(v))
        return results

    def add(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass
