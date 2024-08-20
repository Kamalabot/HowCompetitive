# Pattern: Binary Tree Traversal
# Introduction:

# Sample Problem:

# Perform all traversals in binary tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_recurse_pre(node):
    if node is None:
        return
    print(node.val)
    dfs_recurse_pre(node.left)
    dfs_recurse_pre(node.right)


def dfs_recurse_in(node):
    if node is None:
        return
    dfs_recurse_in(node.left)
    print(node.val)
    dfs_recurse_in(node.right)


def dfs_recurse_post(node):
    if node is None:
        return
    dfs_recurse_post(node.left)
    dfs_recurse_post(node.right)
    print(node.val)


# Involves visiting all the nodes in a binary tree in a specific order (PreOrder, InOrder, PostOrder).
# intuition 1: using the while loop for iteration requires to maintain stack
# intuition 2: when visiting any node, append the current node to the stack


# intuition 0 : pre, in, post order traversals are variants of depth first search
# intuition 1 : will use stack for in-order traversal of the nodes
def inorder_traversal(root):
    result = []
    stack = []
    current = root
    # root is assigned to current node
    while current or stack:
        # while there are elements in stack
        while current:
            # keep on going to left nodes
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result


def depthFirstPrint(node):
    stack = [node]
    while len(stack) > 0:
        curr = stack.pop(0)
        print(curr.val)
        if curr.left is not None:
            stack.insert(0, curr.left)
        if curr.right is not None:
            stack.insert(0, curr.right)


def breadthFirstPrint(node):
    stack = [node]
    while len(stack) > 1:
        curr = stack.pop(0)
        print(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)


# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(inorder_traversal(root))  # Output: [1, 3, 2]
print(depthFirstPrint(root))  # Output:

# LeetCode Problems:
# 1. PreOrder → Binary Tree Paths (LeetCode #257)
# 2. InOrder → Kth Smallest Element in a BST (LeetCode #230)
# 3. PostOrder → Binary Tree Maximum Path Sum (LeetCode #124)
