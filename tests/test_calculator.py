import unittest

from app.calculator import add, subtract, multiply


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(1, 1), 2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(7, 3), 21)

    def test_reject_zero(self):
        with self.assertRaises(ValueError):
            add(0, 5)

    def test_reject_negative_integer(self):
        with self.assertRaises(ValueError):
            subtract(5, -1)

    def test_reject_non_integer(self):
        with self.assertRaises(TypeError):
            multiply(2.5, 3)

    def test_reject_boolean(self):
        with self.assertRaises(TypeError):
            add(True, 5)


if __name__ == "__main__":
    unittest.main()
