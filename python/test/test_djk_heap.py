import unittest
from djk_heap import DJKHeap, DJKNode
from random import randint


class TestDJKHeap(unittest.TestCase):
    def test_djk_heap(self):
        heap = DJKHeap()
        for i in range(1, 11):
            n = randint(1, 100)
            node = DJKNode(i, n)
            heap.insert(node)

        heap.print()

        heap.decrease(DJKNode(1), DJKNode(1, 100))
        heap.print()

