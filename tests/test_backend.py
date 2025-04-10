# fix importing errors
import sys
import os
project_root = os.path.abspath(os.path.dirname(__file__) + "/..")
if project_root not in sys.path:
    sys.path.append(project_root)

import unittest
import sqlite3

# import backend

class TestStoreAccountData(unittest.TestCase):
    def test_(self):
        # conn = sqlite3.connect('test.db')
        # cursor = conn.cursor()
        # conn.execute(backend.sql.CREATE_TABLE_ACCOUNT)
        # conn.commit()
        self.assertEqual('abc', 'abc')

        