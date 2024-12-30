import csv
import os
import unittest
from unittest.mock import patch

from freezegun import freeze_time

from generate_csv import enter_products, get_filename, write_csv
from utils.product import Product


class TestGenerateCsv(unittest.TestCase):
    @patch('builtins.input')
    def test_process_data(self, mock_inputs):
        """
        Test the correct functioning of the `enter_products` function, simulating some inputs and checking the type of
        object it returns.
        """
        mock_inputs.side_effect = [
            'Mouse', 'a mouse for test purposes', '10', '1',
            'PC', '', '300', '1'
        ]
        products = enter_products(2)

        self.assertIsInstance(products, list, 'Expected that the function returns a list')

        actual = len(products)
        expected = 2
        self.assertEqual(actual, expected, 'Expected that the returned list has 2 elements')

        # check that the elements in the returned list are `Product` instances
        for p in products:
            self.assertIsInstance(p, Product)

    @freeze_time('2024-12-30 11:14:00')
    def test_get_filename(self):
        """
        Test that the method generates the expected file name.
        """
        actual = get_filename()
        expected = 'products_12302024_111400.csv'
        self.assertEqual(actual, expected, 'Expected a different filename')

    @staticmethod
    def get_products():
        """
        Returns a list of `Product` instances to use for testing purposes.
        """
        p = Product('mouse', 'a mouse for test purposes')
        p.quantity = 1
        p.price = 10.0
        return [p, ]

    @patch('generate_csv.get_filename')
    def test_write_csv(self, mock_get_filename):
        """
        Test the correct functioning of the `write_csv` function by checking the lines of the generated csv.
        """
        # mock filename
        tempfile_path = 'products_12302024_111400.csv'
        mock_get_filename.return_value = tempfile_path

        # mock products
        products = self.get_products()
        write_csv(products)

        # check lines of generated csv
        with open(tempfile_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile)

            actual = [l for l in csvreader]
            expected = [['name', 'description', 'price', 'quantity'], ['mouse', 'a mouse for test purposes', '10.0', '1']]

            self.assertEqual(actual, expected, 'Different lines expected in csv')

        # remove generated file
        os.remove(tempfile_path)
