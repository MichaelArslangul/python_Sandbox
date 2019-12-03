class TopologicalSort:
    '''
    Topological sort on a graph
    '''

    def topological_sort(self, graph):
        visited = set()
        t_sorted = []
        for node in graph.keys():
            if node not in visited:
                self.topological_sort_util(node, visited, t_sorted)
        return t_sorted[::-1]

    def topological_sort_util(self, node, visited, t_sorted):
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                self.topological_sort_util(child, visited, t_sorted)
        t_sorted.append(node)

ts = TopologicalSort()
graph = {'A':['C'], 'B': ['C', 'D'], 'C' :['E'], 'D':['F'],
         'E':['F', 'H'], 'F':['G'], 'G':[], 'H':[]}
print("topologial sort of the graph: {}".format(ts.topological_sort(graph)))
