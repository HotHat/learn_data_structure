from BTree import BTree, BTreeNode


if __name__ == "__main__":
    tree = BTree(3)

    arr = [100, 50, 30, 500, 600, 800, 200, 20, 150, 300, 550, 580, 5, 28, 922, 82, 68, 182, 832, 12, 32, 234]

    for i in arr:
        print("Insert %d" % i)
        tree.insert(i)
        tree.print()

    tree.print()
