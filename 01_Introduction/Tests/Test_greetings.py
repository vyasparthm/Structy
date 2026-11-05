import unittest as tst
from greetings import greet

class TestGreet(tst.TestCase):
    def test_name(self):
        self.assertEqual(greet('alvin'), "hey alvin")
    def test_empty_str(self):
        self.assertEqual(greet(""), "hey ")

if __name__ =="__main__":
    tst.main()