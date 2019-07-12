class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """ Queue implementation using a linkedList.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, item):
        node = Node(item)
        if self.tail is None:
            self.head = node
            self.head = self.tail
            self.size = 1
        else:
            self.tail.next = node
            self.tail = self.tail.next
            self.size += 1

    def fist(self):
        if self.is_queue_empty():
            raise Empty("Nothing to pull")
        else:
            return self.head.data

    def dequeue(self):
        if self.is_queue_empty():
            raise Empty("Nothing to remove")
        else:
            node = self.head
            self.head = self.head.next
            self.size -= 1
            return node


    def is_queue_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next





queue = Queue()
queue.enqueue(Node("blah,"))
queue.enqueue(Node("blah,"))
queue.enqueue(Node("blah,"))
queue.enqueue(Node("blah,"))
queue.enqueue(Node("blah"))
while queue.size > 0:
    print(queue.dequeue().data)
