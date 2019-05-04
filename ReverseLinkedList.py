class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value

class LinkedList:

    def __init__(self, head: Node = None):
        self.head = head

    def reverse_linked_list(self, ReverseLinkedList):
        if not self.head:
            return []
        previous_node = None
        current_node = self.head
        next_node = current_node.next




ll = LinkedList()
ll.head = Node('1')
ll.head.next = Node('2')
ll.head.next.next = Node('3')
ll.head.next.next.next = Node('4')
