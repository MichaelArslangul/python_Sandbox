from LRUCache import LRUCache

class FibonacciWithLRU:

    def __init__(self):
        self.lru = LRUCache(4)

    def fib(self, number):
        self.lru.put(0, 0)
        self.lru.put(1, 1)
        for i in range(2, number + 1):
            self.lru.put(i, self.lru.get(i-1) + self.lru.get(i-2))
        return self.lru.get(number)

fib = FibonacciWithLRU()
for i in range(1, 45):
    print("Fibonacci element at index {}: {}".format(
        i, fib.fib(i)))

]
