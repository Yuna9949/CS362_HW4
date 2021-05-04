import unittest
from Q1_cube_volume import Q1_cube_volume

class test_Q1(unittest.TestCase):

    def test_isNumber(self):
        v = 5
        self.assertTrue(type(Q1_cube_volume.cubeVolume(v)) is float)

    def test_isNegative(self):
        self.assertGreaterEqual(Q1_cube_volume.cubeVolume(10), 0)
        
    def test_isExact(self):
        self.assertEqual(Q1_cube_volume.cubeVolume(3), 27)
