
class GraphNode:
    def __init__(self, start):
        self.item = start
        self.child = []

    def add_child(self, to):
        if to not in self.child:
            self.child.append(to)


class Graph:
    def add(self, start, end):
        pass

    def find(self, node):
        pass

    def print(self):
        pass


