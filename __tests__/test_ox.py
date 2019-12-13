from unittest import TestCase
from ox import isRowFull

class Test(TestCase):
    def test_is_row_full_returns_false_on_empty_row(self):
        self.assertFalse(isRowFull([0, 0, 0]))
    def test_is_row_full_returns_false_if_row_contains_different_values(self):
        self.assertFalse(isRowFull([1, 2, 1]))
    def test_is_row_full_returns_true_if_row_contains_same_value(self):
        self.assertTrue(isRowFull([1, 1, 1]))
