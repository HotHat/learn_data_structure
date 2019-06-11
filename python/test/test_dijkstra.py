import unittest
from dijkstra import Dijkstra


class TestDijkstra(unittest.TestCase):
    def setUp(self) -> None:
        self.djk = Dijkstra()
        self.djk.add(0, 1, 4)
        self.djk.add(0, 7, 8)

        # djk.add(1, 0, 4)
        self.djk.add(1, 2, 8)
        self.djk.add(1, 7, 11)

        # djk.add(2, 1, 8)
        self.djk.add(2, 8, 2)
        self.djk.add(2, 3, 7)
        self.djk.add(2, 5, 4)

        # djk.add(7, 0, 8)
        # djk.add(7, 1, 11)
        self.djk.add(7, 8, 7)
        self.djk.add(7, 6, 1)

        self.djk.add(6, 7, 1)
        self.djk.add(6, 8, 6)
        self.djk.add(6, 5, 2)

        # djk.add(8, 7, 7)
        # djk.add(8, 6, 6)
        # djk.add(8, 2, 2)

        # djk.add(5, 6, 2)
        # djk.add(5, 2, 4)
        self.djk.add(5, 3, 14)
        self.djk.add(5, 4, 10)

        # djk.add(3, 2, 7)
        # djk.add(3, 5, 4)
        self.djk.add(3, 4, 9)

    def test_undirected_graph(self):
        self.djk.print()

    def test_show_solution(self):
        self.djk.show(1)
