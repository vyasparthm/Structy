import unittest
from max_value import max_value

class TestMaxValue(unittest.TestCase):
    def test_value(self):
        self.assertEqual(max_value([1,5,66,2,3]),66)

if __name__ =="__main__":
    unittest.main()