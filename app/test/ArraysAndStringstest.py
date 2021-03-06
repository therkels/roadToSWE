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
    
    def test_is_one_away(self):
        test_tup = ("pale","ple")
        self.assertTrue(test_tup.is_one_away(test_tup))
        test_tup = ("pales","pale")
        self.assertTrue(test_tup.is_one_away(test_tup))
        test_tup = ("pale","bale")
        self.assertTrue(test_tup.is_one_away(test_tup))
        test_tup = ("pale","bake")
        self.assertFalse(test_tup.is_one_away(test_tup))

    def test_string_compression(self):
        test_string = "aabccccaaa"
        self.assertEquals("a2blc5a3", aas.compress_string(test_string))
        test_string = "abca"
        self.assertEquals("abca", aas.compress_string(test_string))