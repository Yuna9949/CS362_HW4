import unittest
from Q2_ave_list import Q2_ave_list

class test_Q2(unittest.TestCase):

    def test_isList(self):
        self.assertTrue(Q2_ave_list.aveList([1,2,3,4,5]) not in "not list")

    def test_isEmpty(self):
        self.assertTrue(Q2_ave_list.aveList([1,2,3,4,5]) not in "empty")

    def test_isNumber(self):
        self.assertTrue(Q2_ave_list.aveList([1,2,3,4,5]) not in "not number")

        