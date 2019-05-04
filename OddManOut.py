from collections import defaultdict

class OddManOut:
    """
    Starting with an unsorted array of integer where every integer appeas exactly
    twice except for one which appears only once.
    Write an algorithm that finds the integer that appears only once
    """


    def is_unique_integer(self, array):
        _def_dict = defaultdict(int)
        for i in array:
            _def_dict[i] += 1
        print(_def_dict)
        for _chr, _val in _def_dict.items():
            if _val == 1:
                return _chr
        return False


omo = OddManOut()
array = [1,7,7,4,1, 3, 4]
print("Is there an element which appears only once in {}: {}".format(
    array, omo.is_unique_integer(array)))
