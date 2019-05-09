from queue import Queue


class BTreeNode:
    def __init__(self, t):
        self.degree = t
        self.n = 0
        self.leaf = True
        self.keys = [None] * t
        self.children = [None] * (t + 1)
        self.parent = None

    def is_full(self):
        return self.degree == self.n

    def set_leaf(self, b):
        self.leaf = b

    def is_leaf(self):
        return self.leaf

    def middle(self):
        assert self.is_full(), "node must full"
        if self.degree % 2 == 0:
            mid = int(self.degree / 2) - 1
        else:
            mid = int(self.degree / 2)
        return self.keys[mid]

    def add_key(self, key, left=None, right=None):
        assert (not self.is_full()), "full node can't add key"
        self.keys[self.n] = key
        self.n = self.n + 1
        idx = self.__sort_key()
        if left is not None:
            self.children[idx] = left
            left.parent = self
        if right is not None:
            self.children[idx+1] = right
            right.parent = self

    def __sort_key(self):
        p = self.n - 1
        while p > 0 and (self.keys[p] < self.keys[p-1]):
            # sort key
            tmp = self.keys[p-1]
            self.keys[p-1] = self.keys[p]
            self.keys[p] = tmp
            # sort children
            if not self.is_leaf():
                tmp_c = self.children[p]
                self.children[p] = self.children[p+1]
                self.children[p+1] = tmp_c
            p -= 1
        return p

    def print(self):
        tr = "node_"
        for i in range(0, self.n):
            tr += str(self.keys[i])
        tr += '[label=" '
        for i in range(0, self.n):
            tr += "<f%d>| <f%d>%d|" % (i*2, i*2+1, self.keys[i])

        print('%s<f%d>"]' % (tr, self.n * 2))

    def name(self):
        tr = "node_"
        for i in range(0, self.n):
            tr += str(self.keys[i])
        return tr


class BTree:
    def __init__(self, t):
        self.root = None
        self.degree = t

    def insert(self, value):
        if self.root is None:
            self.root = BTreeNode(self.degree)
            self.root.add_key(value)
        else:
            node = self.root
            while True:
                if node.is_full():
                    parent = node.parent
                    mid = node.middle()
                    right = self.split(node)

                    if parent is None:
                        self.root = BTreeNode(self.degree)
                        self.root.add_key(mid, node, right)
                        self.root.set_leaf(False)

                        idx = self.__find_next(self.root, value)

                        node = self.root.children[idx]

                    else:
                        parent.add_key(mid, node, right)
                        idx = self.__find_next(parent, value)
                        node = parent.children[idx]

                else:
                    if node.is_leaf():
                        node.add_key(value)
                        return
                    else:
                        idx = self.__find_next(node, value)
                        node = node.children[idx]

    def print(self):
        print("digraph structs { node [shape=record];")
        if self.root is None:
            return

        q = Queue()
        q.put(self.root)
        while not q.empty():
            current = q.get()
            if current is None:
                return

            current.print()

            name = current.name()

            for i in range(0, current.n+1):
                c = current.children[i]
                if c is not None:
                    print("%s:f%d -> %s" % (name, 2*i, c.name()))
                    q.put(c)
        print("}")

    @staticmethod
    def __find_next(node, value):
        for i in range(0, node.n):
            if value < node.keys[i]:
                return i
        return node.n

    def split(self, node):
        right = BTreeNode(self.degree)
        right.set_leaf(node.is_leaf())

        if self.degree % 2 == 0:
            middle = int(self.degree / 2) - 1
        else:
            middle = int(self.degree / 2)
        node.n -= middle + 1

        index = 0
        # middle_value = node.keys[middle]
        node.keys[middle] = None

        for i in range(middle + 1, node.degree):
            right.keys[index] = node.keys[i]
            right.n += 1
            node.keys[i] = None
            index += 1

        index = 0
        for i in range(middle + 1, node.degree + 1):
            if node.children[i] is not None:
                right.children[index] = node.children[i]
                node.children[i].parent = right
                node.children[i] = None
            index += 1
        return right

        # if key > middle_value:
        #     right.add_key(key)
        # else:
        #     self.add_key(key)
        #
        # if self.parent is None:
        #     root = BTreeNode(self.degree)
        #     root.set_leaf(False)
        #     root.add_key(middle_value, self, right)
        #     self.parent = root
        #     right.parent = root
        #     return root
        # else:
        #     parent = self.parent
        #     parent.add_key(middle_value, self, right)

    def find(self, value):
        root = self.root

        while not root.is_leaf():
            num = root.n
            for i in range(0, num):
                if value < root.keys[i]:
                    root = root.children[i]
                    break
                elif value == root.keys[i]:
                    return None
            else:
                return root.children[num]
        return root

