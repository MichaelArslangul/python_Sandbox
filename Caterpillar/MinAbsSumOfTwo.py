class MinAbsSumOfTwo:
    """
    https://app.codility.com/programmers/lessons/15-caterpillar_method/min_abs_sum_of_two/
    """

    # def solution(self, A):
    #     N =len(A)
    #     _result = float("inf")
    #     j = 0
    #     for i in range(N):
    #         j = i+1
    #         _result = min(_result, abs(A[i] + A[i]) )
    #         while j < N:
    #             _result = min(_result, abs(A[i] + A[j]) )
    #             j += 1
    #     return _result

    def solution(self, A):
        value = 2000000000
        _back = 0
        _front = len(A)-1
        A.sort()

        while _back <= _front:
            value = min(value, abs(A[_back] + A[_front]))
            if abs(A[_back]) > abs(A[_front]):
                _back += 1
            else:
                _front -= 1
        return value

from itertools import *
def getAbsDiff(t):
  return abs(t[0] + t[1])

def solution(A):
  A.sort(key=abs)
  return getAbsDiff(min(chain(izip(A, A),izip(A,A[1:])), key = getAbsDiff))


ma = MinAbsSumOfTwo()
array = [-23, -5, -3, -1, 0, 3, 6, 12, 17, 23]
print("Min abs in the array {}: {}".format(
    array, ma.solution(array)))
