import unittest
from dijkstra import Dijkstra


class TestDijkstra(unittest.TestCase):
    def test_undirected_graph(self):
        djk = Dijkstra()
        djk.add(0, 1, 4)
        djk.add(0, 7, 8)

        # djk.add(1, 0, 4)
        djk.add(1, 2, 8)
        djk.add(1, 7, 11)

        # djk.add(2, 1, 8)
        djk.add(2, 8, 2)
        djk.add(2, 3, 7)
        djk.add(2, 5, 4)

        # djk.add(7, 0, 8)
        # djk.add(7, 1, 11)
        djk.add(7, 8, 7)
        djk.add(7, 6, 1)

        djk.add(6, 7, 1)
        djk.add(6, 8, 6)
        djk.add(6, 5, 2)

        # djk.add(8, 7, 7)
        # djk.add(8, 6, 6)
        # djk.add(8, 2, 2)

        # djk.add(5, 6, 2)
        # djk.add(5, 2, 4)
        djk.add(5, 3, 14)
        djk.add(5, 4, 10)

        # djk.add(3, 2, 7)
        # djk.add(3, 5, 4)
        djk.add(3, 4, 9)

        # djk.add(4, 3, 9)
        # djk.add(4, 5, 10)
        # djk.add(10, 3)

        # djk.print()
        djk.solution(1)
