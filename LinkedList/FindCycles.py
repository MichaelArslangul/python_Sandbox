class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "Node <{}>\n".format(self.value)

class LinkedList:
    """ Given a LinkedList, return True if the list has cycles, False otherwise
    """
    def __init__(self, head: Node = None):
        self.head = head

    def cycle_detection(self, head=None):
        slow, fast = self.head, self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow.value == fast.value:
                return True
        return False

    def __repr__(self):
        if self.head:
            _temp_node = self.head
        else:
            raise Exception("Trying to print empty list")
        while _temp_node:
            _temp_node = _temp_node.next

start = Node('1')
start.next = Node('2')
start.next.next = Node('3')
start.next.next.next = Node('4')
start.next.next.next.next = start.next
fc = LinkedList(start)
print(fc.cycle_detection())
