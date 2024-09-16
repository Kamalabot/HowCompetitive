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
def populate():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(5)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.left.right = TreeNode(6)
    root.left.left = TreeNode(7)
    return root


# intuition 0 : pre, in, post order traversals are variants of depth first search
# intuition 1 : will use stack for in-order traversal of the nodes


def dfs_recurse_pre(node):
    pass


def dfs_recurse_in(node):
    pass


def dfs_recurse_post(node):
    pass


# Involves visiting all the nodes in a binary tree in a specific order (PreOrder, InOrder, PostOrder).
# - results and stack are maintained individualy
#
# - curr is the node that is provided, the root one
#
# - while loop on curr or stack and then inner while on curr
#
#   > inner while left side is checked, and appended to stack
#
# - in outer while stack is poped on curr and value appended to result
#
# - right node is assigned to curr
def inorder_traversal(root):
    pass


def depthFirstPrint(node):
    pass


def breadthFirstPrint(node):
    pass


root = populate()
print(inorder_traversal(root))  # Output: [1, 3, 2]

root = populate()
print(depthFirstPrint(root))  # Output:

root = populate()
print(breadthFirstPrint(root))  # Output:

# LeetCode Problems:
# 1. PreOrder → Binary Tree Paths (LeetCode #257)
# 2. InOrder → Kth Smallest Element in a BST (LeetCode #230)
# 3. PostOrder → Binary Tree Maximum Path Sum (LeetCode #124)
