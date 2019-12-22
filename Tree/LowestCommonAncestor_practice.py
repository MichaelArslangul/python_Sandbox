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
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add_right(value)

    def add_left(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add_left(value)

    def __iter__(self):
        if self.root:
            for v in self.root.in_order():
                yield v

class LowestCommonAncestor:
    """
    Given a binary tree, find the lowest common ancestor (LCA)
    of two given nodes in the tree.

    According to the definition of LCA on Wikipedia:
    “The lowest common ancestor is defined between two nodes
    p and q as the lowest node in T that has both p and q as
    descendants (where we allow a node to be a descendant of
    itself).”binary tree O(log(n))implementation.
    """

    def __init__(self, tree):
        self.tree = tree

    def lowest_common_ancestor(self, root, value1, value2):
        if root is None:
            return None
        if root.value == value1 or root.value == value2:
            return root.value
        else:
            left = self.lowest_common_ancestor(root.left, value1, value2)
            right = self.lowest_common_ancestor(root.right, value1, value2)

        if left and right:
            return root.value
        if left and right is None:
            return left
        if left is None and right:
            return right
        return None

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
lca = LowestCommonAncestor(bin)
value1 = 2
value2 = 8
print("Common ancestor of {} and {} is: {}".format(
    value1, value2, lca.lowest_common_ancestor(bin.root, value1, value2)))
