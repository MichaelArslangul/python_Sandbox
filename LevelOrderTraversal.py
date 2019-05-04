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

    def level_order_traversal(self):
        _my_queue = deque()
        _visited = []
        _result = []
        if self.root is not None:
            _my_queue.append(self.root)
        while _my_queue:
            _temp = _my_queue.popleft()
            _result.append(_temp.value)
            if _temp.left is not None:
                _my_queue.append(_temp.left)
            if _temp.right is not None:
                _my_queue.append(_temp.right)
        return _result

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
bin.root.right.left.add_left(9)
bin.root.right.left.add_right(10)
print(bin.level_order_traversal())
