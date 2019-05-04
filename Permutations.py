class Permutations:
    '''
    Return all permutations of a string
    '''

    # def __init__(self, word):
    #     self.word = word

    # def insert_char_at_position(self, str, chr_to_insert, position):
    #     return str[0:position] + chr_to_insert + str[position + 1:]

    def permutation(self, word):
        if len(word) == 1:
            return word
        else:
            _result = set()
            for i in range(len(word)):
                _chr = word[i]
                _temp_str = word[:i] + word[i+1:]
                for p in self.permutation(_temp_str):
                    _result.add(_chr + p)
            return _result


perm = Permutations()
print(perm.permutation('casts'))
