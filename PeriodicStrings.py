class PeriodicString:
    """
    Find whether string S is periodic.
    Periodic indicates S = nP.
    e.g.
    S = "ababab", then n = 3, and P = "ab"
    S = "xxxxxx", then n = 1, and P = "x"
    S = "aabbaaabba", then n = 2, and P = "aabba"

    Given string S, find out the P (repetitive pattern) of S.
    """

    def repeted_substring(self, str):
        N = len(str)
        _pattern = str[0]
        if N == 1:
            return str
        else:
            for i in range(N//2, 1, -1):
                if N % i == 0:
                    if str[:i]*int(N//i) == str and str[:i] != str[0] * (i):
                        if len(str[:i]) > len(_pattern):
                            _pattern = str[:i]
        return _pattern

ps = PeriodicString()
str="ababab"
# str = 'xxxxxx'
# str = "aabbaaabba"
# str = "blah"
print("Repeted substring is: {} for string: {}".format(
    ps.repeted_substring(str), str))
