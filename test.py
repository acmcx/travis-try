import unittest
from hello import hello, goodbye

class TestHello(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "Hello, World!")

    def test_goodbye(self):
        self.assertEqual(goodbye(), 2)

    def test_wrong(self):
        self.assertEqual(hello(), goodbye())

if __name__ == "__main__":
    unittest.main()
