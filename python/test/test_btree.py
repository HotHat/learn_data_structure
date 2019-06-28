import unittest
from btree import BTree
from random import randint


class TestBTree(unittest.TestCase):
    def test_insert(self):
        tree = BTree(5)

        # arr = [247, 555, 739, 918, 323, 243, 150, 37, 401, 859, 665, 61, 115, 644, 543, 265,
        #        302, 544, 843, 991]
        # print(len(arr))
        arr = []
        for i in range(100):
            n = randint(1, 1000)
            print("Insert %d" % i)
            arr.append(n)
            tree.insert(n)
        tree.print()

        # idx = 1
        # for i in arr:
        #     print("Delete: %d" % i)
        #     # if i == 861 or i == 859:
        #     #     tree.remove(i)
        #     # else:
        #     tree.remove(i)
        #     tree.print(str(idx) + "_" + str(i) + ".gv")
        #     idx += 1
