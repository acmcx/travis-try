import unittest
from hello import hello, goodbye

class TestHello(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "Hello, World!")

    def test_goodbye(self):
        self.assertEqual(goodbye(), 11)

if __name__ == "__main__":
    unittest.main()
