from unittest import TestCase
from calculator import Calculator, CalculationException

class CalculatorTests(TestCase):
    def test_setup(self):
        self.assertEqual(True, True)

    
    def test_empty_string(self):
        # arrange
        calculator = Calculator()

        # act
        result = calculator.calculate("")

        # assert
        self.assertEqual(0, result)

    def test_one_number_string(self):
        # arrange
        calculator = Calculator()

        # act
        result = calculator.calculate("1")

        # assert
        self.assertEqual(1, result)

    def test_two_numbers_string(self):
        # arrange
        calculator = Calculator()

        # act
        result = calculator.calculate("1,2")

        # assert
        self.assertEqual(3, result)

    def test_three_numbers_string(self):
        # arrange
        calculator = Calculator()

        # act
        result = calculator.calculate("1,2,3")

        # assert
        self.assertEqual(6, result)

    def test_number_parse_exception(self):
        # arrange
        calculator = Calculator()

        result = 0
        # act
        try:
            result = calculator.calculate("a")
            self.fail("Should not have got here")
        except CalculationException as ce:
            # assert
            self.assertNotEqual(None, ce)

        