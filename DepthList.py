from LinkedList import LinkedList
from collections import deque

class DepthList:
    """ Store each element at a given depth of the tree in a linked List
    """

    def __init__(self, graph):
        self.graph = graph

    def bfs(self, source):
        """ This method will create and store elements in lists
        """
        _visited = set()
        _queue = deque()
        _perm_queue = deque()
        _max_depth = 0
        _depth = 0

        _visited.add(source)
        _perm_queue.append((source, _depth))
        _queue.append((source, _depth))
        while _queue:
            _current, _level = _queue.popleft()
            if _level > _depth:
                _depth += 1
            for _temp in self.graph[_current]:
                if _temp not in _visited:
                    _max_depth = max(_depth + 1, _max_depth)
                    _perm_queue.append((_temp, _depth +1))
                    _queue.append((_temp, _depth +1))
                    _visited.add(_temp)
        print(_perm_queue)
        # _list_of_linkedList = self._create_lists_based_on_depth(_perm_queue, _max_depth)
        # self.print_elements(_list_of_linkedList)

    # def _create_lists_based_on_depth(self, queue, _max_depth):
    #     _ans = []
    #     _depth = 0
    #
    #     while queue:
    #         _temp = queue.popleft()
    #         _value = _temp[0]
    #         _idepth = _temp[1]
    #
    #         _my_list = LinkedList()
    #         if _idepth == _depth:
    #             print("")
    #             _my_list.add(_value)
    #         elif _idepth > _depth:


        #     for i in range(_max_depth + 1):
        #         _link_list = LinkedList()
        #         if _depth == i:
        #             print("value: {} at depth: {}".format(
        #                 _value, _depth
        #             ))
        #             _link_list.add(_value)
        #             # _link_list.print_list()
        #         print("list at depth: {}: {}".format(i, _link_list.print_list()))
        #         _ans.append(_link_list)
        # print("_ans: {}".format(_ans))
        # return _ans

    def print_elements(self, _list_of_linkedList):
        for i in range(len(_list_of_linkedList)):
            print("List at depth: {} contains: {}".format(
                i, _list_of_linkedList[i].print_list()))



graph = {}
graph["Frank"] = ["Michael", "Arnaud"]
graph["Michael"] = ["Gabrielle", "Lili"]
graph["Arnaud"] = ["Elodie", "Angeline"]
graph["Edith"] = ["Piaf"]
graph["Gabrielle"] = ["Lili"]
graph["Elodie"] = ["Angeline"]
graph["Lili"] = []
graph["Angeline"] = ["Bob"]
graph["Bob"] = []
graph["Piaf"] = []

df = DepthList(graph)
df.bfs("Frank")
# df.print_list()
