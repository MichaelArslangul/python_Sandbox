class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __repr__(self):
        return "Node <{}>".format(self.value)


class Stack:
    """ Stack using a LinkedList
    """

    def __init__(self, head = None):
        self.head = head

    def push(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def pop(self):
        if self.head:
            node = self.head
            self.head = self.head.next
            return node
        else:
            raise Exception("Can't pop an empty list")

    def peek(self):
        return (self.head)

    def is_empty(self):
        return self.head is None

node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('4')
stack = Stack()
stack.push(node1)
stack.push(node2)
stack.push(node4)
stack.push(node3)
print("peek: {}".format(stack.peek()))
print("pop: {}".format(stack.pop()))
print("peek: {}".format(stack.peek()))
print("pop: {}".format(stack.pop()))
# print("peek: {}".format(stack.peek()))
# print("pop: ()".format(stack.pop()))
