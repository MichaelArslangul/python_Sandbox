from functools import lru_cache


class Fibonacci:
    """ Use built-in lru_cache in view of memoization and memoization option
    """

    @lru_cache(32)
    def fib(self, number):
        if number <= 1:
            return number
        else:
            return self.fib(number - 1) + self.fib(number - 2)


    def good_recursive_fibonacci(self, number):
        if number <=1:
            return (number, 0)
        else:
            # this step returns Fn-1 and Fn-2 or a and b
            # to return Fn, I add Fn-1 and Fn-2 or a + b
            # and return (Fn, Fn-1)
            (a,b) = self.good_recursive_fibonacci(number -1)
            return (a+b, a)


fib = Fibonacci()
for i in range(1, 51):
    print("Fibonacci element at index {}: {}".format(
        i, fib.fib(i)))
    print("good recursive Fibonacci for 50: {}".format(fib.good_recursive_fibonacci(50)))
