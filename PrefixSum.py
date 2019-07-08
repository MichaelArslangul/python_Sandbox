class PrefixSum:
    """
    Pass an array and build a prefix sum array which contains the sum at each
    index i of the array of A[0] to A[i] elements
    """


    def prefix_sum(self, array):
        N = len(array)
        P = [0] * (N + 1)
        for i in range(1, N+1):
            P[i] = P[i-1] + array[i-1]
        return P

    def suffix_sum(self, array):
        N = len(array)
        P = [0] * (N + 1)
        for i in range(1, N+1):
            P[i] = P[i-1] + array[N-i]
        return P

ps = PrefixSum()
array = [2, 3, 7, 5, 1, 3, 9]
print("prefix sum for array: {} is: {}".format(array, ps.prefix_sum(array)))
print("suffix sum: {}".format(ps.suffix_sum(array)))
