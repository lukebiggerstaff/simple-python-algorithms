'''
python tree traversal algorithms with Node class
'''


class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return '<Node data {}>'.format(self.data)


class PreOrderNode(Node):

    def __iter__(self):
        yield self
        if self.left is not None:
            yield from self.left
        if self.right is not None:
            yield from self.right


class InOrderNode(Node):

    def __iter__(self):
        if self.left is not None:
            yield from self.left
        yield self
        if self.right is not None:
            yield from self.right


class PostOrderNode(Node):

    def __iter__(self):
        if self.left is not None:
            yield from self.left
        if self.right is not None:
            yield from self.right
        yield self
