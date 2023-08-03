import unittest

class TestSum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum(1, 2), 3)

    def test_negative_numbers(self):
        self.assertEqual(sum(-1, -2), -3)

    def test_zero(self):
        self.assertEqual(sum(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
