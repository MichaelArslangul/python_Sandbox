class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value

class LinkedList:

    def __init__(self, head: Node = None):
        self.head = None

    def reverse_linked_list(self, ReverseLinkedList):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current.next = next

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print(self):
        node = self.head
        while node:
            print(self.head)
            node = node.next


ll = LinkedList()
ll.head = Node('1')
ll.head.next = Node('2')
ll.head.next.next = Node('3')
ll.head.next.next.next = Node('4')
