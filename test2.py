import unittest

class TestSum2(unittest.TestCase):

    def test_large_numbers(self):
        self.assertEqual(sum(1000, 2000), 3000)

    def test_small_numbers(self):
        self.assertEqual(sum(-100, -200), -300)

    def test_fractional_numbers(self):
        self.assertEqual(sum(1.5, 2.5), 4)
