class NearestPalindrome:


    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if int(n) <= 10:
            return str(int(n) - 1)
        _first_half = n[:len(n)//2]
        _mirror = self.return_palindrome(n)
        if len(_mirror) % 2 == 0:
            if int(_mirror) < int(n):
                _temp = int(_first_half) + 1
            else:
                _temp = int(_first_half) - 1
            new_mirror = str(_temp) + str(_temp)[::-1]
        else:
            _list = list(n)
            if int(_mirror) < int(n):
                _list[len(n)//2] = str(int(n[len(n)//2]) + 1)
            else:
                _list[len(n)//2] = str(int(n[len(n)//2]) + 1)
            new_mirror = self.return_palindrome("".join(_list))
        if abs(int(_mirror) - int(n)) == abs(int(new_mirror) - int(n)):
            if int(_mirror) < int(new_mirror):
                return _mirror
            else:
                return new_mirror
        if abs(int(_mirror) - int(n)) < abs(int(new_mirror)-int(n)):
            return _mirror
        else:
            return str(new_mirror)

    def return_palindrome(self, n):
        new = n[:len(n)//2]
        _ch = ''
        if len(n) % 2 is not 0:
            _ch = n[len(n)//2]
        return new + _ch + new[::-1]


np = NearestPalindrome()
print(np.nearestPalindromic("1111"))
