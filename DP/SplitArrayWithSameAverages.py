from collections import defaultdict

class SplitArrayWithSameAverages:

    def can_split(self, A):
        N = len(A)
        _avg = sum(A)/N
        _sums = defaultdict(set)
        _sums[0] = {0}
        _sums[1] = {A[0]}
        for i in range(1, N):
            _element = A[i]
            for j in range(i//2+1, 0, -1):
                for c in _sums[j-1]:
                    if self.subset_avg_equal_avg(c+_element, j, _avg):
                        return True
                    else:
                        _sums[j].add(c + _element)
            _sums[1].add(_element)
        return False

    def subset_avg_equal_avg(self, subset_sum, level, array_average):
        return round(float(subset_sum),2) == round(float(level*array_average),2)

sa = SplitArrayWithSameAverages()
A = [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5] # 14
# A=[18,10,5,3]
# A=[1,6,1]
# A = [2,4,5,7,10,14]
# A = [18,0,16,2]
# A= [1,2,3,4,5,6,7,8] #36/8
print("can split?: {}".format(
    sa.can_split(A)))
