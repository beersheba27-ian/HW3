import unittest
from functions import *


class IndexOfTests(unittest.TestCase):
    def test_repeated_value(self):
        self.assertEqual(indexOf([10, 20, 30, 20, -1], 20), 1)

    def test_first_element(self):
        self.assertEqual(indexOf([10, 20, 30, 20, -1], 10), 0)

    def test_last_element(self):
        self.assertEqual(indexOf([10, 20, 30, 20, -1], -1), 4)

    def test_repeated_value_at_start(self):
        self.assertEqual(indexOf([20, 10, 20, 30, 20, -1], 20), 0)

    def test_repeated_value_at_start_and_end(self):
        self.assertEqual(indexOf([20, 10, 20, 30, 20, -1, 20], 20), 0)

    def test_no_value(self):
        self.assertEqual(indexOf([10, 20, 30], 99), -1)

    def test_empty_list(self):
        self.assertEqual(indexOf([], 10), -1)


class LastIndexOfTests(unittest.TestCase):
    def test_repeated_value(self):
        self.assertEqual(lastIndexOf([10, 20, 30, 20, -1], 20), 3)

    def test_first_element(self):
        self.assertEqual(lastIndexOf([10, 20, 30, 20, -1], 10), 0)

    def test_last_element(self):
        self.assertEqual(lastIndexOf([10, 20, 30, 20, -1], -1), 4)

    def test_repeated_value_at_start(self):
        self.assertEqual(lastIndexOf([20, 10, 20, 30, 20, -1], 20), 4)

    def test_repeated_value_at_start_and_end(self):
        self.assertEqual(lastIndexOf([20, 10, 20, 30, 20, -1, 20], 20), 6)

    def test_no_value(self):
        self.assertEqual(lastIndexOf([10, 20, 30], 99), -1)

    def test_empty_list(self):
        self.assertEqual(lastIndexOf([], 10), -1)


class MinEvenTests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(min_even([9, 4, 7, 2]), 2)

    def test_negative(self):
        self.assertEqual(min_even([-8, -3, -4, 5]), -8)

    def test_zero(self):
        self.assertEqual(min_even([5, 0, 3, 2]), 0)

    def test_single(self):
        self.assertEqual(min_even([6]), 6)


class CountTests(unittest.TestCase):
    def test_multiple(self):
        self.assertEqual(count([10, 20, 30, 20, -1], 20), 2)

    def test_single(self):
        self.assertEqual(count([10, 20, 30, 20, -1], 30), 1)

    def test_single_first(self):
        self.assertEqual(count([10, 20, 30, 20, -1], 10), 1)

    def test_single_negative(self):
        self.assertEqual(count([10, 20, 30, 20, -1], -1), 1)

    def test_no_value(self):
        self.assertEqual(count([1, 2, 3], 4), 0)

    def test_all(self):
        self.assertEqual(count([5, 5, 5], 5), 3)

    def test_empty_list(self):
        self.assertEqual(count([], 5), 0)


class SumOfTwoExistsTests(unittest.TestCase):
    def test_zero_sum(self):
        self.assertTrue(sumOfTwoExists([1, -1, 40, 50, 0], 0))
        
    def test_negative_sum(self):
        self.assertTrue(sumOfTwoExists([1, -1, 40, -50, 0], -10))

    def test_pair_positive_and_negative(self):
        self.assertTrue(sumOfTwoExists([1, -1, 40, 50, 0], 39))

    def test_pair_positives(self):
        self.assertTrue(sumOfTwoExists([1, -1, 40, 50, 0], 41))

    def test_pair_positive_and_zero(self):
        self.assertTrue(sumOfTwoExists([1, -1, 40, 50, 0], 50))

    def test_no_pair(self):
        self.assertFalse(sumOfTwoExists([1, -1, 40, 50, 0], 2))

    def test_short_list(self):
        self.assertTrue(sumOfTwoExists([1, 2, 3], 5))

    def test_two_equal_elements_true(self):
        self.assertTrue(sumOfTwoExists([3, 3], 6))

    def test_two_equal_elements_false(self):
        self.assertFalse(sumOfTwoExists([3, 3], 7))

    def test_two_non_equal_elements_true(self):
        self.assertTrue(sumOfTwoExists([4, 5], 9))

    def test_two_non_equal_elements_false(self):
        self.assertFalse(sumOfTwoExists([4, 5], 10))

    def test_one_element_false(self):
        self.assertFalse(sumOfTwoExists([1], 2))
        
    def test_empty_list_false(self):
        self.assertFalse(sumOfTwoExists([], 5))


if __name__ == "__main__":
    unittest.main()
