class PalindromeCheck:

    def isPalindrome(self, inputString):
        n = len(inputString)

        if n == 0:
            return True

        if inputString[0] != inputString[-1]:
            return False

        return self.isPalindrome(inputString[1:n-1])

pa = PalindromeCheck()
print(pa.isPalindrome("abcdefedcba"))
