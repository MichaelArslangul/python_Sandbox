from collections import deque

class RouteBetweenNodes:
    """ Given a directed graph, find out whether there is a
    path between nodes
    """

    def __init__(self, graph):
        self.graph = graph

    def path_exist(self, source, destination):
        if source not in self.graph.keys() or \
            destination not in self.graph.keys():
            raise Exception("{} or {} not in graph".format(node1, node2))
        elif source == destination:
            print("nothing to do")
            return source
        else:
            _visited = set()
            _queue = deque()

            _visited.add(source)
            _queue.append(source)

            while _queue:
                _current = _queue.popleft()
                for i in self.graph[_current]:
                    if i not in _visited:
                        if i == destination:
                            return True
                        else:
                            _visited.add(i)
                            _queue.append(i)
            return False




graph = {}
graph["Frank"] = ["Michael", "Arnaud"]
graph["Michael"] = ["Gabrielle", "Lili"]
graph["Arnaud"] = ["Elodie", "Angeline"]
graph["Edith"] = ["Piaf"]
graph["Gabrielle"] = ["Lili"]
graph["Elodie"] = ["Angeline"]
graph["Lili"] = []
graph["Angeline"] = []
graph["Piaf"] = []

route = RouteBetweenNodes(graph)
print("Is there a path between {} and {}: {}".format(
    "Frank", "Angeline", route.path_exist("Frank", "Piaf")))
