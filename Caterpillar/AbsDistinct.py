class AbsDistinct:
    """ A non-empty A A consisting of N numbers is given.
    The A is sorted in non-decreasing order.
    The absolute distinct count of this A is the number of distinct
    absolute values among the elements of the A.

    For example, consider A A such that:

    A[0] = -5
    A[1] = -3
    A[2] = -1
    A[3] =  0
    A[4] =  3
    A[5] =  6
    The absolute distinct count of` this A is 5, because there are 5 distinct
    absolute values among the elements of this A, namely 0, 1, 3, 5 and 6.
    """


    def nbr_of_abs_values(self, A):
        N = len(set(A))
        _equal_abs_values = 0
        _front = 1
        _back = 0

        if A[0] > 0:
            return N
        if A[-1] <0:
            return N
        if len(A) == 1:
            return 1

        while A[_back] < 0:
            while A[-_front] > 0 and abs(A[_back]) <= A[-_front]:
                if abs(A[_back]) == A[-_front]:
                    _equal_abs_values += 1
                    print("values: {}, {}".format(A[_back], A[-_front]))
                    break
                _front += 1
            _back += 1
        return N - _equal_abs_values





ad = AbsDistinct()
A = [-23, -5, -3, -1, 0, 3, 6, 12, 17, 23]
print("How many absolute values are there in the A {}: {}".format(
    A, ad.nbr_of_abs_values(A)))
