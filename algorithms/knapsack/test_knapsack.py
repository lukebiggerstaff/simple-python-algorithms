import unittest

from .knapsack import knapsack


class TestKnapsack(unittest.TestCase):

    def test_knapsack_can_find_best_value(self):
        result = knapsack(
            [(1, 1), (3, 2), (2, 4)],
            4
        )
        expected = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 1, 1, 2, 3],
            [0, 1, 4, 5, 5]
        ]
        self.assertEqual(result, expected)
