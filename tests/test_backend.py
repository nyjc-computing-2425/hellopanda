# fix importing errors
import sys
import os
project_root = os.path.abspath(os.path.dirname(__file__) + "/..")
if project_root not in sys.path:
    sys.path.append(project_root)

import unittest
import sqlite3

import backend

class TestAccountRetrieveFunctions(unittest.TestCase):
    def test_store(self):
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

    def test_retrieve_by_name(self):
        pass

    def test_retrieve_by_class(self):
        pass

    def test_retrieve_by_email(self):
        pass

    def test_retrieve_by_year(self):
        pass

    def test_get_account_type(self):
        pass

class TestAccountUpdateFunctions(unittest.TestCase):
    def test_update_name(self):
        conn = sqlite3.connect('tests/test.db')
        
        conn.execute(backend.sql.CREATE_TABLE_ACCOUNT)
        conn.execute(backend.sql.INSERT_INTO_ACCOUNT, ['abc@gmail.com', 'abcde', '@R3alPassword', 'student', 'Jonathan Lim', 2426, 2025]) # [email, salt, password, _type, name, _class, graduation_year]
        conn.commit()

        conn.execute(backend.sql.UPDATE_ACCOUNT_NAME, ['Rebecca Tan', 'abc@gmail.com'])
        conn.commit()

        cursor = conn.execute("SELECT * FROM account")
        rows = cursor.fetchall()

        conn.execute(backend.sql.DELETE_TABLE_ACCOUNT)
        conn.commit()
        conn.close()
        
        self.assertEqual(list(rows[0]), ['abc@gmail.com', 'abcde', '@R3alPassword', 'student', 'Rebecca Tan', 2426, 2025])
    def test_update_class(self):
        conn = sqlite3.connect('tests/test.db')
        
        conn.execute(backend.sql.CREATE_TABLE_ACCOUNT)
        conn.execute(backend.sql.INSERT_INTO_ACCOUNT, ['abc@gmail.com', 'abcde', '@R3alPassword', 'student', 'Jonathan Lim', 2426, 2025]) # [email, salt, password, _type, name, _class, graduation_year]
        conn.commit()
    
        conn.execute(backend.sql.UPDATE_ACCOUNT_CLASS, [2430, 'abc@gmail.com'])
        conn.commit()

        cursor = conn.execute("SELECT * FROM account")
        rows = cursor.fetchall()

        conn.execute(backend.sql.DELETE_TABLE_ACCOUNT)
        conn.commit()
        
        conn.close()
        
        self.assertEqual(list(rows[0]), ['abc@gmail.com', 'abcde', '@R3alPassword', 'student', 'Jonathan Lim', 2430, 2025])

    def test_update_email(self):
        pass

    def test_update_year(self):
        pass

if __name__ == "__main__":
    unittest.main()