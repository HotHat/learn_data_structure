import unittest
from undirected_graph import UndirectedGraph as Graph
from random import randint


class TestUndirectedGraph(unittest.TestCase):
    def test_graph(self):
        g = Graph()
        g.add(0, 1, 4)
        g.add(0, 7, 8)

        # g.add(1, 0, 4)
        g.add(1, 2, 8)
        g.add(1, 7, 11)

        # g.add(2, 1, 8)
        g.add(2, 8, 2)
        g.add(2, 3, 7)
        g.add(2, 5, 4)

        # g.add(7, 0, 8)
        # g.add(7, 1, 11)
        g.add(7, 8, 7)
        g.add(7, 6, 1)

        g.add(6, 7, 1)
        g.add(6, 8, 6)
        g.add(6, 5, 2)

        # g.add(8, 7, 7)
        # g.add(8, 6, 6)
        # g.add(8, 2, 2)

        # g.add(5, 6, 2)
        # g.add(5, 2, 4)
        g.add(5, 3, 14)
        g.add(5, 4, 10)

        # g.add(3, 2, 7)
        # g.add(3, 5, 4)
        g.add(3, 4, 9)

        # g.add(4, 3, 9)
        # g.add(4, 5, 10)
        # g.add(10, 3)

        g.print()
