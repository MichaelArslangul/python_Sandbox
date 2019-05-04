class Findpairs:
    def __init__(self):
        self._my_list = [1, 7, 5, 9, 2, 12, 3]
        self.delta = 2

    def find_pairs(self):
        _pairs = []
        _my_set = set(self._my_list)
        print("My set: {}".format(_my_set))
        for _value in self._my_list:
            if _value + self.delta in _my_set:
                _pairs.append([_value, _value + self.delta])
        return _pairs


findpairs = Findpairs()
print("Pairs: {}".format(findpairs.find_pairs()))
