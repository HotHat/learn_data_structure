from redblacktree import RedBlackTree





class DirectedGraph:
    class DirectedGraphEdge:
        def __init__(self, value, weight):
            self.value = value
            self.weight = weight

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

    def __iter__(self):
        for i in self.node:
            yield i

    def add(self, start, end=None, weight=None):
        g = DirectedGraph.GraphVertex(start)
        self.node.insert(g)
        if end is not None:
            g2 = DirectedGraph.GraphVertex(end)
            self.node.insert(g2)
            # a --> b
            p = self.node.search(g)
            p.add_child(DirectedGraph.DirectedGraphEdge(g2.item, weight))

    def find(self, node):
        n = DirectedGraph.GraphVertex(node)
        r = self.node.find(n)
        if r is None:
            return r
        else:
            return r.value

    def print(self):
        print("strict digraph Tree {")
        for i in self.node:
            print(i)
            for s in i.child:
                if s.weight is not None:
                    print("%s -> %s [label=%s]" % (str(i), str(s.value), str(s.weight)))
                else:
                    print("%s -> %s" % (str(i), str(s.value)))

        print("}")


