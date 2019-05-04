class ArrayQueue:
    DEFAULT_CAPACITY = 5

    def __init__(self):
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def len(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self._data[self._front]

    def enqueue(self, item):
        if self._size == ArrayQueue.DEFAULT_CAPACITY:
            raise Exception("queue is full, can't add any element")
        else:
            _index = (self._front + self._size) % ArrayQueue.DEFAULT_CAPACITY
            self._data[_index] = item
            self._size += 1

    def deque(self):
        if self.is_empty():
            raise Exception("trying to dequeue when queue is empty")
        else:
            _result = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1) % ArrayQueue.DEFAULT_CAPACITY
            self._size -= 1
            if self._size <= ArrayQueue.DEFAULT_CAPACITY // 4:
                print("could reduce size in half")
            return _result


aq = ArrayQueue()
aq.enqueue(1)
aq.enqueue(3)
aq.enqueue(5)
aq.enqueue(7)
aq.enqueue(9)
print("dequeued: {}".format(aq.deque()))
print("dequeued: {}".format(aq.deque()))
print("dequeued: {}".format(aq.deque()))
print("dequeued: {}".format(aq.deque()))
print("Is the queue empty: {}".format(aq.is_empty()))
aq.enqueue(11)
print("length: {}".format(aq.len()))
print("first element: {}".format(aq.first()))
print("Is the queue empty: {}".format(aq.is_empty()))
