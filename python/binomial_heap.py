from queue import Queue


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
        return "s%d_%d" % (self.sn, self.value)

    def print(self):
        q = Queue()
        if self is not None:
            q.put(self)

        while not q.empty():
            p = q.get()
            start = p
            s = []
            while start is not None:
                s.append(start.name())
                start = start.sibling
            for i in s:
                print(i)
            if len(s) > 1:
                print("{rank=same; %s}" % " ".join(s))
            start = p
            while start is not None:
                s = start.sibling
                if start.child is not None:
                    print("%s -> %s" % (start.name(), start.child.name()))
                    q.put(start.child)
                if s is not None:
                    print("%s -> %s" % (start.name(), s.name()))
                start = start.sibling


class BinomialHeap:
    def __init__(self):
        self.root = BinomialNode(None)
        self.mini = None

    def push(self, value):
        node = BinomialNode(value)
        p = self.root
        if p.sibling is None:
            self.root.sibling = node
            self.mini = node
        else:
            node.sibling = p.sibling
            self.root.sibling = node
        self.__fix_push()

    def pop(self):
        pass

    def merge(self, other):
        pass

    def decrease(self, key):
        pass

    def print(self):
        print("digraph structs { ")
        if self.root.sibling is not None:
            self.root.sibling.print()
        print("}")

    def __fix_push(self):
        assert self.root.sibling is not None, "root must not be None"
        father = self.root
        point = father.sibling
        while point is not None:
            sibling = point.sibling

            if sibling is None:
                break

            if point.degree < sibling.degree:
                break

            # change position
            elif sibling.degree < point.degree:
                father.sibling = sibling
                tmp = sibling.sibling
                sibling.sibling = point
                point.sibling = tmp
                father = sibling
            # union
            elif sibling.degree == point.degree:
                self.__union(father, point, sibling)
                point = father.sibling

    @staticmethod
    def __union(father, left, right):
        if left.value > right.value:
            father.sibling = right
            left.sibling = right.child
            right.child = left
            right.degree += 1
        else:
            left.sibling = right.sibling
            right.sibling = left.child
            left.child = right
            left.degree += 1


