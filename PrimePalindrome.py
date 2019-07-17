class PrimePalindrome:
    def primePalindrome(self, N):
        if N == 1 or N == 2:
            return 2
        if N % 2 == 0:
            for i in range(N+1, N**2, 2):
                if self.is_palindrome(i):
                    if self.is_prime(i):
                        return i
                continue
        else:
            for i in range(N, N**2, 2):
                if self.is_palindrome(i):
                    if self.is_prime(i):
                        return i
                continue
        return False

    # def check(self, n):

    def is_palindrome(self, N):
        return N == int(str(N)[::-1])

    def is_prime(self, n):
        for i in range(3, 1 + int(n**0.5), 2):
            if n % i == 0:
                return False
        return True


pp = PrimePalindrome()
N = 9989900
print("First prime palindrome after {} is: {}".format(N, pp.primePalindrome(N)))
