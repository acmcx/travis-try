import unittest

from hello import hello, goodbye, me_need_test

class TestHello(unittest.TestCase):

    def test_hello(self):
        h = hello()
        self.assertEqual(h, "Hello, World!")

    def test_goodbye(self):
        g = goodbye()
        self.assertEqual(g, 11)
    
    def test_me_need_test(self):
        i = me_need_test()
        self.assertEqual(i, 1)

if __name__ == "__main__":
    unittest.main()
