import unittest
from bellman_ford import BellmanFord as Graph


class TestBellmanFord(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()
        self.graph.add('A', 'B', -1)
        self.graph.add('A', 'C', 4)
        self.graph.add('B', 'C', 3)
        self.graph.add('B', 'D', 2)
        self.graph.add('D', 'B', 1)
        self.graph.add('D', 'C', 5)
        self.graph.add('B', 'E', 2)
        self.graph.add('E', 'D', -3)

    def test_graph(self):
        self.graph.print()

    def test_solution(self):
        pass

    def test_show(self):
        pass
