from PI_Words.PI.PiGenerator import PiGenerator
import unittest

# class Test_PiGenerator(unittest.TestCase):
#
#     def test_basicPowerMod(self):
#         # 5^7 mod 23 = 17
#         self.assertEqual(PiGenerator.powerMod(5, 7, 23), 17)
#         # 2^2 mod 2 = 0
#         self.assertEqual(PiGenerator.powerMod(2, 2, 2), 0)

def test_basicPowerMod():
    # 5^7 mod 23 = 17
    assert PiGenerator.powerMod(7, 5, 23) == 17
    # 2^2 mod 2 = 0
    # assert PiGenerator.powerMod(2, 2, 2) == 0

def test_powerModNegativeInput():
    # If a < 0, b < 0, or m < 0, return -1.
    assert PiGenerator.powerMod(-5, 7, 23) == -1
    assert PiGenerator.powerMod(5, -7, 23) == -1
    assert PiGenerator.powerMod(5, 7, -23) == -1
    # int max ranges

def test_powerModMaxIntRanges():
    assert PiGenerator.powerMod(2, 30, 2) == 0
    assert PiGenerator.powerMod(2, 62, 2) == 0
    assert PiGenerator.powerMod(2, 92, 2) == 0
    assert PiGenerator.powerMod(2, 392, 2) == 0

    #TODO: Write more tests (Problem 1.a, 1.c)

def test_computePiInHex():
    pass
