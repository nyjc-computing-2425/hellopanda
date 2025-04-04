import unittest
import validate

class validate_email_tc(unittest.TestCase):
    def test_at_symbol(self):
        self.assertTrue(validate_email('kenneth@gmail.com'))
        self.assertFalse(validate_email('kennethgmail.com'))

class TestValidateName(unittest.TestCase):
    def test_presence_of_symbols(self):
        self.assertFalse(validate.name('J@hn'))
        self.assertTrue(validate.name('John Tan'))

    def test_numbers(self):
        self.assertTrue(validate.name('John'))
        self.assertFalse(validate.name('J0hn'))

class TestValidateClass(unittest.TestCase):
    def test_letters(self):
        self.assertTrue(validate.class('2426'))
        self.assertFalse(validate.class('2a26'))
    
    def test_length(self):
        self.assertTrue(validate.class('2426'))
        self.assertFalse(validate.class('23456'))

    def test_special_characters(self):
        self.assertTrue(validate.class('1234'))
        self.assertFalse(validate.class('24@26'))

if __name__ == '__main__':
    unittest.main()