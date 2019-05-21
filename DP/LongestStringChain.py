from collections import defaultdict
class LongestStringCheck:
    """ Leetcode 1048
    """


    def longestStrChain(self, words):
        dp = defaultdict(list)
        s_words = sorted(words, key = len)
        for _word in s_words:
            for i in range(len(_word)):
                print(dp)
                print(_word)
                print(_word[:i] + _word[i+1:])
                if _word[:i] + _word[i+1:] in dp.keys():
                    print("in")
                    dp[_word] = dp[_word[:i] + _word[i+1:]].append(_word)
                else:
                    dp[_word].append(_word)
        return dp



lsc = LongestStringCheck()
input = ["a","b","ba","bca","bda","bdca"]
print("longest sting check of: {} is: {}".format(
    input, lsc.longestStrChain(input)))
# ["a","b","ba","bca","bda","bdca"]
# ["bdca","a","d","bca","ba","bda"]
