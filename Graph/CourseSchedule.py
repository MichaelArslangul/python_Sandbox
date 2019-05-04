from collections import defaultdict, deque

class SourceToTarget:
    """
    Leetcode 797
    """

    def find_paths(self, input):
        _graph = defaultdict(list)
        _visited = [False]*len(input)
        _destination = input[-2]
        _path = []
        if not input:
            return []
        else:
            for i in range(len(input)):
                _graph[i] = input[i]
        return self.dfs(_graph, 0 , _destination[0], _visited, _path)

    def dfs(self, graph, source, destination, visited, path):
        visited[source] = True
        path.append(source)
        if source == destination:
            print(path)
        for item in graph[source]:
            if visited[item] == False:
                self.dfs(graph, item, destination, visited, path)
        path.pop()
        visited[source] = False

fp = SourceToTarget()
input = [[1,2], [3], [3], []]
print("Paths between {} and {} are: {}".format(
    0, len(input) - 1, fp.find_paths(input)))
