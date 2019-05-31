import unittest
from binomial_heap import BinomialHeap


class TestBinomialHeap(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(1, 1)

    def test_world(self):
        self.assertEqual(1, 2)

    def test_push(self):
        heap = BinomialHeap()
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print("insert: %d" % i)
            heap.insert(i)
        heap.print()

        # heap.extract_min()
        # heap.print()
        # heap.extract_min()
        # heap.print()
        # heap.extract_min()
        # heap.print()

        heap.delete(5)
        heap.print()
        self.assertEqual(1, 1)

    def test_decrease(self):
        heap = BinomialHeap()
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print("insert: %d" % i)
            heap.insert(i)
        heap.print()
        import math
        heap.decrease(5, -math.inf)
        heap.print()

    def test_delete(self):
        heap = BinomialHeap()
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            # print("insert: %d" % i)
            heap.insert(i)
        heap.print()
        heap.delete(5)
        heap.print()

    def test_dup(self):
        heap = BinomialHeap()
        for i in [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]:
            # print("insert: %d" % i)
            heap.insert(i)
        heap.print()
        heap.delete(5)
        heap.print()

if __name__ == '__main__':
    unittest.main()
