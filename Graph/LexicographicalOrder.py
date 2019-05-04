# class TreeNode:
#
#     def __init__(self, value):
#         self.value = value
#         self.child = []
#
#     def add(self,value):
#         node = TreeNode(value)
#         self.child.append(node)
#
#     def traverse(self):
#         if self.value:
#             yield self.value
#             for child in self.child.traverse():
#                 yield child
#
#
# class LexTree:
#
#     def __init__(self, height):
#         self.height = height
#         self.root = TreeNode(0)
#
#     def build_tree(self):
#         _height = len(str(self.height))
#         if _height == 0:
#             return self.root.value
#         elif _height == 1:
#             for i in range(1, 10):
#                 self.root.add(i)
#         elif _height > 1:
#             node = self.root
#             self._next_order(node)
#             for _ in range(2, _height + 1):
#                 for child_node in node.child:
#                     self._next_order(child_node)
#
#     def _next_order(self, node):
#         for i in range(1, 10):
#             node.add(node.value *10 + i)
#         return node
#
#     def __repr__(self):
#         for v in self.root.traverse():
#             print(v)

class Lexicographicalorder:
    """
    Leetcode 386
    """
    def lexical_order(self, number):
        _result = []
        for i in range(1, 10):
            self.dfs(i, number, _result)
        return _result

    def dfs(self, curr, target, result):
        if curr <= target:
            result.append(curr)
            _next_order = 10*curr
            if _next_order <= target:
                for i in range(10):
                    self.dfs(_next_order + i, target, result)




lo = Lexicographicalorder()
number = 100000

print("lexicogaphical order for number {} is: {}".format(
    number, lo.lexical_order(number)))
