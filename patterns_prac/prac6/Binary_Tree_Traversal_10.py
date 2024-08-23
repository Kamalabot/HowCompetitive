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
def give_head():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(5)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.left.right = TreeNode(6)
    root.left.left = TreeNode(7)

    return root


# Involves visiting all the nodes in a binary tree in a specific order (PreOrder, InOrder, PostOrder).
# intuition 1: using the while loop for iteration requires to maintain stack
# intuition 2: when visiting any node, append the current node to the stack


# intuition 0 : pre, in, post order traversals are variants of depth first search
# intuition 1 : will use stack for in-order traversal of the nodes


def inorder_traversal(root):
    stack = []
    result = []
    current = root
    # while there is stack or current
    while stack or current:
        # while there is current, go left
        while current:
            # append current to stack
            stack.append(current)
            # move current to current's left
            current = current.left
        # pop out the last node into current
        current = stack.pop()
        # append it to result
        result.append(current.val)
        # move to that current node's right
        current = current.right
    return result


def depthFirstPrint(node):
    if node is None:
        return []
    result = []
    stack = [node]
    while stack:
        curr = stack.pop()
        result.append(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return result


def breadthFirstPrint(node):
    if node is None:
        return []
    result = []
    stack = [node]
    while stack:
        curr = stack.pop(0)
        result.append(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return result


root = give_head()
print(inorder_traversal(root))  # Output: [1, 3, 2]

root = give_head()
print(depthFirstPrint(root))  # Output:

root = give_head()
print(breadthFirstPrint(root))  # Output:

# LeetCode Problems:
# 1. PreOrder → Binary Tree Paths (LeetCode #257)
# 2. InOrder → Kth Smallest Element in a BST (LeetCode #230)
# 3. PostOrder → Binary Tree Maximum Path Sum (LeetCode #124)
