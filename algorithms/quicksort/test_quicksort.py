import unittest

from .quicksort import quicksort


class TestQuickSort(unittest.TestCase):

    def test_quicksort_can_sort(self):
        list_ = [7, 2, 8, 22, 101, 9, 73]
        quicksort(list_)
        self.assertEqual(list_, [2, 7, 8, 9, 22, 73, 101])
