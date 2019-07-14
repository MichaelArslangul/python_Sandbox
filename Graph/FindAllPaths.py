from collections import defaultdict, deque

class FindAllPaths:
    """
    Leetcode 797 - Second implementation
    """
    def allPathsSourceTarget(self, graph):
        N = len(graph)
        res = []
        def dfs(N, graph, start, res, path):
            if start == N-1:
                res.append(path)
            else:
                for node in graph[start]:
                    dfs(N, graph, node, res, path + [node])
        dfs(N, graph, 0, res, [0])
        return (res)

fp = FindAllPaths()
input = [[1,2], [3], [3], []]
print("Paths are: {}".format(fp.allPathsSourceTarget(input)))
