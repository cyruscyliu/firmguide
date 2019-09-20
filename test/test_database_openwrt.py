from unittest import TestCase

from database.db import DatabaseOpenWrt

import os
import csv


class TestDatabaseOpenWrt(TestCase):
    def test_init(self):
        os.chdir(os.path.join(os.getcwd(), '..'))
        db = DatabaseOpenWrt()
        db.table.close()

    def test_select(self):
        os.chdir(os.path.join(os.getcwd(), '..'))
        db = DatabaseOpenWrt()
        selects = ['target', 'subtarget']
        results = db.select(*selects, deduplicated=True)
        columns = results.keys()
        for i, column in enumerate(columns):
            self.assertEqual(db.header[column], selects[i])
        selects = ['*']
        results = db.select(*selects, target='orion', row=True)
        self.assertEqual(4, len(results))
        db.table.close()

    def test_format(self):
        os.chdir(os.path.join(os.getcwd(), '..'))
        db = DatabaseOpenWrt()
        columns = None
        for line in csv.reader(db.table, delimiter='\t'):
            if columns is None:
                columns = len(line)
            self.assertEqual(columns, len(line))
        db.table.close()
