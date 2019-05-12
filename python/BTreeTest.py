from BTree import BTree
from queue import Queue
from random import randint


if __name__ == "__main__":
    tree = BTree(3)

    arr = [100, 50, 30, 510, 600, 500, 200, 201, 150, 300, 550, 580, 5, 28, 922, 82, 68, 182, 832, 234]

    for i in arr:
        # print("Insert %d" % i)
        tree.insert(i)
    # tree.print()
# q = Queue()
    # for i in range(50, 0, -1):
    #     n = randint(1, 100)
    #     q.put(n)
    #     # print("%d, " % n, end=" ")
    #     tree.insert(n)
    tree.print()
    for i in [500, 550, 300, 580, 600, 510, 234, 201, 150, 182, 200]:
        print("Delete: %d" % i)
        tree.remove(i)
        tree.print()


