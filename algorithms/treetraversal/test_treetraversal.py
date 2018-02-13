import unittest

from .treetraversal import PreOrderNode, InOrderNode, PostOrderNode


class TestTreeTraversal(unittest.TestCase):

    def test_preorder_visits_nodes_in_correct_order(self):
        n = PreOrderNode(5)
        n.left = PreOrderNode(1)
        n.right = PreOrderNode(7)
        n2 = n.left
        n2.left = PreOrderNode(0)
        n2.right = PreOrderNode(3)
        n2.right.left = PreOrderNode(2)
        n2.right.right = PreOrderNode(4)
        n3 = n.right
        n3.left = PreOrderNode(6)
        n3.right = PreOrderNode(8)
        node_list = list()
        for node in n:
            node_list.append(node.data)
        result = [5, 1, 0, 3, 2, 4, 7, 6, 8]
        self.assertEqual(node_list, result)

    def test_inorder_visits_nodes_in_correct_order(self):
        n = InOrderNode(5)
        n.left = InOrderNode(1)
        n.right = InOrderNode(7)
        n2 = n.left
        n2.left = InOrderNode(0)
        n2.right = InOrderNode(3)
        n2.right.left = InOrderNode(2)
        n2.right.right = InOrderNode(4)
        n3 = n.right
        n3.left = InOrderNode(6)
        n3.right = InOrderNode(8)
        node_list = list()
        for node in n:
            node_list.append(node.data)
        result = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(node_list, result)

    def test_postorder_visits_nodes_in_correct_order(self):
        n = PostOrderNode(5)
        n.left = PostOrderNode(1)
        n.right = PostOrderNode(7)
        n2 = n.left
        n2.left = PostOrderNode(0)
        n2.right = PostOrderNode(3)
        n2.right.left = PostOrderNode(2)
        n2.right.right = PostOrderNode(4)
        n3 = n.right
        n3.left = PostOrderNode(6)
        n3.right = PostOrderNode(8)
        node_list = list()
        for node in n:
            node_list.append(node.data)
        result = [0, 2, 4, 3, 1, 6, 8, 7, 5]
        self.assertEqual(node_list, result)
