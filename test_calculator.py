import unittest
from calculator_module import Calculator  # Import your calculator module

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Initialize the calculator object
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtraction(self):
        result = self.calculator.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiplication(self):
        result = self.calculator.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_division(self):
        result = self.calculator.divide(10, 5)
        self.assertEqual(result, 2)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(15, 0)

if __name__ == '__main__':
    unittest.main()
