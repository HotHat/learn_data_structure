from undirected_graph import UndirectedGraph
import unittest


class TestDepthFirstSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = UndirectedGraph()
        self.graph.add('1', '2')
        self.graph.add('1', '3')
        self.graph.add('2', '4')
        self.graph.add('3', '4')
        self.graph.add('4', '5')
        self.graph.add('5', '6')
        self.graph.add('6', '7')
        self.graph.add('7', '8')
        self.graph.add('7', '9')
        self.graph.add('7', '13')
        self.graph.add('9', '10')
        self.graph.add('9', '11')
        self.graph.add('10', '11')
        self.graph.add('11', '12')
        self.graph.add('12', '13')
        self.graph.add('13', '14')

    def test_a(self):
        stack = []
        visited = {}
        child_num = {}
        father = {}
        for i in self.graph:
            visited[i.item] = False
            child_num[i.item] = 0

        stack.append('1')
        visited['1'] = True
        while len(stack) != 0:
            print(stack)
            idx = stack.pop()
            print(idx)
            p = self.graph.find(idx)
            for c in p.child:
                if visited[c.value]:
                    pass
                else:
                    child_num[idx] += 1
                    visited[c.value] = True
                    stack.append(c.value)
        # print(visited)
        # self.graph.print()



