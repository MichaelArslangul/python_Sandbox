from collections import defaultdict


class UniqueChar:
    def __init__(self, word):
        self.word = word

    def has_dups(self):
        _d_dict = defaultdict(int)
        for _char in self.word:
            _d_dict[_char] += 1
        for key, _value in _d_dict.items():
            if _value > 1:
                print("char: {} has a value greater than 1: {}".format(
                    key, _value))
            # return True


unique_char = UniqueChar('csduicbdsuicbdsu')
print("Has dups is: {}".format(unique_char.has_dups()))
