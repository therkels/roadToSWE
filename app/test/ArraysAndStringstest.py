import unittest
from app.src import ArraysAndStrings as aas


class Test(unittest.TestCase):
    def test_is_unique(self):
        test_str = "abc"
        self.assertTrue(aas.is_unique(test_str))
        test_str = "book"
        self.assertFalse(aas.is_unique(test_str))
        test_str = "fondle"
        self.assertTrue(aas.is_unique(test_str))

    def test_check_permutation(self):
        a = "abc"
        b = "bac"
        self.assertTrue(aas.check_permutation(a, b))
        a = "back"
        b = "gack"
        self.assertFalse(aas.check_permutation(a, b))
        a = "asdf"
        b = "asdff"
        self.assertFalse(aas.check_permutation(a, b))

    def test_URLify(self):
        test_str = "Mr John Smith    "
        test_count = 13

    def test_palindrome(self):
        test_str = "tact coa"
        self.assertTrue(aas.is_palindrome(test_str))
        test_str = "ascda"
        self.assertFalse(aas.is_palindrome(test_str))
        test_str = "as"
        self.assertFalse(aas.is_palindrome(test_str))