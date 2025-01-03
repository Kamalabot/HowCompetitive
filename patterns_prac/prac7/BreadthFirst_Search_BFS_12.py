# Pattern: Breadth-First Search (BFS)
# Introduction:
# A traversal technique that explores nodes level by level in a tree or graph.

# Sample Problem:
# Perform level-order traversal of a binary tree.
# intuition 1: Breadth-First is also called Level Order traversal
# intuition 2: Will be using queue to store and extract the elements

from collections import deque


class TreeNode:
    # observe the attr is having left and right
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lorder(root):
    if not root:
        return []
    queue = deque([root])
    nodes = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        nodes.append(level)
    return nodes


# intuition 1: Deque is used as queue
# intuition 2: At each level, the nodes are collected
# intuition 3: Enumerate for loop the queue elements and append vals to level
# intuition 4: look at the right and left of each elm and append to queue
# intuition 5: levels are appended finally to nodes and returned


def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        # there is additional list for the level
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


# Example usage:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(level_order(root))  # Output: [[3], [9, 20], [15, 7]]

# LeetCode Problems:
# 1. Binary Tree Level Order Traversal (LeetCode #102)
# 2. Rotting Oranges (LeetCode #994)
# 3. Word Ladder (LeetCode #127)
