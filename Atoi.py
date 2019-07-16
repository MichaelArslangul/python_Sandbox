class Atoi:
    _NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    _CHAR = ["+", "-"]

    def myAtoi(self, str: str) -> int:
        _res_str = ""
        _input = str.strip()
        if not _input:
            return 0
        if _input[0] not in (self._NUMBERS+self._CHAR):
            print(_input[0])
            return 0
        if _input[0] in self._CHAR:
            _res_str += _input[0]
            _input = _input[1:]

        for chr in _input:
            if chr in self._NUMBERS:
                _res_str += chr
            else:
                break
        if _res_str in self._CHAR:
            return 0
        if int(_res_str) < -2**31:
            return -2**31
        if int(_res_str) > 2**31:
            return 2**31
        return int(_res_str)




atoi = Atoi()
# input = "words and 987"
input="2+12223 words 22222"
print("result for string: {} is: {}".format(input, atoi.myAtoi(input)))
