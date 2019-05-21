
class BinomialNode:
    def __init__(self, value):
        self.parent = None
        self.sibling = None
        self.child = None
        self.degree = 0
        self.value = value


class BinomialHeap:
    def __init__(self):
        self.root = None
        self.mini = None

    def push(self, value):
        node = BinomialNode(value)
        if self.root is None:
            self.root = node
            self.mini = node
        else:
            node.sibling = self.root
            self.root = node
        self.__fix_push(self.root)

    def pop(self):
        pass

    def merge(self, other):
        pass

    def decrease(self, key):
        pass

    def print(self):
        pass

    def __fix_push(self, node):
        pass

    def __union(self, left, right):
        pass
