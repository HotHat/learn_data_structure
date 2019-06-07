from binomial_heap import BinomialHeap
from queue import Queue


class DJKNode:
    def __init__(self, n, w=0, parent=None):
        self.number = n
        self.weight = w
        self.parent = parent

    def __str__(self):
        if self.parent is not None:
            return "%s_%s_%s" % (str(self.number), str(self.weight), str(self.parent))
        else:
            return "%s_%s" % (str(self.number), str(self.weight))
        # return "%d" % self.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight


class DJKHeap(BinomialHeap):
    def find(self, node):
        if self.root is None:
            return None

        q = Queue()
        s = BinomialHeap.get_sibling(self.root)
        for i in s:
            q.put(i)

        while not q.empty():
            n = q.get()
            if n.value.number == node.number:
                return n
            else:
                c = self.get_child(n)
                for i in c:
                    q.put(i)
        return None

