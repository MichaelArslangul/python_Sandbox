class LinkedQueue:
    """
    FIFO queue ADT using a linkedList
    """

    class Node:

        def __init__(self, value, next = None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, element):
        """ add to the head of the queue """
        _node = self.Node(element)
        if self.is_empty():
            self.head = self.tail = _node
        else:
            self.tail.next = _node
        self.tail = _node
        self.size += 1


    def dequeue(self):
        """ Returns and removes first element in the queue """
        if self.head is None:
            raise Exception("nothing to dequeue, queue is empty")
        _head = self.head.value
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return _head

    def first(self):
        """ Returns first element in the queue """
        if self.head is None:
            raise Exception("nothing in queue")
        return self.head.value

    def len(self):
        return self.size

    def is_empty(self):
        return self.size == 0

lq = LinkedQueue()
lq.enqueue(1)
lq.enqueue(2)
lq.enqueue(4)
lq.enqueue(8)
print("size of the stack: {}".format(lq.len()))
print("top of the stack, pop: {}".format(lq.dequeue()))
print("size of the stack: {}".format(lq.len()))
print("top of the stack, pop: {}".format(lq.dequeue()))
print("size of the stack: {}".format(lq.len()))
print("top of the stack, top: {}".format(lq.first()))
print("size of the stack: {}".format(lq.len()))
