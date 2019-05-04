class BinraryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            self.left = self.addSubtree(self.left, value)
        elif value > self.value:
            self.right = self.addSubtree(self.right, value)

    def addSubtree(self, parent, value):
        if parent is None:
            return BinraryNode(value)
        else:
            parent.add(value)
            return parent

    def remove(self, value):
        if value < self.value:
            self.left = self.removeTree(self.left, value)
        elif value > self.value:
            self.right = self.removeTree(self.right, value)
        else:
            if self.left is None:
                return self.right
            child = self.left
            while child.right:
                child = child.right
            childkey = child.value
            self.left = self.removeTree(self.left, childkey)
            self.value = childkey

    def removeTree(self, parent, value):
        if parent is not None:
            return parent.remove(value)
        return None

class BinaryTree:
    """ binary tree O(log(n))implementation.
    """
    def __init__(self):
        self.root = None

    def getMin(self):
        if self.root is None:
            raise ValueError("No min or max in a null tree")
        n = self.root
        while n.left:
            n = n.left
        return n.value

    def getMax(self):
        if self.root is None:
            raise ValueError("No min or max in a null tree")
        n = self.root
        while n.right:
            n = n.right
        return n.value

    def closest_node(self, target):
        if self.root is None:
            raise ValueError("Can't compute closest value in a null tree")

        node = self.root
        best = node
        distance = abs(node.value - target)

        while node:
            if abs(node.value - target) < distance:
                best = node
                distance = abs(node.value - target)
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return target
        return best.value

    def add(self, value):
        if self.root is None:
            self.root =  BinraryNode(value)
        else:
            self.root.add(value)


    def remove(self, value):
        if self.root is not None:
            self.root.remove(value)

    def __contains__(self, target):
        node = self.root
        while node is not None:
            if target < node.value:
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True
        return False
