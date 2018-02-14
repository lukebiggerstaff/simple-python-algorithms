import unittest

from .dijkstra import dijkstra


class TestDijkstra(unittest.TestCase):

    def setUp(self):
        self.adj_list = dict()
        self.adj_list[1] = {2: 2, 4: 1, 3: 4}
        self.adj_list[2] = {3: 3, 5: 1}
        self.adj_list[4] = {5: 3}
        self.adj_list[5] = {7: 3, 6: 3}

    def test_can_dijkstra_find_min_path(self):
        result = dijkstra(self.adj_list, 1)
        expected = dict()
        expected[1] = 0
        expected[2] = 2
        expected[3] = 4
        expected[4] = 1
        expected[5] = 3
        expected[6] = 6
        expected[7] = 6
        self.assertEqual(result, expected)
