class Dijkstra:

    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, start, end):
        _shortest_distance = {}
        _predecessor = {}
        _path = []
        _unseen_nodes = self.graph

        for node in _unseen_nodes:
            _shortest_distance[node] = float('inf')
        _shortest_distance[start] = 0

        while _unseen_nodes:
            _min_node = None
            for node in _unseen_nodes:
                if _min_node is None:
                    _min_node = node
                elif _shortest_distance[node] < _shortest_distance[_min_node]:
                    _min_node = node

            for child_node, weight in graph[_min_node].items():
                if weight + _shortest_distance[_min_node] < _shortest_distance[child_node]:
                    _shortest_distance[child_node] = weight + _shortest_distance[_min_node]
                    _predecessor[child_node] = _min_node
            _unseen_nodes.pop(_min_node)

        _currentNode = end
        while  _currentNode != start:
            try:
                _path.insert(0, _currentNode)
                _currentNode = _predecessor[_currentNode]
            except KeyError:
                return "Unreachable path"
        _path.insert(0, start)

        if _shortest_distance[end] != float('inf'):
            print("Shortest path is: {}".format(_path))
            return _shortest_distance[end]





graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
dk = Dijkstra(graph)
print("Length of the shortest path between {} and {} is: {}".format("a", "d", dk.shortest_path("a", "d")))
