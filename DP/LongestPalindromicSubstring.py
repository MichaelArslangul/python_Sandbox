class LongestPalindromicSubstring:
    """ Leetcode 5 """

    def longestPalindrome(self, s: str) -> str:
        _res = ""
        if len(s) == 1:
            return s
        if self.is_palindrome(s):
            return s

    def is_palindrome(self, s):
        return s[::-1] == s


lps = LongestPalindromicSubstring()
input = "babad"
print("longest palindrome substring of: {} is: {}".format(
    input, lps.longestPalindrome(input)
))
