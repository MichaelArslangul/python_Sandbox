class Lexicographicalorder:
    """
    Leetcode 386
    """
    def lexical_order(self, number):
        _result = []
        for i in range(1, 10):
            self.dfs(i, number, _result)
        return _result

    def dfs(self, curr, target, result):
        if curr <= target:
            result.append(curr)
            _next_order = 10*curr
            if _next_order <= target:
                for i in range(10):
                    self.dfs(_next_order + i, target, result)




lo = Lexicographicalorder()
number = 100000

print("lexicogaphical order for number {} is: {}".format(
    number, lo.lexical_order(number)))
