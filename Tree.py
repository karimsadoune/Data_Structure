class Node:
    def __init__(self, key):
        self.val = key
        self.right = None
        self.left = None

    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')


def isFullTree(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left and root.right:
        return isFullTree(root.left) and isFullTree(root.right)
    return False


def calculateDepth(node):
    d = 0
    while node:
        d += 1
        node = node.left
    return d


def is_perfect(root, d, level=0):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return d == level + 1

    if root.left is None or root.right is None:
        return False

    return is_perfect(root.left, d, level+1) and is_perfect(root.right, d, level+1)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(4)
    root.right.right = Node(5)
    """
    print("Pre order Traversal: ", end="")
    root.traversePreOrder()
    print("\nIn order Traversal: ", end="")
    root.traverseInOrder()
    print("\nPost order Traversal: ", end="")
    root.traversePostOrder()
    """
    if isFullTree(root):
        print("the tree is Full")
    else:
        print("the tree isn't Full")
    print(calculateDepth(root))

    if is_perfect(root, calculateDepth(root)):
        print("The tree is a perfect binary tree")
    else:
        print("The tree is not a perfect binary tree")