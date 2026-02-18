import unittest
from modules.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(5 + 3, 8)

    def test_subtraction(self):
        self.assertEqual(10 - 4, 6)

    def test_multiplication(self):
        self.assertEqual(6 * 7, 42)

    def test_division(self):
        self.assertEqual(8 / 2, 4)


if __name__ == "__main__":
    unittest.main()
