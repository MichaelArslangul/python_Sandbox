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


class DFS:
    """
    Depth First Search using a stack
    """

    def __init__(self, tree):
        self.tree = tree


    def dfs(self):
        _stack = []
        visited = []
        _result = []
        if self.tree.root is None:
            raise Exception("Can't traverse an empty tree")
        else:
            _stack.append(self.tree.root)
            while _stack:
                _temp_node = _stack.pop()
                if _temp_node not in visited:
                    visited.append(_temp_node)
                    if _temp_node.right:
                        _stack.append(_temp_node.right)
                    if _temp_node.left:
                        _stack.append(_temp_node.left)
        return visited

    def print(self):
        print("depth first search: ")
        for i in self.dfs():
            print(i.value)





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
dfs = DFS(bin)
dfs.print()
