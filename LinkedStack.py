class LinkedStack:
    """
    stack ADT using a linkedList
    """

    class Node:

        def __init__(self, value, next = None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, element):
        self.head = self.Node(element, self.head)
        self.size += 1


    def pop(self):
        """ Return and remove top element """
        if self.is_empty():
            raise Exception("LinkedStack is empty")
        _ans = self.head.value
        self.head = self.head.next
        self.size -= 1
        return _ans

    def top(self):
        """ Return but doesn't remove from the head """
        if self.is_empty():
            raise Exception("LinkedStack is empty")
        else:
            return self.head.value

    def len(self):
        return self.size

    def is_empty(self):
        return self.size == 0

ls = LinkedStack()
ls.push(1)
ls.push(2)
ls.push(4)
ls.push(8)
print("size of the stack: {}".format(ls.len()))
print("top of the stack, pop: {}".format(ls.pop()))
print("size of the stack: {}".format(ls.len()))
print("top of the stack, pop: {}".format(ls.pop()))
print("size of the stack: {}".format(ls.len()))
print("top of the stack, top: {}".format(ls.top()))
print("size of the stack: {}".format(ls.len()))
