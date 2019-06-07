from undirected_graph import UndirectedGraph
from djk_heap import DJKHeap, DJKNode


class Dijkstra:
    def __init__(self):
        self.graph = UndirectedGraph()
        self.heap = DJKHeap()

    def add(self, start, to=None, weight=None):
        self.graph.add(start, to, weight)

    def solution(self, start):
        for i in self.graph:
            # print(i)
            if i.item != start:
                self.heap.insert(DJKNode(i.item, float('Infinity')))
            else:
                self.heap.insert(DJKNode(i.item, 0))
            # for j in i.child:
            #     # if i.item == start:
            #     mn = min(i.item, j.value)
            #     mx = max(i.item, j.value)
            #     s.add((mn, mx, j.weight))
                # else:
                #     s.add((i.item, j.value, 0))

            # print('------------------------')
        # self.heap.print()
        # self.heap.print()
        result = []
        while not self.heap.empty():
            m = self.heap.get_min()
            result.append(m)
            f = self.graph.find(m.number)
            assert (f is not None), 'must find the node'
            for i in f.child:
                n = m.weight + i.weight
                p = self.heap.find(DJKNode(i.value, i.weight))
                if p is not None:
                    hp = p.value
                    if n < hp.weight:
                        hp.parent = m.number
                        hp.weight = n
                        self.heap.decrease(hp, hp)
            self.heap.extract_min()

        for i in result:
            print(i)

    # print the solution
    def show(self):
        pass

    # print the graph
    def print(self):
        self.graph.print()
