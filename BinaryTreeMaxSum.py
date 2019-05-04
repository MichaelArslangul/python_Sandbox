from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTreeMaxSum:
    """
    Given a non-empty binary tree, find the maximum path sum.


    A path is defined as any sequence of nodes from some starting node
    to any node in the tree along the parent-child connections.
    The path must contain at least one node and does not need
    to go through the root.
    """

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _best = float('-inf')
        _visited = []
        _stack = []
        _temp_result = 0

        if root is None:
            return _best
        else:
            _stack.append(root)
            _best = root.val
            while _stack:
                _result = 0
                _temp = _stack.pop()
                _best = max(_temp.val, _best)
                if _temp not in _visited:
                    _visited.append(_temp)
                    if _temp.right:
                        _stack.append(_temp.right)
                        if _temp.left:
                            _result = max(_best, _best + _temp.left.val)
                        _best = max(_temp_result, _temp.right.val, _temp_result + _temp.right.val)
                        _temp_result = 0
                    if _temp.left:
                        _stack.append(_temp.left)
                        _best = max(_best, _temp.left.val + _best)
                        _temp_result += _temp.left.val
        return _best

    def print(self):
        print("depth first search: ")
        for i in self.dfs():
            print(i.value)





tn = TreeNode(-10)
tn.left = TreeNode(9)
tn.left.right = TreeNode(20)
tn.left.right.left = TreeNode(15)
tn.left.right.right = TreeNode(7)
btm = BinaryTreeMaxSum()
print(btm.maxPathSum(tn))


# bin.root.left.add_left(6)
# bin.root.left.add_right(2)
# bin.root.left.right.add_left(7)
# bin.root.left.right.add_right(4)
# bin.root.add_right(1)
# bin.root.right.add_left(0)
# bin.root.right.add_right(8)
# dfs = DFS(bin)
# dfs.print()
