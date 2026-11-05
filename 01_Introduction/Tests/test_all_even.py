import unittest
from all_even import all_even

class Test_all_even(unittest.TestCase):
    def test_even(self):
        self.assertEqual(all_even([4, 90, 68, 6, -2]),True)
        self.assertEqual(all_even([30, 24, 2048, 0, 12, 50]),True)
        self.assertEqual(all_even([100]),True)
    def test_non_even(self):
        self.assertEqual(all_even([14, 40, 36, 3]),False)
        self.assertEqual(all_even([7, 7, 7, 7]) ,False)

if __name__ == "__main__":
    unittest.main()