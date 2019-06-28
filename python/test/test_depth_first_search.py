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
        # self.graph.print()
        # return
        result = []
        p_idx = 1
        stack = []
        visited = {}
        child_num = {}
        cur_child_num = {}
        back_child_num = {}
        articulation_map = {}
        father = {}
        low = {}
        depth = {}
        for i in self.graph:
            visited[i.item] = False
            child_num[i.item] = len(i.child)
            cur_child_num[i.item] = 0
            back_child_num[i.item] = 0
            articulation_map[i.item] = False

        father['6'] = None
        stack.append('6')
        visited['6'] = True
        depth['6'] = p_idx
        low['6'] = p_idx
        # father['1'] = None
        # stack.append('1')
        # visited['1'] = True
        # depth['1'] = p_idx
        # low['1'] = p_idx
        p_idx += 1

        while len(stack) != 0:
            p = self.graph.find(stack[-1])
            idx = p.item
            # print(idx)
            while cur_child_num[idx] != child_num[idx]:
                c_n = cur_child_num[idx]
                n = p.child[c_n].value
                if visited[n]:
                    cur_child_num[idx] += 1
                    # pass
                    if father[idx] is not None and n != father[idx]:
                        low[idx] = min(low[idx], depth[n])
                    continue
                else:
                    # cur_child_num[idx] += 1
                    father[n] = idx
                    depth[n] = p_idx
                    low[n] = p_idx
                    p_idx += 1
                    visited[n] = True
                    stack.append(n)
                    break
                    # cu
            else:
                # print(stack)
                print("idx:%s " % idx)
                # if cur_child_num[idx] != child_num[idx]:
                f = father[idx]
                if f is not None and low[idx] >= depth[f]:
                    articulation_map[f] = True
                if f is not None:
                    back_child_num[f] += 1
                    low[f] = min(low[f], low[idx])

                stack.pop()

                if (father[idx] is not None and articulation_map[idx]) or (
                        father[idx] is None and back_child_num[idx] > 1):
                    print("%s is articulation point" % idx)
                    result.append(idx)

                # r_child_num[n] += 1

        # print(father)
        # print(low)
        # print(depth)

        # print("current child num:")
        # print(back_child_num)
        print(result)
        for i in result:
            print('%s[color=red]' % i)
        # print(call_back_stack)
        # self.graph.print()



