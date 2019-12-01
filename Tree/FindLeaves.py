class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Pattern():
    def getLeafs(self,root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        leaves = self.getLeafs(root.left) + self.getLeafs(root.right)
        return leaves

    def similar_leaf(self, root1, root2):
        return self.getLeafs(root1) == self.getLeafs(root2)


#simple test
root= Node(3)
root.left = Node(5)
root.right= Node(1)

root.left.left =  Node(6)
root.left.right =  Node(2)
root.left.right.left =Node(7)
root.left.right.right =Node(4)

root.right.left =  Node(9)
root.right.right =  Node(8)

pattern =Pattern()
print(pattern.getLeafs(root))
