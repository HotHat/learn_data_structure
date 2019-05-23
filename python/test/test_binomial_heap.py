import unittest
from binomial_heap import BinomialHeap


class TestBinomialHeap(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(1, 1)

    def test_world(self):
        self.assertEqual(1, 2)

    def test_push(self):
        heap = BinomialHeap()
        for i in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
            print("insert: %d" % i)
            heap.insert(i)
            heap.print()

        heap.extract_min()
        heap.print()

        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
