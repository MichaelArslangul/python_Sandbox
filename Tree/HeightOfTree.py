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

    def height(self, node):
        height_left = 0
        height_right = 0
        if not node:
            return 0
        else:
            height_left = 1 + self.height(node.left)
            height_right = 1 + self.height(node.right)
        return max(height_left, height_right)

    def insert(self, root, value):
        node = BinaryNode(value)
        if not root:
            return node
        elif value < root.value:
            self.insert(root.left, value)
        else:
            self.insert(root.right, value)

    # should be __contains__
    def search(self, root, value):
        if not root:
            return None
        if root.value == value:
            return root
        elif value < root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)

    def display(self):
        for v in self:
            print(v)


class HeightOfTree:
    """
    Given a binary tree, return the height of the tree
    """

    def __init__(self, tree):
        self.tree = tree
        self.size = 0

    def height_of_tree(self, root):
        return self.tree.height(root)




bin = BinaryTree()
# bin.add_right(3)
# bin.root.add_left(6)
# bin.root.left.add_left(2)
# bin.root.left.add_right(11)
# bin.root.left.right.add_left(9)
# bin.root.left.right.add_right(5)
# bin.root.add_right(8)
# bin.root.right.add_right(13)
# bin.root.right.right.add_left(7)
# bin.root.right.right.left.add_left(8)
bin.add_right(10)
bin.root.add_left(-5)
bin.root.left.add_left(-10)
bin.root.left.add_right(5)
bin.root.add_right(25)
bin.root.right.add_right(36)
sot = HeightOfTree(bin)
value = 40
print("height of tree is: {}".format(sot.height_of_tree(bin.root)))
print("is node: {} in our tree: {}".format(value, bin.search(bin.root, value)))
print("inserting value: {} in tree to get new tree {}".format(
    value, bin.insert(bin.root, value)))

bin.display()
