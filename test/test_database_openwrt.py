from unittest import TestCase

from database.db import DatabaseOpenWrt

import os


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
        db.table.close()
