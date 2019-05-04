class IntPalindromes:
    '''
    Retrieve closest  palendrome
    '''

    def get_closest_palindromes(self, n):
        _n = int(n)
        if _n < 10:
            return str(_n-1)
        # elif self.is_palendrome(_n):
        #     return str(self.get_lower_palindrome(_n))
        else:
            if (_n - self.get_lower_palindrome(_n)) <= \
                    (self.get_higher_palindrome(_n) - _n):
                return str(self.get_lower_palindrome(_n))
            else:
                return str(self.get_higher_palindrome(_n))

    def get_higher_palindrome(self, n):
        n += 1
        while not self.is_palendrome(n):
            n += 1
        return n

    def get_lower_palindrome(self, n):
        n -= 1
        while not self.is_palendrome(n):
            n -= 1
        return n

    def is_palendrome(self, n):
        _sn = str(n)
        return _sn == _sn[::-1]

        # _list = list(str(n))
        # _size = len(_list)
        # for i in range(_size):
        #     if not _list[i] == _list[_size - 1 - i]:
        #         return False
        # return True


ipal = IntPalindromes()
print("Is this a palendrome: {}".format(ipal.is_palendrome(1903828091)))
print(ipal.get_closest_palindromes(1903828091))
