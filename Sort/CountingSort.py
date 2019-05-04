class CountingSort:
    """
    k is the max value of the array
    """


    def counting_sort(self, A, k):
        N = len(A)
        _max_value = k+1
        _count = [0] * _max_value
        for i in A:
            _count[i] += 1
        _c = 0
        for a in range(_max_value):
            for j in range(_count[a]):
                A[_c] = a
                _c += 1
        return A




cs = CountingSort()
# A = [0, 3, 6, 12, 3, 17, 23]
A= [1,2,7,3,2,1,4,2,3,2,1]
print("sorted array: {}".format(
    cs.counting_sort(A, 24)))
