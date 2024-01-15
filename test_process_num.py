from process_num import process_numbers
import unittest

class TestProcessNumbers(unittest.TestCase):

    def test_with_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        total_sum, average, doubled_numbers = process_numbers(numbers)
        self.assertEqual(total_sum, 15)
        self.assertEqual(average, 3)
        self.assertEqual(doubled_numbers, [2, 4, 6, 8, 10])

    def test_with_empty_list(self):
        numbers = []
        total_sum, average, doubled_numbers = process_numbers(numbers)
        self.assertEqual(total_sum, 0)
        self.assertEqual(average, 0)
        self.assertEqual(doubled_numbers, [])

    def test_with_single_number(self):
        numbers = [5]
        total_sum, average, doubled_numbers = process_numbers(numbers)
        self.assertEqual(total_sum, 5)
        self.assertEqual(average, 5)
        self.assertEqual(doubled_numbers, [10])

if __name__ == '__main__':
    unittest.main()