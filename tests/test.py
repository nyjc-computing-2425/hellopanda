import unittest

def validate_email(email):
    return True

class validate_email_tc(unittest.TestCase):
    def test_at_symbol(self):
        self.assertTrue(validate_email('kenneth@gmail.com'))
        self.assertFalse(validate_email('kennethgmail.com'))

if __name__ == '__main__':
    unittest.main()