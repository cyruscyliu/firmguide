import os

from unittest import TestCase

from database.firmware import DatabaseText


class TestDatabaseText(TestCase):
    def test_load(self):
        db = DatabaseText(os.path.join('database', 'firmware'))
        self.assertIsNotNone(db)
