class SelectionSort:
    """
    """


    def selection_sort(self, A):
        N = len(A)
        _min = 0
        for i in range(N):
            _min = i
            for j in range(_min + 1, N):
                if A[j] < A[_min]:
                    _min = j
            A[i], A[_min] = A[_min], A[i]
        return A




ss = SelectionSort()
A = [0, 3, 6, 12, 3, 17, 23]
print("sorted array: {}".format(
    ss.selection_sort(A)))
