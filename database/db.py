import os
import re
import abc
import csv
import yaml
import fcntl


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


class DatabasePaused(Database):
    def __init__(self):
        self.path = os.path.join(os.getcwd(), 'database', 'pause.yaml')
        if os.path.exists(self.path):
            self.last_paused_analyses = yaml.safe_load(open(self.path))
        else:
            self.last_paused_analyses = {}
        self.new_paused_analyses = {}
        # clear the database
        with open(self.path, 'w'):
            pass

    def select(self, *args, **kwargs):
        if self.last_paused_analyses:
            return [key for key in self.last_paused_analyses.keys()]

    def add(self, *args, **kwargs):
        uuid = kwargs.pop('uuid')
        name = kwargs.pop('name')
        hint = kwargs.pop('hint')
        input_ = kwargs.pop('input')
        self.new_paused_analyses[uuid] = {
            'name': name,
            'hint': hint,
            'input': input_
        }
        with open(self.path, 'a') as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            yaml.safe_dump(self.new_paused_analyses, f)
            fcntl.flock(f, fcntl.LOCK_UN)

    def delete(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass


class DatabaseOpenWRTMapping(Database):
    def select(self, *args, **kwargs):
        """
        select revision where kernel_version='2.6.32'
        select url where revision='10.03'
        select url where kernel_version='2.6.32'
        """
        action = args[0]
        table = open(os.path.join(os.getcwd(), 'database', 'openwrt.yaml'))

        if action == 'revision':
            kernel_version = kwargs.pop('kernel_version')
            openwrt_release_info = yaml.safe_load(table)
            for revision, info in openwrt_release_info.items():
                if info['kernel'] == kernel_version:
                    return revision
            return None

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')
        pass

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')
        pass

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')
        pass


class DatabaseOpenWRTToH(Database):
    """
    Will load openwrt.csv which is the official table of hardware from OpenWrt.
    Download it from https://openwrt.org/_media/toh_dump_tab_separated_csv.zip.
    We rename toh_dump_tab_separated_csv.csv to simple openwrt.csv.

    Note: the delimiter is '\t'.
    """

    def __init__(self):
        self.header_last_selected = None

    def select(self, *args, **kwargs):
        """
        select * where conditions [[transpose], [deduplicated]]
        select a, b, c where conditions [[transpose], [deduplicated]]
        check tests/test_openwrt_toh.py for more information
        return format
        """
        # parse control parameters
        transpose = kwargs.pop('transpose', False)
        deduplicated = kwargs.pop('deduplicated', False)
        # the rest are conditions
        conditions = kwargs
        # parse what you want to select
        if len(args) == 1 and args[0] == '*':
            args = ['pid', 'devicetype', 'brand', 'model', 'supportedsincerel', 'supportedcurrentrel',
                    'target', 'subtarget', 'packagearchitecture', 'bootloader', 'cpu', 'flashmb', 'rammb']
        # let's begin to execute the command
        columns = []
        records = []
        header = None
        table = open(os.path.join(os.getcwd(), 'database', 'openwrt.csv'))
        for line in csv.reader(table, delimiter='\t'):
            # save the header first
            if header is None:
                header = line
                for arg in args:
                    columns.append(header.index(arg))
                self.header_last_selected = args
                continue
            # check conditions, then
            valid = 1
            for k, v in conditions.items():
                if v is None:
                    continue
                if line[header.index(k)] != v:
                    valid = 0
                    break
            if not valid:
                continue
            # select columns what we need
            record = []
            for column in columns:
                item = line[column]
                record.append(item)
            records.append(record)
        # transpose if required
        if transpose:
            x = len(records)  # row -> column
            y = len(records[0])  # column -> row
            # construct
            records_t = []
            for yy in range(0, y):
                records_t.append([])
                for xx in range(0, x):
                    records_t[yy].append([])
            # fill
            for yy in range(0, y):
                for xx in range(0, x):
                    records_t[yy][xx] = records[xx][yy]
            # deduplicate
            if deduplicated:
                for i in range(len(records_t)):
                    records_t[i] = list(set(records_t[i]))
            records = records_t
        table.close()
        return records

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')
