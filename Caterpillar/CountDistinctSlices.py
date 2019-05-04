class CountDistinctSlices:
    """ An integer M and a non-empty array A consisting of N non-negative integers
    are given. All integers in array A are less than or equal to M.

    A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice
    of array A. The slice consists of the elements A[P], A[P + 1], ..., A[Q].
    A distinct slice is a slice consisting of only unique numbers.
    That is, no individual number occurs more than once in the slice.

    For example, consider integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
    There are exactly nine distinct slices:
    (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

    The goal is to calculate the number of distinct slices.

    Write a function:

    def solution(M, A)

    that, given an integer M and a non-empty array A consisting of N integers,
    returns the number of distinct slices.
    """


    def nbr_of_distinct_slices(self, M, A):
        _result = []
        for i in range(len(A)):
            j = i+1
            _result.append((i, i))
            _set = set()
            _set.add(A[i])
            while j < len(A) and A[j] not in _set:
                _set.add(A[j])
                _result.append((i, j))
                j += 1
        return len(_result)







nbr_slices = CountDistinctSlices()
array = [3, 4, 5, 5, 2]
print("How many absolute values are there in the array {}: {}".format(
    array, nbr_slices.nbr_of_distinct_slices(6, array)))
