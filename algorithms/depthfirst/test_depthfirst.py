import unittest

from .depthfirst import depth_first_search


class TestDepthFirstSearch(unittest.TestCase):

    def setUp(self):
        self.adj_list = dict()
        self.adj_list[1] = [2, 4, 7]
        self.adj_list[2] = [3, 5, 8]
        self.adj_list[3] = [6]
        self.adj_list[4] = [7]
        self.adj_list[5] = [8, 9]
        self.adj_list[9] = [10]

    def test_dfs_can_visit_all_nodes(self):
        result = depth_first_search(self.adj_list)
        visited_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(result, visited_set)
