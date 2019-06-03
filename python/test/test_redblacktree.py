import unittest
from redblacktree import RedBlackTree
from queue import Queue
from random import randint


class TestRedBlackTree(unittest.TestCase):
    def test_iter(self):
        tree = RedBlackTree()
        # q = Queue()
        # for i in range(10, 0, -1):
        for i in [4,  96,  33,  11,  5,  20,  83,  69,  93,  88, 10, 28, 39, 42, 50, 61, 72]:
            # n = randint(1, 100)
            # q.put(n)
            # print("%d, " % n, end=" ")
            tree.insert(i)
        tree.print()

        for i in tree:
            print(i)

