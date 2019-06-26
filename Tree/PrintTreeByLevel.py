from collections import deque, defaultdict

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

    def height_of_tree(self, node):
        if not node:
            return 0
        else:
            _left = self.height_of_tree(node.left)
            _right = self.height_of_tree(node.right)
        return 1 + max(_left, _right)

    def print_by_level_using_counters(self):
        _queue = deque()
        _level_count = 0
        _current_count = 0

        if self.root:
            _queue.append(self.root)
        while _queue:
            _temp = _queue.popleft()
            _level_count += 1
            print(_temp.value)
            _level_count -= 1
            if _temp.left:
                _queue.append(_temp.left)
                _current_count +=1
            if _temp.right:
                _queue.append(_temp.right)
                _current_count +=1
            if _current_count > 0 and _level_count == 0:
                print('\n')
                _current_count = _level_count
                _level_count = 0
            elif _current_count ==0 and _level_count == 0:
                break

    def print_by_level(self):
        _item_by_level = {}
        _level = 0
        _queue = deque()
        _visited = []
        if self.root:
            _queue.append(self.root)
            _queue.append("end")
            _item_by_level[_level] = self.root.value
        while _queue:
            _temp = _queue.popleft()
            if _temp  != "end" and _temp not in _visited:
                _visited.append(_temp)
                if _temp.left:
                    _queue.append(_temp.left)
                if _temp.right:
                    _queue.append(_temp.right)
            elif _temp == "end" and _queue:
                _list = []
                for _node in _queue:
                    _list.append(_node.value)
                _level += 1
                _item_by_level[_level] = _list
                _queue.append("end")
            elif _temp == "end" and not _queue:
                break
        return _item_by_level



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

print("height of tree is: {}".format(bin.height_of_tree(bin.root)))
print("tree by level: {}".format(bin.print_by_level()))
print("tree by level: {}".format(bin.print_by_level_using_counters()))
