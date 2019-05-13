from queue import Queue


class BTreeNode:
    serial_number = 1

    def __init__(self, t):
        assert t > 2, "the degree must greater then 2"
        self.degree = t
        self.n = 0
        self.leaf = True
        self.keys = [None] * t
        self.children = [None] * (t + 1)
        self.parent = None
        self.sn = BTreeNode.serial_number
        BTreeNode.serial_number += 1

    def is_full(self):
        return self.degree == self.n

    def set_leaf(self, b):
        self.leaf = b

    def is_leaf(self):
        return self.leaf

    def middle(self):
        assert self.is_full(), "node must full"
        mid = self.__middle()
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
        tr = "node_" + str(self.sn)
        tr += '[label=" '
        for i in range(0, self.n):
            tr += "<f%d>| <f%d>%d|" % (i*2, i*2+1, self.keys[i])

        return '%s<f%d>"]' % (tr, self.n * 2)

    def name(self):
        return "node_" + str(self.sn)

    def find_next(self, value):
        for i in range(0, self.n):
            if value < self.keys[i]:
                return i
        return self.n

    def find_pos(self, value):
        for i in range(0, self.n):
            if value == self.keys[i]:
                return i
        return None

    def remove(self, value):
        pos = self.find_pos(value)
        assert (self.is_leaf() and pos is not None), "remove value from node must be leaf"
        # move node
        for i in range(pos + 1, self.n):
            self.keys[i-1] = self.keys[i]
        self.keys[self.n-1] = None
        self.n -= 1

    # function for remove key
    def child_pos(self, child):
        for i in range(0, self.n+1):
            if self.children[i] is child:
                return i
        return None

    def is_low(self):
        """ the node capacity(n) is less the degree/2 (if degree is even, less then degree/2-1)"""
        mid = self.__middle()
        return self.n < mid

    def is_enough(self):
        """ the node capacity(n) is node borrow to sibling"""
        mid = self.__middle()
        return self.n > mid

    def left_sibling(self):
        assert (self.parent is not None), "parent must not be none"
        p = self.parent.child_pos(self)
        if p == 0 or p is None:
            return None
        return self.parent.children[p-1]

    def right_sibling(self):
        assert (self.parent is not None), "parent must not be none"
        p = self.parent.child_pos(self)
        if p == self.parent.n or p is None:
            return None
        return self.parent.children[p+1]

    def backward(self, pos):
        assert 0 <= pos <= self.n, "pos must between 0 and" + str(self.n)
        # move node behind position forward
        for i in range(pos, self.n - 1):
            self.keys[i] = self.keys[i+1]
        if not self.is_leaf():
            for i in range(pos, self.n):
                self.children[i] = self.children[i+1]
            self.children[self.n] = None
        self.keys[self.n-1] = None
        self.n -= 1

    def forward(self, pos):
        assert 0 <= pos <= self.n, "pos must between 0 and " + str(self.n)
        for i in range(pos, self.n):
            self.keys[i+1] = self.keys[i]
        if not self.is_leaf():
            for i in range(self.n+1, 0, -1):
                self.children[i] = self.children[i-1]
        self.n += 1

    def __middle(self):
        if self.degree % 2 == 0:
            mid = int(self.degree / 2) - 1
        else:
            mid = int(self.degree / 2)
        return mid

    def successor(self, pos):
        assert (not self.is_leaf()), "leaf have not successor"
        s = self.children[pos + 1]
        while s is not None and s.children[0] is not None:
            s = s.children[0]
        return s


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

                        idx = self.root.find_next(value)

                        node = self.root.children[idx]

                    else:
                        parent.add_key(mid, node, right)
                        idx = parent.find_next(value)
                        node = parent.children[idx]

                else:
                    if node.is_leaf():
                        node.add_key(value)
                        return
                    else:
                        idx = node.find_next(value)
                        node = node.children[idx]

    def print(self, name=None):
        if name is None:
            name = "BTree.gv"
        with open("F:\\b_tree\\" + name, 'w+') as f:
            f.write("digraph structs { node [shape=record];\n")
            if self.root is None:
                f.write("}")
                return

            q = Queue()
            q.put(self.root)

            while not q.empty():
                current = q.get()
                if current is None:
                    return

                n = current.print()
                f.write(n + "\n")

                name = current.name()

                for i in range(0, current.n+1):
                    c = current.children[i]
                    if c is not None:
                        f.write("%s:f%d -> %s\n" % (name, 2*i, c.name()))
                        q.put(c)
            f.write("}")

    def split(self, node):
        right = BTreeNode(self.degree)
        right.set_leaf(node.is_leaf())

        if self.degree % 2 == 0:
            middle = int(self.degree / 2) - 1
        else:
            middle = int(self.degree / 2)
        node.n = middle

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
        node = self.root
        if self.root is None:
            return None

        while not node.is_leaf():
            num = node.n
            for i in range(0, num):
                if value < node.keys[i]:
                    node = node.children[i]
                    break
                elif value == node.keys[i]:
                    return node
            else:
                node = node.children[num]
        return node

    @staticmethod
    def merge(left_node, right_node, parent_node, parent_pos):
        left_node.keys[left_node.n] = parent_node.keys[parent_pos]
        left_node.n += 1
        # children must move first
        if not left_node.is_leaf() and not right_node.is_leaf():
            for i in range(0, right_node.n + 1):
                left_node.children[left_node.n + i] = right_node.children[i]
                left_node.children[left_node.n + i].parent = left_node
        for i in range(0, right_node.n):
            left_node.keys[left_node.n] = right_node.keys[i]
            left_node.n += 1

        left = parent_node.children[parent_pos]
        parent_node.backward(parent_pos)
        parent_node.children[parent_pos] = left
        # del right_node
        # if parent_node.is_low():
        #     parent_pos = parent_node.parent.find_next(parent_node.keys[0])
        #     parent_node = parent_node.parent

    def fix_remove(self, node):
        while node is not self.root:
            if node is self.root or not node.is_low():
                return

            left_sibling = node.left_sibling()
            if left_sibling is not None and left_sibling.is_enough():
                # change value
                # parent value to node first, left node right most value to to parent
                parent = node.parent
                parent_pos = parent.child_pos(node) - 1
                node.forward(0)
                if not node.is_leaf():
                    node.children[0] = left_sibling.children[left_sibling.n]
                    node.children[0].parent = node
                    left_sibling.children[left_sibling.n] = None
                node.keys[0] = parent.keys[parent_pos]
                parent.keys[parent_pos] = left_sibling.keys[left_sibling.n - 1]
                left_sibling.keys[left_sibling.n - 1] = None
                left_sibling.n -= 1
                return
            right_sibling = node.right_sibling()
            if right_sibling is not None and right_sibling.is_enough():
                # change value
                # parent value to left node left most, right node first to parent
                parent = node.parent
                parent_pos = parent.child_pos(node)
                node.keys[node.n] = parent.keys[parent_pos]
                node.n += 1
                parent.keys[parent_pos] = right_sibling.keys[0]
                if not node.is_leaf():
                    node.children[node.n] = right_sibling.children[0]
                    node.children[node.n].parent = node
                right_sibling.backward(0)
                return
            # left sibling and right sibling all is low then should merge
            parent = node.parent
            parent_pos = parent.child_pos(node)
            if left_sibling is not None:
                # parent_pos is point to right node
                self.merge(left_sibling, node, parent, parent_pos - 1)
                left_node = left_sibling
            else:
                # parent_pos is point to left node
                self.merge(node, right_sibling, parent, parent_pos)
                left_node = node

            if parent is self.root and self.root.n == 0:
                # up to the root
                self.root = left_node
                node = self.root
            else:
                node = parent

    def remove(self, value):
        node = self.find(value)

        if node is not None:
            if node.is_leaf():
                p = node.find_pos(value)
                # not find in tree
                if p is None:
                    return
                if node is self.root:
                    if self.root.n == 1:
                        self.root = None
                    else:
                        self.root.remove(value)
                    return
                node.remove(value)

                self.fix_remove(node)
            else:
                pos = node.find_pos(value)
                s = node.successor(pos)
                value = s.keys[0]
                node.keys[pos] = value
                s.remove(value)
                self.fix_remove(s)

