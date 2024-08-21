# Pattern: Binary Tree Traversal
# Introduction:

# Sample Problem:

# Perform all traversals in binary tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(5)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.left = TreeNode(7)


def dfs_recurse_pre(node):
    if head is None:
        return None
    print(node.val)
    dfs_recurse_pre(node.left)
    dfs_recurse_pre(node.right)


def dfs_recurse_in(node):
    if head is None:
        return None
    dfs_recurse_pre(node.left)
    print(node.val)
    dfs_recurse_pre(node.right)


def dfs_recurse_post(node):
    if head is None:
        return None
    dfs_recurse_pre(node.left)
    dfs_recurse_pre(node.right)
    print(node.val)


# Involves visiting all the nodes in a binary tree in a specific order (PreOrder, InOrder, PostOrder).
# intuition 1: using the while loop for iteration requires to maintain stack
# intuition 2: when visiting any node, append the current node to the stack


# intuition 0 : pre, in, post order traversals are variants of depth first search
# intuition 1 : will use stack for in-order traversal of the nodes
def inorder_traversal(root):
    if root is None:
        return None
    current = root
    stack = []
    elms = []
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        elms.append(current.val)
        current = current.right
    return elms


def depthFirstPrint(node):
    if node is None:
        return None

    stack = [node]
    result = []

    while len(stack) > 0:
        curr = stack.pop()
        result.append(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)

    return result


def breadthFirstPrint(node):
    if node is None:
        return None

    stack = [node]
    result = []

    while len(stack) > 0:
        curr = stack.pop(0)
        result.append(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)

    return result


print(inorder_traversal(root))  # Output: [1, 3, 2]

# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(5)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.left = TreeNode(7)


print(depthFirstPrint(root))  # Output:

# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(5)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.left = TreeNode(7)

print(breadthFirstPrint(root))  # Output:

# LeetCode Problems:
# 1. PreOrder → Binary Tree Paths (LeetCode #257)
# 2. InOrder → Kth Smallest Element in a BST (LeetCode #230)
# 3. PostOrder → Binary Tree Maximum Path Sum (LeetCode #124)
