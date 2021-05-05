import unittest
from app.src import RecursionAndDynamic as dac


class Test(unittest.TestCase):
    def test_is_fun(self):
        self.assertEqual("fun",dac.fun_function())