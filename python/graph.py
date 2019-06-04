from redblacktree import RedBlackTree


class Vertex:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


class Graph:
    class GraphVertex:
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

    def __init__(self):
        self.node = RedBlackTree()

    def add(self, start, end, weight=0):
        g = Graph.GraphVertex(start)
        self.node.insert(g)
        g2 = Graph.GraphVertex(end)
        self.node.insert(g2)
        p = self.node.find(g)
        p.value.add_child(Vertex(g2.item, weight))

    def find(self, node):
        pass

    def print(self):
        print("strict graph Tree {")
        for i in self.node:
            print(i)
            for s in i.child:
                print("%s -- %s [label=%s]" % (str(i), str(s.value), str(s.weight)))

        print("}")


