from collections import defaultdict

class SumAllSubsequence:


    def sums_by_level(self, array):
        N = len(A)
        _sums = defaultdict(set)
        _sums[0]= {array[0]}

        for i in range(1, N):
            _element = array[i]
            for j in range(i, 0, -1):
                for c in _sums[j-1]:
                    _sums[j].add(c + _element)
            _sums[0].add(_element)
        return _sums



sa = SumAllSubsequence()
# A = [2,4,5,7,10,14]
A = [2, 4, 5, 7]
print("Sums by levels: {}".format(
    sa.sums_by_level(A)))
