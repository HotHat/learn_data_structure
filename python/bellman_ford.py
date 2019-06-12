from directed_graph import DirectedGraph


class BellmanFord:
    def __init__(self):
        self.graph = DirectedGraph()

    def add(self, start, to=None, weight=None):
        self.graph.add(start, to, weight)

    def solution(self, start):
        pass

    # print the solution
    def show(self):
        pass

    # print the graph
    def print(self):
        self.graph.print()
