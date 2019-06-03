from redblacktree import RedBlackTree


class GraphNode:
    def __init__(self, start):
        self.item = start
        self.child = []

    def add_child(self, to):
        if to not in self.child:
            self.child.append(to)

    def __eq__(self, other):
        return self.item == other.item

    def __lt__(self, other):
        return self.item < other.item

    def __gt__(self, other):
        return self.item > other.item

    def __str__(self):
        return str(self.item)


class Graph:
    def __init__(self):
        self.node = RedBlackTree()

    def add(self, start, end):
        g = GraphNode(start)
        self.node.insert(g)
        g2 = GraphNode(end)
        self.node.insert(g2)
        p = self.node.find(g)
        p.add_child(g2)

    def find(self, node):
        pass

    def print(self):
        for i in self.node:
            print(i)


