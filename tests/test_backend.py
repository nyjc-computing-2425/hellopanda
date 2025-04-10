# fix importing errors
import sys
import os
project_root = os.path.abspath(os.path.dirname(__file__) + "/..")
if project_root not in sys.path:
    sys.path.append(project_root)

import unittest
import sqlite3

import backend

class TestStoreAccountData(unittest.TestCase):
    def test_(self):
        conn = sqlite3.connect('tests/test.db')
        
        conn.execute(backend.sql.CREATE_TABLE_ACCOUNT)
        conn.execute(backend.sql.INSERT_INTO_ACCOUNT, ['abc@gmail.com', 'abcde', '@R3alPassword', 'student', 'Jonathan Lim', 2426, 2025]) # [email, salt, password, _type, name, _class, graduation_year]
        conn.commit()

        cursor = conn.execute("SELECT * FROM account")
        rows = cursor.fetchall()
        self.assertEqual(list(rows[0]), ['abc@gmail.com', 'abcde', '@R3alPassword', 'student', 'Jonathan Lim', 2426, 2025])
        
        conn.execute(backend.sql.DELETE_TABLE_ACCOUNT)
        conn.commit()
        
        conn.close()

if __name__ == "__main__":
    unittest.main()