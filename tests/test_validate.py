# fix importing errors
import sys
import os
project_root = os.path.abspath(os.path.dirname(__file__) + "/..")
if project_root not in sys.path:
    sys.path.append(project_root)

import unittest

from backend import validate

class TestValidateEmail(unittest.TestCase):
    def test_at_symbol(self):
        self.assertTrue(validate.email('hellopanda@gmail.com'))
        self.assertFalse(validate.email('hellopandagmail.com'))
        self.assertFalse(validate.email("hellopanda#gamil.com"))

    def test_no_space(self):
        self.assertTrue(validate.email("hellopanda@gmail.com"))
        self.assertFalse(validate.email("hello panda@gmail.com"))

    def test_in_domain(self):
        self.assertTrue(validate.email("hellopanda@gmail.com"))
        self.assertFalse(validate.email("hellopanda@gmailcom"))

class TestValidatePassword(unittest.TestCase):
    def test_no_space(self):
        self.assertTrue(validate.password("@R3alPassword"))
        self.assertFalse(validate.password("a real password"))

    def test_length(self):
        self.assertTrue(validate.password("@R3alPassword"))
        self.assertTrue(validate.password("R3alPassw@rd"))
        self.assertFalse(validate.password("@R3alPass"))

    def test_uppercase(self):
        self.assertTrue(validate.password("@R3alPassword"))
        self.assertFalse(validate.password("arealpassword"))


    def test_number(self):
        self.assertTrue(validate.password("@R3alPassword"))
        self.assertFalse(validate.password("aRealPassword"))

    def test_special_char(self):
        self.assertTrue(validate.password("@R3alPassword"))
        self.assertFalse(validate.password('aR3alPassword'))

class TestValidateName(unittest.TestCase):
    def test_presence_of_symbols(self):
        self.assertFalse(validate.name('J@hn'))
        self.assertTrue(validate.name('John Tan'))

    def test_numbers(self):
        self.assertTrue(validate.name('John'))
        self.assertFalse(validate.name('J0hn'))

class TestValidateClass(unittest.TestCase):
    def test_letters(self):
        self.assertTrue(validate.class_number('2426'))
        self.assertFalse(validate.class_number('2a26'))

    def test_length(self):
        self.assertTrue(validate.class_number('2426'))
        self.assertFalse(validate.class_number('23456'))

    def test_special_characters(self):
        self.assertTrue(validate.class_number('1234'))
        self.assertFalse(validate.class_number('24@26'))

if __name__ == '__main__':
    unittest.main()