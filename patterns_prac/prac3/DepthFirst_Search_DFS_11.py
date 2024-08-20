# Pattern: Depth-First Search (DFS)
# Introduction:
# A traversal technique that explores as far down a branch as possible before backtracking.

# Sample Problem:
# Find all paths from the root to leaves in a binary tree.

# intuition0: Need to get the path for each node, and track it
# intuition1: Need to start the stack with root and its value, as tuple
# intuition2: append the right and left node to stack, along with curr path value
# intuition3: node, and path are popped for each element in the stack


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root):
    if not root:
        return []
    paths = []
    stack = [(root, str(root.val))]
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            paths.append(path)
        if node.right:
            stack.append((node.right, path + "->" + str(node.right.val)))
        if node.left:
            stack.append((node.left, path + "->" + str(node.left.val)))
    return paths


def binary_tree_paths_prac(root):
    if not root:
        return []

    paths = []
    stack = [(root, str(root.val))]
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            paths.append(path)
        if node.right:
            stack.append((node.right, path + " ->" + str(node.right.val)))
        if node.left:
            stack.append((node.left, path + "->" + str(node.left.val)))
    return paths


# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
print(binary_tree_paths(root))  # Output: ["1->2->5", "1->3"]

# Example:
root = [1, 2, 3, None, 5]
# Output: ["1->2->5", "1->3"]

# LeetCode Problems:
# 1. Clone Graph (LeetCode #133)
# 2. Path Sum II (LeetCode #113)
# 3. Course Schedule II (LeetCode #210)
