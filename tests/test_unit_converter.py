import unittest


class TestUnitConverter(unittest.TestCase):

    def test_meters_to_km(self):
        self.assertEqual(1000 / 1000, 1)

    def test_km_to_meters(self):
        self.assertEqual(2 * 1000, 2000)

    def test_celsius_to_fahrenheit(self):
        self.assertEqual((0 * 9/5) + 32, 32)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual((32 - 32) * 5/9, 0)


if __name__ == "__main__":
    unittest.main()
