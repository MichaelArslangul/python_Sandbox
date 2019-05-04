from collections import OrderedDict

class LRUCache(object):


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.remains = capacity
        self._lru_dictionary = OrderedDict()



    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self._lru_dictionary.keys():
            _value = self._lru_dictionary.pop(key)
            self._lru_dictionary[key] = _value
            return _value
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self._lru_dictionary:
            self._lru_dictionary.pop(key)
        else:
            if self.remains > 0:
              self.remains -=1
            else:
                self._lru_dictionary.popitem(False)
        self._lru_dictionary[key] = value
