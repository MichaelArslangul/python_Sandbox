class CourseSchedule:
    """
    There are a total of n courses you have to take, labeled from 0 to n-1.

    Some courses may have prerequisites, for example to take
    course 0 you have to first take course 1, which is expressed
    as a pair: [0,1]

    Given the total number of courses and a list of prerequisite
    pairs, is it possible for you to finish all courses?
    """

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        _graph = {}
        _count = 0
        _visited = []
        _stack = []
        if len(prerequisites) == 0:
            return True

        for _prereq in prerequisites:
            print(_prereq)
            if _graph[_prereq[-1]]:
                _graph[_prereq[-1]] = _prereq[0], _graph[_prereq[-1]]
            else:
                _graph[_prereq[-1]] = _prereq[0]
        print(_graph)
        for _class, _ in _graph.items():
            _stack.append(_class)
            while _stack:
                _temp = _stack.pop()
                if _temp not in _visited:
                    _visited.append(_temp)
                    _stack.append(_graph[_temp])
                    _count +=1
                else:
                    return False
        return True


prerequisites = [[0,1], [0,2], [1,2]]
cs = CourseSchedule()
print("Can finish: {}".format(cs.canFinish(3, prerequisites)))
