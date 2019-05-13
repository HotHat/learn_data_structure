from BTree import BTree
from queue import Queue
from random import randint


if __name__ == "__main__":
    tree = BTree(3)

    arr = [247,  555,  739,  918,  323,  243,  150,  37,  401,  859,  665,  61,  115,  644,  543,  265,
           302,  544,  843, 991]
    print(len(arr))
    for i in arr:
        print("Insert %d" % i)
        tree.insert(i)
    tree.print()

    idx = 1
    for i in arr:
        print("Delete: %d" % i)
        if i == 861 or i == 859:
            tree.remove(i)
        else:
            tree.remove(i)
        tree.print(str(idx) + "_" + str(i) + ".gv")
        idx += 1

    # q = Queue()
    # for i in range(1000, 0, -1):
    #     n = randint(1, 1000)
    #     q.put(n)
    #     print("%d, " % n, end=" ")
    #     tree.insert(n)
    # tree.print()
    # print("Begin Remove Item(%d): " % q.qsize())
    # idx = 1
    # while not q.empty():
    #     p = q.get()
    #     print("delete %d" % p)
    #     tree.remove(p)
    #     tree.print(str(idx) + "_" + str(p) + ".gv")
    #     idx += 1


