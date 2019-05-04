class Palindromes:
    '''
    Return list of Palindromes
    '''

    def __init__(self, word):
        self.word = word

    def get_palindromes(self):
        _result = []
        for _temp_word in self.permutation(self.word):
            _first_half, _second_half = \
                self.first_and_second_word(_temp_word)
            if _second_half == _first_half[::-1]:
                _result.append(_temp_word)
        return _result

    def permutation(self, word):
        if len(word) == 1:
            return word
        else:
            _perm = set()
            for i in range(len(word)):
                _ch = word[i]
                _temp_word = word[:i] + word[i+1:]
                for p in self.permutation(_temp_word):
                    _perm.add(_ch + p)
            return _perm

    def first_and_second_word(self, word):
        if len(word) % 2 is not 0:
            _first_half = word[:len(word)//2]
            _second_half = word[(len(word)//2)+1:]
        else:
            _first_half = word[:len(word)//2]
            _second_half = word[(len(word)//2):]
        return _first_half, _second_half



pal = Palindromes('castsca')
print(pal.get_palindromes())
