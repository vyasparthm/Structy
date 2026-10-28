import unittest
from longest_word import longest_word

class Test_longest_word(unittest.TestCase):
    def testLongestWord(self):
        self.assertEqual(longest_word("Hello I am Steve Rogerss"), "Rogerss" )

if __name__ =="__main__":
    unittest.main()