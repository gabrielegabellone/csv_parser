import unittest
from unittest.mock import patch

from utils.product import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product()

    @patch('builtins.input')
    def test_choose_name(self, mock_inputs):
        """
        Test the correct functioning of the `choose_name` function, simulating some inputs.
        """
        chosen_name = 'Mouse'
        mock_inputs.side_effect = [chosen_name, ]
        self.product.choose_name()

        actual = self.product.name
        expected = chosen_name
        self.assertEqual(actual, expected)

    def test_set_empty_product_name(self):
        """
        Test that when an empty string is set to the `name` attribute an `AttributeError` exception is raised.
        """
        empty_strings = ['', '   ', ' ']
        for empty_string in empty_strings:
            with self.assertRaises(AttributeError):
                self.product.name = empty_string


    @patch('builtins.input')
    def test_choose_description(self, mock_inputs):
        """
        Test the correct functioning of the `choose_description` function, simulating some inputs.
        """
        chosen_description = 'Mouse for test purposes'
        mock_inputs.side_effect = [chosen_description, ]
        self.product.choose_description()

        actual = self.product.description
        expected = chosen_description
        self.assertEqual(actual, expected)

    @patch('builtins.input')
    def test_choose_price(self, mock_inputs):
        """
        Test the correct functioning of the `choose_price` function, simulating some inputs.
        """
        chosen_price = '10'
        mock_inputs.side_effect = [chosen_price, ]
        self.product.choose_price()

        actual = self.product.price
        expected = 10.0
        self.assertEqual(actual, expected)

    def test_set_price_lower_than_the_minimum_allowed(self):
        """
        Test that when a value lower than the minimum allowed is set to the `price` attribute an `AttributeError`
        exception is raised.
        """
        minimum_price = 0.05
        with self.assertRaises(AttributeError):
            self.product.price = minimum_price - 1

    @patch('builtins.input')
    def test_choose_quantity(self, mock_inputs):
        """
        Test the correct functioning of the `choose_quantity` function, simulating some inputs.
        """
        chosen_quantity = '1'
        mock_inputs.side_effect = [chosen_quantity, ]
        self.product.choose_quantity()

        actual = self.product.quantity
        expected = 1
        self.assertEqual(actual, expected)

    def test_set_quantity_lower_than_the_minimum_allowed(self):
        """
        Test that when a value lower than the minimum allowed is set to the `quantity` attribute an `AttributeError`
        exception is raised.
        """
        with self.assertRaises(AttributeError):
            self.product.quantity = -1
