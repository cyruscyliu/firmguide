import csv
import os

import yaml

from database.db import Database


class DatabaseOpenWRTMapping(Database):
    def select(self, *args, **kwargs):
        """
        select revision where kernel_version='2.6.32'
        select url where revision='10.03'
        select url where kernel_version='2.6.32'
        """
        action = args[0]
        table = open(os.path.join(os.getcwd(), 'database', 'openwrt_rk.yaml'))

        if action == 'revision':
            kernel_version = kwargs.pop('kernel_version')
            openwrt_release_info = yaml.safe_load(table)
            for revision, info in openwrt_release_info.items():
                if isinstance(info['kernel'], list) and kernel_version in info['kernel']:
                    return revision
                else:
                    if info['kernel'] == kernel_version:
                        return revision
            return None

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')


class DatabaseOpenWRTToH(Database):
    """
    Will load openwrt_toh.csv which is the official table of hardware from OpenWrt.
    Download it from https://openwrt.org/_media/toh_dump_tab_separated_csv.zip.
    We rename toh_dump_tab_separated_csv.csv to simple openwrt_toh.csv.

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
        table = open(os.path.join(os.getcwd(), 'database', 'openwrt_toh.csv'))
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
