import asyncio
import io
import sys
import textwrap
import types
import unittest
from unittest.mock import patch, AsyncMock

from main import process_data, csv_reader, main


class TestMain(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.in_mem_csv = io.StringIO(textwrap.dedent("""\
        name,quantity,price
        mouse,1,10
        pc,1,300
        desk,1,80"""))

    async def test_process_data(self):
        """
        Test the `process_data` method by verifying that it prints the correct output, based on the data in the queue
        provided as a parameter to the function.
        """
        # asyncio Queue object creation
        queue = asyncio.Queue()
        stop_value = None
        csv_rows = ['first row', 'second row', 'third row', stop_value]

        for r in csv_rows:
            await queue.put(r)

        # capture the output in the console
        captured_output = io.StringIO()                 # Create StringIO.
        sys.stdout = captured_output                    # Redirect stdout.
        await process_data(queue)                       # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.

        # check the captured output
        actual = captured_output.getvalue()
        expected = 'Processing first row\nProcessing second row\nProcessing third row\n'

        self.assertEqual(actual, expected)

    async def test_csv_reader(self):
        """
        Test the correct functioning of the `csv_reader` function by verifying that it returns the correct elements
        in the generator based on the mocked csv.
        """
        # mock csv file
        with patch("builtins.open", return_value=self.in_mem_csv) as mock_file:
            # test generator function
            fake_file_path = 'path/to/open'
            rows = csv_reader(fake_file_path)

            self.assertIsInstance(rows, types.GeneratorType, 'Expected that the function returns a Generator object')

            actual = list(rows)
            expected = [
                {'name': 'mouse', 'quantity': '1', 'price': '10'},
                {'name': 'pc', 'quantity': '1', 'price': '300'},
                {'name': 'desk', 'quantity': '1', 'price': '80'}
            ]

            self.assertEqual(actual, expected, 'Elements produced by the generator do not correspond to those expected')

    @patch('main.process_data', new_callable=AsyncMock)
    @patch('main.csv_reader')
    async def test_main(self, mock_process_data, mock_csv_reader):
        """
        Test that the `process_data` and `csv_reader` functions are called during the execution of the `main` function.
        """
        # mock csv file
        with patch("builtins.open", return_value=self.in_mem_csv) as mock_file:
            fake_file_path = 'path/to/open'
            await main(fake_file_path)
            mock_process_data.assert_called_once()
            mock_csv_reader.assert_called_once()
