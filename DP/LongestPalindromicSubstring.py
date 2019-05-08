class LongestPalindromicSubstring:
    """ Leetcode 5 """

    def longestPalindrome(self, s: str) -> str:
        _res = [0]*(len(s)+1)
        _res_str = ""
        if len(s) == 1:
            return s
        if self.is_palindrome(s):
            return s
        for i in range(1, len(s)+1):
            _max = max(_res)
            for j in range(i):
                if self.is_palindrome(s[j:i]):
                    if _max < len(s[j:i]):
                        _res[i] = len(s[j:i])
                        _res_str = s[j:i]
                        break
                    else:
                        _res[i] = _max
        return _res_str

    def is_palindrome(self, s):
        return s[::-1] == s


lps = LongestPalindromicSubstring()
# input = "abadd"
input = "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
print("longest palindrome substring of: {} is: {}".format(
    input, lps.longestPalindrome(input)
))
