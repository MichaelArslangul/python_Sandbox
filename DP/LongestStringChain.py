from collections import defaultdict
class LongestStringCheck:
    """ Leetcode 1048
    """


    def longestStrChain(self, words):
        dp = defaultdict(int)
        for _word in sorted(words, key = len):
            for i in range(len(_word)):
                if _word[:i] + _word[i+1:] in dp.keys():
                    dp[_word] = max(dp[_word], dp[_word[:i] + _word[i+1:]] +1)
                else:
                    dp[_word] = max(dp[_word], 1)
        return max(dp.values())



lsc = LongestStringCheck()
input = ["a","b","ba","bca","bda","bdca"]
print("longest sting check of: {} is: {}".format(
    input, lsc.longestStrChain(input)))
