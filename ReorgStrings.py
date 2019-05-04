from collections import Counter

class ReorgStrings:

    def reorganizeString(self, S):
        if len(S) == 0:
            return ""
        elif len(S) == 1:
            return S
        _counter = Counter(S).most_common()
        print(_counter)
        if Counter(S).most_common(1)[0][1] > (len(S) + 1) // 2:
            return ""
        _res = [""]*len(S)
        _index = 0
        _left_over = []
        print(_counter[0])
        for letter, count in _counter:
            for _ in range(count):
                if _index < len(S):
                    _res[_index] = letter
                    _index += 2
                else:
                    _left_over.append(letter)
        _start = 1
        for letter in _left_over:
            _res[_start] = letter
            _start += 2
        return "".join(_res)






rs = ReorgStrings()
print(rs.reorganizeString("aabc"))
