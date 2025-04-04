import unittest
import validate

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


if __name__ == '__main__':
    unittest.main()