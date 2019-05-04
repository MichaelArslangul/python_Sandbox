class MaxValue:
    """ Leetcode 318
    """


    def maxProduct(self, words):
        res = 0
        if not words:
            return 0
        for i in range(len(words) -1):
            _set = set(words[i])
            for j in range(i+1, len(words)):
                _second_set = set(words[j])
                if not _set&_second_set:
                    res = max(res, len(words[i])*len(words[j]))
        return res

    def maxProduct_alt(self, words):
        _val = [0] * len(words)
        res = 0
        for i in range(len(words)):
            for _chr in words[i]:
                _val[i] |= 1 << (ord(_chr) - ord('a'))
            for j in range(i):
                if _val[i] & _val[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res



mv = MaxValue()
words = ["a","ab","abc","d","cd","bcd","abcd"]
print("Max value is: {} ".format(
    mv.maxProduct(words)))
print("Max value is: {} ".format(
    mv.maxProduct_alt(words)))
