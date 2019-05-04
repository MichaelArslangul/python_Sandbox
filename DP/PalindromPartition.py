import math
class PalindromPartition:
    """ Leetcode 132
    """

    def minCut(self, s):
        _res = self.dp_min_cut(len(s), s)
        return _res

    def dp_min_cut(self, index, s):
        N=len(s)
        _min_cut = [(i-1) for i in range(index+1)]

        for i in range(1, N+1):
            _min_value = float('inf')
            for j in range(i):
                if self.is_palindrome(s[j:i]):
                    _min_value = min(_min_value, 1 + _min_cut[j])
            _min_cut[i] = _min_value
        return _min_cut[index]

    def is_palindrome(self, s):
        return s == s[::-1]

pp = PalindromPartition()
# _string = "cabababcbc"
# _string = "abbab"
# _string = "leet"
_string = "ab"
print("min number of cuts for string: {} is {}".format(
    _string, pp.minCut(_string)))






# for i in range(1, N):
#     if self.is_palindrome(s[:i]):
#         print(s[:i])
#         print(_min_value)
#         print(1 + self.minCut(s[:i-1]))
#         print
#         _min_value = min(_min_value, 1 + self.minCut(s[:i-1]))

        # for i in range(1, N-1):
        #     print(i)
        #     print("s[:N-1-i]: {}".format(s[:N-i]))
        #     print("s[i:]: {}".format(s[i:]))
        #     _min_value += 1 + min(self.minCut(s[:N-1-i]), self.minCut(s[i:]))
        #     print("_min_value: {}".format(_min_value))
        #     print("--")
        # return _min_value
