from collections import deque

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

    def remove(self, node):
        pass

    def __iter__(self):
        if self.root:
            for v in self.root.in_order():
                yield v

    def __contains__(self, target):
        if self.root is not None:
            for v in self.root.in_order():
                if v == target:
                    return True

        return False


class LCA:
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


    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.value == p.value or root.value == q.value:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left or right:
            return left or right





bin = BinaryTree()
bin.add_right(3)
bin.root.add_left(5)
bin.root.left.add_left(6)
bin.root.left.add_right(2)
bin.root.left.right.add_left(7)
bin.root.left.right.add_right(4)
bin.root.add_right(1)
bin.root.right.add_left(0)
bin.root.right.add_right(8)
lca = LCA(bin)
result = lca.lowestCommonAncestor(bin.root, bin.root, bin.root.right)
print("result: {}".format(result.value))
