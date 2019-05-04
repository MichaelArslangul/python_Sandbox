class LinkedList:
    """
    Simple LinkedList
    """

    class Node:

        def __init__(self, value, next = None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def _empty(self):
        return self.length == 0

    def _length(self):
        return self.length

    def print_list(self):
        if self.head is None:
            raise Exception("LinkedList is empty, nothing to print")
        _temp_val = self.head
        while _temp_val:
            print(_temp_val.value)
            _temp_val = _temp_val.next

    def add(self, element):
        _node = self.Node(element)
        if self.head is None:
            self.head = _node
        else:
            self.tail.next = _node
        self.tail = _node
        self.length += 1


    def dequeue(self):
        if self.head is None:
            raise Exception("Nothing to dequeue, list is empty")
        else:
            _temp = self.head
            self.head = self.head.next
            self.length -= 1
            return _temp

    def first_element(self):
        if self.head is None:
            raise Exception("Nothing to dequeue, list is empty")
        else:
            return self.head.value

# lq = LinkedList()
# lq.add('R')
# lq.add('A')
# lq.add('D')
# lq.add('A')
# lq.add('R')
# print(lq.first_element())
# lq.print_list()
# lq.dequeue()
# lq.print_list()
#
# lq1 = LinkedList()
# lq1.add('A')
# lq1.add('B')
# lq1.add('C')
# lq1.print_list()
