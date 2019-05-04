class CircleOfFriends:

    """
    There are N students in a class. Some of them are friends,
    while some are not. Their friendship is transitive in nature.
    For example, if A is a direct friend of B, and B is a direct friend of C,
    then A is an indirect friend of C. And we defined a friend circle
    is a group of students who are direct or indirect friends.

    Given a N*N matrix M representing the friend relationship
    between students in the class. If M[i][j] = 1,
    then the ith and jth students are direct friends with each other,
    otherwise not. And you have to output the total number of friend circles
    among all the students.

    :type M: List[List[int]]
    :rtype: int

    """

    def __init__(self, matrix):
        self.matrix = matrix
        self.visited = set()
        self.graph = collections.defaultdict(set)
        self.create_graph()

    def create_graph(self):
        _length = len(M)
        for i in range(_length):
            for j in range(_length):
                if self.matrix[i][j] ==1:
                    self.graph[i].add(j)

    def dfs(self, node):
        if node not in self.visited:
            self.visited.add(node)
            for i in self.graph[node]:
                self.dfs(i)

    def count_circles(self):
        _result = 0
        for i in range(len(self.matrix)):
            if i not in self.visited:
                self.dfs(i)
                _result +=1
        return _result

M= [[1,1,0], [1,1,0], [0,0,1]]
cof = CircleOfFriends(M)
print("Number of circles: {}".format(cof.count_circles()))
