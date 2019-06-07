from queue import Queue
import math


class BinomialNode:
    serial_number = 1

    def __init__(self, value):
        self.parent = None
        self.sibling = None
        self.child = None
        self.degree = 0
        self.value = value
        self.sn = BinomialNode.serial_number
        BinomialNode.serial_number += 1

    def name(self):
        return "s%d_%s" % (self.sn, str(self.value))

    def print(self):
        q = Queue()
        if self is not None:
            q.put(self)

        while not q.empty():
            root = q.get()
            idx = root
            s = []
            while idx is not None:
                s.append(idx.name())
                sb = idx.sibling
                if sb is not None:
                    q.put(sb)
                    if idx.parent is None:
                        print("%s -> %s" % (idx.name(),  sb.name()))
                idx = sb

            for i in s:
                print(i)

            if len(s) > 1:
                print("{rank=same; %s}" % " ".join(s))

            # children
            c = root.child
            if c is not None:
                s2 = []
                while c is not None:
                    s2.append(c.name())
                    q.put(c)
                    c = c.sibling
                if len(s2) > 1:
                    print("{rank=same; %s}" % " ".join(s2))
                for i in s2:
                    print("%s -> %s" % (root.name(),  i))


class BinomialHeap:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = BinomialNode(value)
        self.__union(self.root, node)

    def get_min(self):
        m = self.__find_min()
        if m is not None:
            return m.value
        else:
            return None

    def empty(self):
        return self.root is None

    def extract_min(self):
        m = self.__find_min()
        if m is None:
            return
        self.__extract_min_node(m)

    def decrease(self, old, new):
        t = self.find(old)
        if t is None:
            return False

        t.value = new
        self.__bubble_up(t, False)
        return True

    def delete(self, key):
        p = self.find(key)
        if p is None:
            return
        m = self.__bubble_up(p, True)

        self.__extract_min_node(m)

    def find(self, value):
        if self.root is None:
            return None

        q = Queue()
        s = self.get_sibling(self.root)
        for i in s:
            q.put(i)

        while not q.empty():
            n = q.get()
            if n.value == value:
                return n
            elif n.value < value:
                c = self.get_child(n)
                for i in c:
                    q.put(i)
        return None

    @staticmethod
    def get_sibling(n):
        r = []
        while n is not None:
            r.append(n)
            n = n.sibling
        return r

    def get_child(self, n):
        if n is None or n.child is None:
            return []
        else:
            return self.get_sibling(n.child)

    @staticmethod
    def __link(h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        if h1.degree <= h2.degree:
            root = h1
        else:
            root = h2
        while h1 is not None and h2 is not None:
            if h1.degree <= h2.degree:
                s = h1.sibling
                if h1.degree == h2.degree or s is None or s.degree > h2.degree:
                    tmp = h1.sibling
                    h1.sibling = h2
                    h1 = h2
                    h2 = tmp
                else:
                    h1 = s
            elif h1.degree > h2.degree:
                tmp = h2
                h2 = h1
                h1 = tmp

        return root

    def print(self):
        print("strict digraph binomial_heap{ ")
        if self.root is not None:
            self.root.print()
        print("}")

    def __find_pre(self, n):
        p = self.root
        if p is n:
            return p
        while p.sibling is not n:
            p = p.sibling
        return p

    def __find_min(self):
        if self.root is None:
            return None
        x = self.root
        y = self.root
        while x is not None:
            if x .value < y.value:
                y = x
            x = x.sibling
        return y

    @staticmethod
    def __merge(h1, h2):
        assert (h1.degree == h2.degree), "degree must the same"
        h2.sibling = h1.child
        h1.child = h2
        h2.parent = h1
        h1.degree = h2.degree + 1

    def __union(self, h1, h2):
        self.root = self.__link(h1, h2)
        x = self.root
        f = x
        while x is not None:
            nxt = x.sibling
            if nxt is None:
                return

            if nxt.sibling is not None and nxt.sibling.degree == x.degree:
                x = nxt
            elif x.degree == nxt.degree:
                if x.value <= nxt.value:
                    x.sibling = nxt.sibling
                    self.__merge(x, nxt)
                else:
                    if x is self.root:
                        self.root = nxt
                        f = nxt
                    else:
                        f.sibling = nxt
                    self.__merge(nxt, x)
                    x = nxt
            else:
                if x is not self.root:
                    f = f.sibling
                x = nxt

    @staticmethod
    def __reverse(c):
        if c is None:
            return c

        stack = []
        m = c
        while m is not None:
            m.parent = None
            stack.append(m)
            m = m.sibling
        root = stack.pop()
        m = root
        while len(stack) > 0:
            n = stack.pop()
            m.sibling = n
            m = n
        m.sibling = None

        return root

    @staticmethod
    def __bubble_up(n, to_top):
        if to_top:
            while n.parent is not None:
                f = n.parent
                tmp = f.value
                f.value = n.value
                n.value = tmp
                n = f
        else:
            while n.parent is not None and n.value < n.parent.value:
                f = n.parent
                tmp = f.value
                f.value = n.value
                n.value = tmp
                n = f
        return n

    def __remove_node(self, n):
        assert (n is not None), "remove node must not None"
        assert (n.parent is None), "remove node must be root level"

        s = self.get_sibling(n.child)
        for i in s:
            i.parent = None

    def __extract_min_node(self, m):
        pre = self.__find_pre(m)
        if m is self.root:
            self.root = m.sibling
        else:
            pre.sibling = m.sibling
        m.sibling = None
        c = m.child
        self.__remove_node(m)
        r = self.__reverse(c)
        self.__union(self.root, r)

