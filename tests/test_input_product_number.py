import unittest
from unittest.mock import patch

from utils.input_product_number import InputProductNumber


class TestInputProductNumber(unittest.TestCase):
    @patch('builtins.input')
    def test_enter_product_number(self, mock_input):
        """
        Test the correct functioning of the `enter_product_number` method by simulating some inputs.
        """
        mock_input.side_effect = ['two', '-1', '1']
        actual = InputProductNumber().enter_product_number()
        expected = 1
        self.assertEqual(actual, expected)
