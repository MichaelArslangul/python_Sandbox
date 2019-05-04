class LinkedListPalindrome:
    """
    Checks whether a linked list is a palindrome
    """

    class Node:

        def __init__(self, value, next = None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            raise Exception("Nothing to print")
        _printval = self.head
        while _printval is not None:
            print(_printval.value)
            _printval = _printval.next

    def add(self, element):
        _node = self.Node(element)
        if self.head is None:
            self.head = _node
        else:
            _node.next = self.head
            self.head = _node

    def palindrome(self):
        """
        writes all elements in a list, then move forward and backward
        and check for equality, if not equal, not a palindrome
        """
        _front = self.head
        _back = self.head
        i = 0
        _list = []

        while _back is not None:
            _list.append(_back.value)
            _back = _back.next
            i += 1

        _count = 1
        while _count < i//2 +1:
            if not _list[-_count] == _front.value:
                print("Value: {} not equal to: {}".format(
                    _list[-_count], _front.value))
                return False
            else:
                _front = _front.next
                _count += 1
        return True

    def palindrome2(self):
        """
        Uses a list and reverses it to check for equality
        """
        _list = []
        p = self.head
        while p:
            _list.append(p.value)
            p = p.next
        return _list == _list[::-1]


lq = LinkedListPalindrome()
lq.add('R')
lq.add('A')
lq.add('D')
lq.add('A')
lq.add('R')
lq.print_list()
print(lq.palindrome())
print(lq.palindrome2())

lq1 = LinkedListPalindrome()
lq1.add('A')
lq1.add('B')
lq1.add('C')
lq1.print_list()
print(lq1.palindrome())
print(lq1.palindrome2())
