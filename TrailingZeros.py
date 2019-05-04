class TrailingZeroes:

    def trailing_zeroes_1(self, n):
        _count = 0
        _exp = 1
        while 10**_exp <= self.factorial(n):
            if self.factorial(n) % 10**_exp == 0:
                _count += 1
                _exp += 1
            else:
                return _count
        return _count

    def trailing_zeroes_2(self, n):
        """
        Accepted Solution
        """
        i = 5
        zeros = 0
        while n >= i:
            zeros += n // i
            i *= 5
        return zeros

    def trailing_zeroes_3(self, n):
        _count = 0
        _fact = [int(x) for x in str(self.factorial(n))]
        for i in range(len(_fact)-1, -1, -1):
            if _fact[i] == 0:
                _count += 1
            else:
                return _count
        return _count

    def factorial(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return n * self.factorial(n-1)


if __name__ == "__main__":
    for i in range(1, 21):
        print("Number of trailing zeroes for {} is: {}".format(
            i, TrailingZeroes().trailing_zeroes_1(i)))
