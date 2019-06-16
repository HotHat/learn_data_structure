import unittest
from bellman_ford import BellmanFord


class TestBellmanFord(unittest.TestCase):
    def setUp(self) -> None:
        self.bellman = BellmanFord()
        self.bellman.add('A', 'B', -1)
        self.bellman.add('A', 'C', 4)
        self.bellman.add('B', 'C', 3)
        self.bellman.add('B', 'D', 2)
        self.bellman.add('D', 'B', 1)
        self.bellman.add('D', 'C', 5)
        self.bellman.add('B', 'E', 2)
        self.bellman.add('E', 'D', -3)

    def test_graph(self):
        self.bellman.print()

    def test_solution(self):
        ss = self.bellman.solution('A')
        print(ss)

    def test_show(self):
        self.bellman.show('A')
