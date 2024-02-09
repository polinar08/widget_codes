import unittest
from Widget_functions.utilis import load_operations, sort_operations, filter_operations, take_first_n_operations, \
    formatter_date, formatter_from, formatter_to


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.test_filename = 'operations.json'

    def test_load_operations(self):
        operations = load_operations(self.test_filename)
        self.assertEqual(len(operations), 15)

    def test_sort_operations(self):
        operations = load_operations(self.test_filename)
        sorted_operations = sort_operations(operations)
        self.assertEqual(sorted_operations[0]['date'],
                         '2019-12-08T22:46:21.935582')

    def test_filter_operations(self):
        operations = load_operations(self.test_filename)
        filtered_operations = filter_operations(operations)
        self.assertTrue(all(operation['state'] == 'EXECUTED' for operation in
                            filtered_operations))

    def test_take_first_n_operations(self):
        operations = load_operations(self.test_filename)
        first_operations = take_first_n_operations(operations, 5)
        self.assertEqual(len(first_operations), 5)

    def test_formatter_date(self):
        formatted_date = formatter_date('2019-07-03T18:35:29.512364')
        self.assertEqual(formatted_date, '03.07.2019')

    def test_formatter_from(self):
        formatted_from = formatter_from('MasterCard 7158300734726758')
        self.assertEqual(formatted_from, 'Master ****** 6758')

    def test_formatter_to(self):
        formatted_to = formatter_to('Счет 35383033474447895560')
        self.assertEqual(formatted_to, '**5560')


if __name__ == '__main__':
    unittest.main()
