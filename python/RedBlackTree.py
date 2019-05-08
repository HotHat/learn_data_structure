from enum import Enum
from queue import Queue
from random import randint


class Color(Enum):
    RED = 1
    BLACK = 2


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value
        self.color = Color.RED

    def uncle(self):
        assert (self.parent is not None)
        assert (self.parent.parent is not None)
        return self.parent.sibling()

    def is_left(self):
        assert(self.parent is not None)
        return self.parent.left == self

    def is_leaf(self):
        return self.left is None and self.right is None

    def sibling(self):
        assert(self.parent is not None)
        if self.is_left():
            return self.parent.right
        else:
            return self.parent.left


class RedBlackTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self.root.color = Color.BLACK
            return

        n = self.__search(value)

        if n is None:
            return
        new = Node(value)

        if n.value > value:
            n.left = new
        else:
            n.right = new

        new.parent = n
        self.__fix_rotate(new)

    def remove(self, value):
        v = self.find(value)

        while v is not None:
            if v.is_leaf():
                self.__fix_remove(v)
                return
            else:
                u = self.__successor(v)

                if u is not None:
                    self.__swap_value(v, u)
                    if u.is_leaf():
                        self.__fix_remove(u)
                        return
                    else:
                        v = u
                else:
                    self.__swap_value(v, v.left)
                    v = v.left

    def find(self, value):
        p = self.root
        while p is not None:
            if p.value == value:
                return p
            if p.value > value:
                p = p.left
            else:
                p = p.right
        return p

    def print(self):
        print("strict digraph Tree {")
        q = Queue()
        q.put(self.root)
        self.__recursive(q)
        print("}")

    @staticmethod
    def __successor(node):
        s = node.right
        while s is not None and s.left is not None:
            s = s.left
        return s

    @staticmethod
    def __remove_node(node):
        assert node is not None
        if node.parent is None:
            del node
            return
        if node.is_left():
            node.parent.left = None
        else:
            node.parent.right = None
        del node

    def __recursive(self, q):
        p = Queue()

        while not q.empty():
            current = q.get()
            if current is None:
                return

            print(" %d[" % current.value, end="")
            if current.color is Color.RED:
                print("color=red]")
            else:
                print("color=black]")

            if current.left is not None:
                p.put(current.left)
                print(" %d -> %d" % (current.value, current.left.value))
            if current.right is not None:
                p.put(current.right)
                print(" %d -> %d" % (current.value, current.right.value))

            if not p.empty():
                self.__recursive(p)

    def __search(self, value):
        p = self.root
        while p is not None:
            if p.value == value:
                return None

            if p.value > value:
                if p.left is not None:
                    p = p.left
                else:
                    return p
            else:
                if p.right is not None:
                    p = p.right
                else:
                    return p

    def __left_rotate(self, node):
        right = node.right

        if node is self.root:
            self.root = right
            right.parent = None
        else:
            if node.is_left():
                node.parent.left = right
            else:
                node.parent.right = right
            right.parent = node.parent

        node.right = right.left
        if right.left is not None:
            right.left.parent = node

        right.left = node
        node.parent = right

    def __right_rotate(self, node):
        left = node.left

        if node is self.root:
            self.root = left
            left.parent = None
        else:
            if node.is_left():
                node.parent.left = left
            else:
                node.parent.right = left

            left.parent = node.parent

        node.left = left.right
        if left.right is not None:
            left.right.parent = node

        left.right = node
        node.parent = left

    def __fix_rotate(self, node):
        if node == self.root:
            return

        point = node

        while point is not self.root:
            if point.parent.color is Color.BLACK:
                return

            uncle = point.uncle()

            if uncle is not None and uncle.color is Color.RED:
                parent = point.parent
                uncle.color = Color.BLACK
                parent.color = Color.BLACK
                if parent.parent is not self.root:
                    parent.parent.color = Color.RED
                point = parent.parent

            else:
                parent = point.parent
                if point.is_left():
                    if parent.is_left():
                        self.__swap_color(parent.parent, parent)
                        self.__right_rotate(parent.parent)
                    else:
                        self.__right_rotate(parent)
                        self.__swap_color(point.parent, point)
                        self.__left_rotate(point.parent)

                else:
                    if not parent.is_left():
                        self.__swap_color(parent.parent, parent)
                        self.__left_rotate(parent.parent)

                    else:
                        self.__left_rotate(parent)
                        self.__swap_color(point.parent, point)
                        self.__right_rotate(point.parent)

                return

    @staticmethod
    def __swap_color(l, r):
        assert (l is not None)
        assert (r is not None)
        tmp = l.color
        l.color = r.color
        r.color = tmp

    def __fix_remove(self, node):
        if node is self.root:
            self.root = None
            self.__remove_node(node)
            return

        if node.color == Color.RED:
            self.__remove_node(node)
            return

        point = node
        while point is not self.root:
            sibling = point.sibling()
            if sibling.color == Color.BLACK:
                if (sibling.left is None or sibling.left.color == Color.BLACK) and (
                        sibling.right is None or sibling.right.color == Color.BLACK):
                    parent = sibling.parent
                    if parent.color == Color.RED:
                        parent.color = Color.BLACK
                        sibling.color = Color.RED
                        break
                    else:
                        sibling.color = Color.RED
                        parent.color = Color.BLACK
                        point = parent
                if sibling.left is not None and sibling.left.color == Color.RED:
                    if sibling.is_left():
                        sibling.left.color = Color.BLACK
                        self.__swap_color(sibling, sibling.parent)
                        self.__right_rotate(point.parent)
                    else:
                        self.__swap_color(sibling, sibling.left)
                        self.__right_rotate(sibling)
                        s = point.sibling()
                        s.right.color = Color.BLACK
                        self.__swap_color(s, s.parent)
                        self.__left_rotate(s.parent)
                    break
                if sibling.right is not None and sibling.right.color == Color.RED:
                    if not sibling.is_left():
                        sibling.right.color = Color.BLACK
                        self.__swap_color(sibling, sibling.parent)
                        self.__left_rotate(sibling.parent)
                    else:
                        self.__swap_color(sibling, sibling.right)
                        self.__left_rotate(sibling)
                        s = point.sibling()
                        s.left.color = Color.BLACK
                        self.__swap_color(s, s.parent)
                        self.__right_rotate(s.parent)
                    break
            else:
                self.__swap_color(sibling, sibling.parent)
                if sibling.is_left():
                    self.__right_rotate(sibling.parent)
                else:
                    self.__left_rotate(sibling.parent)

        self.__remove_node(node)

    @staticmethod
    def __swap_value(l, r):
        assert(l is not None)
        assert(r is not None)
        tmp = l.value
        l.value = r.value
        r.value = tmp


if __name__ == "__main__":
    tree = RedBlackTree()
    q = Queue()
    # for i in range(10, 0, -1):
    #     n = randint(1, 100)
    #     q.put(n)
    #     print("%d, " % n, end=" ")
    #     tree.insert(n)
    #
    # print()
    arr = [53,  83,  48,  100,  28,  86,  21,  59,  2,  72]
    for i in arr:
        q.put(i)
        tree.insert(i)
    tree.print()
    print("Begin Remove Item: ")
    while not q.empty():
        p = q.get()
        print("delete %d" % p)
        tree.remove(p)
        tree.print()

    # tree.insert(7)
    # tree.insert(3)
    # tree.insert(18)
    # tree.insert(10)
    # tree.insert(22)
    # tree.insert(8)
    # tree.insert(11)
    # tree.insert(26)
    # tree.insert(2)
    # tree.insert(6)
    # tree.insert(13)
    #
    # tree.print()
    # tree.remove(18)
    # tree.print()
    # tree.remove(11)
    # tree.print()
    # tree.remove(3)
    # tree.print()
    # tree.remove(10)
    # tree.print()
    # tree.remove(22)
    # tree.print()
