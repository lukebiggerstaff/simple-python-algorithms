import unittest

from .mergesort import mergesort


class TestMergeSort(unittest.TestCase):

    def test_mergesort_can_sort(self):
        list_ = [55, 2, 8, 99, 101, 22, 34]
        r = mergesort(list_)
        self.assertEqual(r, [2, 8, 22, 34, 55, 99, 101])
