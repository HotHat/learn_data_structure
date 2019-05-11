from BTree import BTree
from queue import Queue
from random import randint


if __name__ == "__main__":
    tree = BTree(3)

    arr = [100, 50, 30, 510, 600, 500, 200, 200, 150, 300, 550, 580, 5, 28, 922, 82, 68, 182, 832, 234]

    for i in arr:
        # print("Insert %d" % i)
        tree.insert(i)
    tree.print()
# q = Queue()
    # for i in range(50, 0, -1):
    #     n = randint(1, 100)
    #     q.put(n)
    #     # print("%d, " % n, end=" ")
    #     tree.insert(n)
    tree.remove(500)
    # print()
    tree.print()
    tree.remove(550)
    tree.print()
    tree.remove(300)
    tree.print()
