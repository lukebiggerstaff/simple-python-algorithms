import unittest

from .binarysearch import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_binary_search_finds_integer(self):
        arr = [1, 5, 8, 99, 101, 105, 1000]
        r1 = binary_search(5, arr)
        self.assertTrue(r1)
        r2 = binary_search(3, arr)
        self.assertFalse(r2)

    def test_recursive_binary_search_finds_integer(self):
        arr = [1, 5, 8, 99, 101, 105, 1000]
        r1 = binary_search(5, arr)
        self.assertTrue(r1)
        r2 = binary_search(3, arr)
        self.assertFalse(r2)
