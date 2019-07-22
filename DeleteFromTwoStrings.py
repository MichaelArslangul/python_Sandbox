class DeleteOpsFromTwoStrings:

    def minDistance(self, word1, word2) -> int:
        m = len(word1)
        n = len(word2)
        DP = [[0]*(n + 1) for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    DP[i][j] = DP[i-1][j-1] + 1
                else:
                    DP[i][j] = max(DP[i][j-1], DP[i-1][j])
        _sum = DP[m][n]
        return (m - _sum) + (n - _sum)

ds = DeleteOpsFromTwoStrings()
word1="sea"
word2="eat"
print("the number of elements to delete so that {} and {} match are: {}".format(
    word1, word2, ds.minDistance(word1, word2)
))
