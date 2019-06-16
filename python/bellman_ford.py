from directed_graph import DirectedGraph
from redblacktree import RedBlackTree


class BellmanFord:
    class Vertex:
        def __init__(self, label, weight, father=None):
            self.label = label
            self.father = father
            self.weight = weight

        def __eq__(self, other):
            return self.label == other.label

        def __lt__(self, other):
            return self.label < other.label

        def __gt__(self, other):
            return self.label > other.label

        def __str__(self):
            return "label: %s weight: %s from: %s" % (self.label, str(self.weight), self.father)

    def __init__(self):
        self.graph = DirectedGraph()

    def add(self, start, to=None, weight=None):
        self.graph.add(start, to, weight)

    def solution(self, start):
        p = self.graph.find(start)

        # can't find start node, not solution
        if p is None:
            return None

        rb = RedBlackTree()

        ss = set()
        for i in self.graph:
            # init solution
            if i.item == p.item:
                rb.insert(BellmanFord.Vertex(i.item, 0))
            else:
                rb.insert(BellmanFord.Vertex(i.item, float('Infinity')))

            for j in i.child:
                ss.add((i.item, j.value, j.weight))

        cnt = len(ss) - 1
        for i in range(0, cnt):
            for (s, t, w) in ss:
                ns = rb.search(BellmanFord.Vertex(s, 0))
                nt = rb.search(BellmanFord.Vertex(t, 0))
                if ns.weight + w < nt.weight:
                    nt.weight = ns.weight + w
                    nt.father = ns.label

        result = []
        for i in rb:
            result.append((i.label, i.weight, i.father))

        return result

    # print the solution
    def show(self, start):
        result = self.solution(start)
        # ss = set()
        print("digraph Tree {")
        for (t, w, f) in result:
            if f is not None:
                print("%s -> %s [label=%s]" % (str(f), str(t), str(w)))

        print("}")

    # print the graph
    def print(self):
        self.graph.print()
