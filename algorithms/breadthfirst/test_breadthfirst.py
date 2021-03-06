import unittest

from .breadthfirst import breadth_first_search


class TestBFS(unittest.TestCase):

    def setUp(self):
        self.adj_list = dict()
        self.adj_list[1] = [2, 4, 7]
        self.adj_list[2] = [3, 5, 8]
        self.adj_list[3] = [6]
        self.adj_list[4] = [7]
        self.adj_list[5] = [8, 9]
        self.adj_list[9] = [10]

    def test_bfs_can_search(self):
        result = breadth_first_search(self.adj_list)
        visited_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(result, visited_set)
