# class BinaryNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def add_left(self, value):
#         _node = BinaryNode(value)
#         _node.left = self.left
#         self.left = _node
#
#     def add_right(self, parent, value):
#         _node = BinaryNode(value)
#         _node.right = self.right
#         self.right = _node
#
#     def in_order(self):
#         if self.left:
#             for node in self.left.in_order():
#                 yield node
#
#         yield self.value
#
#         if self.right:
#             for node in self.right.in_order():
#                 yield node

class BinaryTree:
    def __init__(self):
        self.value = value
        self.left = None
        self.right = None

class AlgebricTree:
    """ binary tree O(log(n))implementation.
    """
    def __init__(self):
        self.open_param = '('
        self.closing_param = ')'
        self.operations = ['+', '-', '*', '/']
        self.digits = [_ for _ in range(10)]


    # def add(self, value):
    #     stack =[]
    #
    #     if value in self.operations:
    #         self._stack.append(value)
    #     elif value in self.digits:
    #         self._stack.append(AlgebricTree(value))
    #     elif value == self.closing_param:
    #         right_operand = _stack.pop()
    #         operator = _stack.pop()
    #         left_operand = _stack.pop()
    #         self._stack.append(AlgebricTree(operator, left_operand,right_operand))
    #     return _stack
        #     if self.root is None:
        #         self.root = node
        #     else:
        #         self.root.left = node
        #     self._stack.append(self)
        # print(self)
        #
        # elif value == self.closing_param:
        #     pass
        # elif value in self.operations:
        #     pass
        # elif value in self.digits:
        #     pass

    def build_tree(self, expression):
        stack  = []

        for val in expression:
            if val == self.open_param:
                tree = BinaryTree('')
                stack.append(tree)
            elif val in self.digits:
                tree = BinaryTree(val)
                stack.append(tree)
            elif val in operations:
                tree = BinaryTree(val)
                left = stack.pop()
                right = stack.pop()

    def execute_expression(self):
        pass
        # if node.value == '+':
        #     return self.calc(node.left) + self.calc(node.right)
        # if node.value == '-':
        #     return self.calc(node.left) - self.calc(node.right)
        # if node.value == '*':
        #     return self.calc(node.left) * self.calc(node.right)
        # if node.value == '/':
        #     return self.calc(node.left) / self.calc(node.right)
        # else:
        #     return node.value

    def calc(self, expression):
        self.build_tree(expression)
        return self.execute_expression()

    def __contains__(self, value):
        if self.root:
            for v in self.root.in_order():
                yield v

    def __iter__(self):
        if self.root:
            for v in self.root.in_order():
                yield v

    def in_order(self):
        for node in
    # def __str__(self):
    #     for node in self:
    #         print(node.value)

# class AlgebricTree:
#
#     def __init__(self):
#         self.open_param = '('
#         self.closing_param = ')'
#         self.operations = ['+', '-', '*', '/']
#         self.digits = [_ for _ in range(10)]
#         self.bin = BinaryTree()
#
#     def build_tree(self, expression):
#         _stack = []
#         a_tree = BinaryTree()
#
#         for _char in expression:
#             if _char in self.operations:
#                 a_tree.add_left(_char)
#                 node.left = _stack.pop()
#                 node.right = _stack.pop()
#             else:
#                 node = a_tree.add_left(_char)
#             _stack.append(node)
#         return _stack
#
#     def calc(self, node):
#         if node.value == '+':
#             return self.calc(node.left) + self.calc(node.right)
#         if node.value == '-':
#             return self.calc(node.left) - self.calc(node.right)
#         if node.value == '*':
#             return self.calc(node.left) * self.calc(node.right)
#         if node.value == '/':
#             return self.calc(node.left) / self.calc(node.right)
#         else:
#             return node.value
#
#     def evaluate_expression(self, equation):
#         _stack = self.build_tree(equation)
#         root = _stack.pop()
#         print(self.calc(root))


expression = "((7+3)∗(5−2))"
at = AlgebricTree()
print("evaluate tree: {}".format(at.calc(expression)))
