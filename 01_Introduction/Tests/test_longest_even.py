import unittest
from longest_even_run import longest_even_run

class test_longest_even(unittest.TestCase):
    def testLongestEvenSequence(self):
        self.assertEqual(longest_even_run([1,2,3,4,6,7]),2)
        self.assertEqual(longest_even_run([1,2,3,4,6,7,8,10,4]),3)

if __name__ =="__main__":
    unittest.main()        