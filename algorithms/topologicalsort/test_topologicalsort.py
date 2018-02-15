import unittest

from .topologicalsort import topological_sort


class TestTopologicalSort(unittest.TestCase):

    def test_can_top_sort_find_path(self):
        graph = dict()
        graph[1] = {2, 3}
        graph[2] = {3, 6}
        graph[3] = {4, 7}
        graph[6] = {10}
        graph[7] = {9}
        result = topological_sort(graph)
        # now check that all depdendent verticies
        # come after their dependency
        self.assertTrue(result.index(1) > result.index(2))
        self.assertTrue(result.index(1) > result.index(3))
        self.assertTrue(result.index(2) > result.index(3))
        self.assertTrue(result.index(2) > result.index(6))
        self.assertTrue(result.index(3) > result.index(4))
        self.assertTrue(result.index(7) > result.index(9))
        self.assertTrue(result.index(6) > result.index(10))
