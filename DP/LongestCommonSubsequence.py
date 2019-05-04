class LongestCommonSubsequence:
    """ given 2 strings, find the longest common subsequence
    """

    def longest_sub(self, array1, array2):
        M = len(array1)
        N = len(array2)
        long_sub = [[0]*(N + 1)]*(M + 1)
        for i in range(1, M+1):
            for j in range(1, N+1):
                if array1[i-1] == array2[j-1]:
                    long_sub[i][j] = 1 + long_sub[i-1][j-1]
                else:
                    long_sub[i][j] = max(long_sub[i][j-1], long_sub[i-1][j])
        return long_sub[M][N]



ls = LongestCommonSubsequence()
A = "ABACBDAB"
B = "BDCABA"
print("Longest common subsequence between {} and {} is: {}".format(
    A, B, ls.longest_sub(A, B)))
