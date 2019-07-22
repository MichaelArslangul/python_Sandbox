class LongestCommonSubsequence:
    """ given 2 strings, find the longest common subsequence
    """

    def longest_sub(self, array1, array2):
        m = len(array1)
        n = len(array2)
        DP = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if array1[i-1] == array2[j-1]:
                    DP[i][j] = 1 + DP[i-1][j-1]
                else:
                    DP[i][j] = max(DP[i][j-1], DP[i-1][j])
        return DP[m][n]



ls = LongestCommonSubsequence()
A = "ABACBDAB"
B = "BDCABA"
print("Longest common subsequence between {} and {} is: {}".format(
    A, B, ls.longest_sub(A, B)))
