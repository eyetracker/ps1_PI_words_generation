import unittest
from PI_Words.PI import simple

class TestUtils(unittest.TestCase):

    def test_adder(self):
        self.assertEqual(simple.adder(1,1), 2)
        self.assertEqual(simple.adder(1,1), 3)

    def test_substractor(self):
        self.assertEqual(simple.substractor(1,1), 0)
        # self.assertEqual(simple.substractor(1,1), 2)

if __name__ == "__main__":
    unittest.main()
