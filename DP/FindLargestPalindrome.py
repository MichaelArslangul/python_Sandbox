class FindLargestPalindrome:
    """ Find the largest palindrome made from the product of two
    n-digit numbers. Since the result could be very large,
    you should return the largest palindrome mod 1337.
    """

    def nbr_of_ways(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 9
        _max = 10**n
        for i in range(_max -1, 1, -1):
            _pal = self.palindrome(i)
            # for j in range(int(_pal**.5), _max +1):
            for j in range(_max-1, int(_pal**.5), -1 ):
                if self.is_entier(_pal/j) and _pal/j < _max:
                    print("x: {}, y: {} for pal: {}".format(j, int(_pal/j), _pal))
                    return _pal%1337
        return None


    def palindrome(self, number):
        _s = str(number)
        return number*10**len(_s) + int(_s[::-1])

    def is_entier(self, number):
        return int(number) == number



lp = FindLargestPalindrome()
A = 8
print("Largest palindrome for from the product of two {} digit number is: {}".format(
    A, lp.nbr_of_ways(A)))
