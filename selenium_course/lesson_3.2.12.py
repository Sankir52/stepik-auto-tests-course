# unittest
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self1, iii=-42):
        self1.assertEqual(abs(-42), iii, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()