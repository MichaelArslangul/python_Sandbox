class FindPaths:
    """
    Finds all the path between nodes
    """

    def find_paths(self, graph, start, end):
        if start == end:
            return []
        if start or end not in graph:
            return None
        

fp = FindPaths()
graph = {'A': ['B', 'C'],'B': ['C', 'D'], 'C': ['D'], 'D': ['C'],'E': ['F'],'F': ['C']}
start = 'A'
end = 'D'
print("Paths between {} and {} are: {}".format(
    start, end, fp.find_paths(graph, start, end)))
