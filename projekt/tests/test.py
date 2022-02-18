import unittest

from mmpackage.file import greetings

class TestGreetings(unittest.TestCase):
    def test_greetings(self):
        result = greetings()
        self.assertEqual(result, "Hello")

if __name__ == '__main__':
    unittest.main()
