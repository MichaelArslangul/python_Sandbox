class LongestSubstring:
    """ Leetcode 3
    """


    def lengthOfLongestSubstring(self, s: str) -> int:
        """ Intuition was DP. Implementation is space and time expensive. """
        _len_of_sub = 0
        dp = [""]*(len(s) + 1)
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        dp[0] = s[0]
        for i in range(1, len(s)):
            if s[i] in dp[i-1]:
                for j in range(1, i+1):
                    if s[i] in dp[i-1][j:]:
                        continue
                    else:
                        dp[i] = dp[i-1][j:] + s[i]
                        break
            else:
                dp[i] = dp[i-1] + s[i]
            _len_of_sub = max(_len_of_sub, len(dp[i]))
        return _len_of_sub

    def lengthOfLongestSubstring2(self, s: str) -> int:
        _front = 0
        _back = 0
        _visited = set()
        _res = 0
        while _front != len(s):
            if s[_front] not in _visited:
                _visited.add(s[_front])
                _res = max(_res, len(_visited))
                _front +=1
            else:
                _visited.remove(s[_back])
                _back +=1
        return _res



LS = LongestSubstring()
_str1 = "aa"
_str2 = "abcabcbb"
_str3 = "bbbbbb"
_str4 = "pwwkew"
_str5 = "dvdf"
_str6 = "anviaj"
_str7 = "tmmzuxt"
print("Length of the longest substring is: {}".format(
    LS.lengthOfLongestSubstring(_str1)))
print("Length of the longest substring is: {}".format(
    LS.lengthOfLongestSubstring(_str2)))
print("Length of the longest substring is: {}".format(
    LS.lengthOfLongestSubstring(_str3)))
print("Length of the longest substring is: {}".format(
    LS.lengthOfLongestSubstring2(_str4)))
print("Length of the longest substring is: {}".format(
    LS.lengthOfLongestSubstring2(_str5)))
print("Length of the longest substring is: {}".format(
    LS.lengthOfLongestSubstring2(_str6)))
print("Length of the longest substring is: {}".format(
    LS.lengthOfLongestSubstring2(_str7)))
