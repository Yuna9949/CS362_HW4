import unittest
from Q3_name import Q3_name

class test_Q3(unittest.TestCase):
    def test_isStr(self):
        self.assertTrue(type(Q3_name.name_print()) is not str)

    def test_isEmpty(self):
        nameTemp = Q3_name.name_print()
        self.assertTrue(nameTemp[0:1] is not ' ')
        lnth = len(nameTemp)
        self.assertTrue(nameTemp[lnth-1:lnth] is not ' ')

    def test_Exact(self):
        self.assertTrue(Q3_name.name_print() in "Yuna Oh")
