class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_right(self, value):
        node = BinaryNode(value)
        node.right = self.right
        self.right = node

    def add_left(self, value):
        node = BinaryNode(value)
        node.left = self.left
        self.left = node

    def in_order(self):
        if self.left:
            for v in self.left.in_order():
                yield v

        yield self.value

        if self.right:
            for v in self.right.in_order():
                yield v

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_right(self, value):
        if not self.root:
            self.root = BinaryNode(value)
        else:
            self.root.add_right(value)

    def add_left(self, value):
        if not root:
            self.root = BinaryNode(value)
        else:
            self.root.add_left(value)

    def __iter__(self):
        if self.root:
            for v in self.root.in_order():
                yield v


class SizeOfTree:
    """
    Given a binary tree, return the number of nodes in that tree
    """

    def __init__(self, tree):
        self.tree = tree
        self.size = 0

    def size_of_tree(self):
        if not self.tree.root:
            return 0
        else:
            for _ in self.tree:
                self.size +=1
        return self.size




bin = BinaryTree()
bin.add_right(3)
bin.root.add_left(6)
bin.root.left.add_left(2)
bin.root.left.add_right(11)
bin.root.left.right.add_left(9)
bin.root.left.right.add_right(5)
bin.root.add_right(8)
bin.root.right.add_right(13)
bin.root.right.right.add_left(7)
sot = SizeOfTree(bin)

print("size of tree is: {}".format(sot.size_of_tree()))
