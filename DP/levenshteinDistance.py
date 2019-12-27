class LevenshteinDistance:

    def levenshteinDistance(self, str1, str2):
    	length1 = len(str1)
    	length2 = len(str2)
    	if length1 == 0:
    		return length2
    	if length2 == 0:
    		return length1
    	DP = [[0 for _ in range(length2 +1)] for _ in range(length1+1)]
    	for i in range(length1+1):
    		for j in range(length2+1):
    			if i == 0:
    				DP[i][j] = j
    			elif j == 0:
    				DP[i][j] = i
    			elif str1[i-1] == str2[j-1]:
    				DP[i][j] = DP[i-1][j-1]
    			else:
    				DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1
    	return DP[-1][-1]

ld = LevenshteinDistance()
print("Levenshtein Distance between: {} and {} is: {}".format(
    "sunday", "saturday",ld.levenshteinDistance("sunday", "saturday")))
