# from PI_Words.PI.PiGenerator import PiGenerator
from PI_Words.PI.PiGenerator import PiGenerator
# import unittest
# import pytest

# class Test_PiGenerator(unittest.TestCase):
#
#     def test_basicPowerMod(self):
#         # 5^7 mod 23 = 17
#         self.assertEqual(PiGenerator.powerMod(5, 7, 23), 17)
#         # 2^2 mod 2 = 0
#         self.assertEqual(PiGenerator.powerMod(2, 2, 2), 0)

# Classic xUnit testing scheme (setup_module and teardown_module)
# def setup_module(module):
#     global pig
#     pig = PiGenerator()
# 
# def test_basicPowerMod():
#     assert pig.powerMod(7, 5, 23) == 17
#     # assert pig.powerMod(2, 2, 2) == 0

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
    assert PiGenerator.powerMod(2, 10392, 2) == 0
    assert PiGenerator.powerMod(2, 102232, 2) == 0 #md

    # TODO: Write more tests (Problem 1.a, 1.c)

def test_piDigit():
    assert PiGenerator.piDigit(0) == 3
    assert PiGenerator.piDigit(1) == 2
    assert PiGenerator.piDigit(2) == 4
    assert PiGenerator.piDigit(3) == 3
    assert PiGenerator.piDigit(4) == 15
    assert PiGenerator.piDigit(5) == 6
    assert PiGenerator.piDigit(6) == 10
    assert PiGenerator.piDigit(7) == 8
    assert PiGenerator.piDigit(8) == 8
    assert PiGenerator.piDigit(9) == 8
    assert PiGenerator.piDigit(10) == 5
    assert PiGenerator.piDigit(11) == 10
    assert PiGenerator.piDigit(12) == 3
    assert PiGenerator.piDigit(13) == 0
    assert PiGenerator.piDigit(14) == 8
    assert PiGenerator.piDigit(15) == 13
    assert PiGenerator.piDigit(16) == 3

def test_computePiInHex():
    assert PiGenerator.computePiInHex(0) == []
    assert PiGenerator.computePiInHex(1) == [3]
    assert len(PiGenerator.computePiInHex(16)) == 16
    assert PiGenerator.computePiInHex(16) == [3,2,4,3,15,6,10,8,8,8,5,10,3,0,8,13]

