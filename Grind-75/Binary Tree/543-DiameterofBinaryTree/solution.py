from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        self.find_diameter(root)
        return self.answer

    def find_diameter(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return -1  # when root is none, then dia is -1
        # recursively find_dia for left and right nodes
        left, right = self.find_diameter(node.left), self.find_diameter(node.right)
        # store the max of answer compared with dia of left + right + 2
        self.answer = max(self.answer, 2 + left + right)
        # answer = max(0, 2 + 0 + 0) = 2  for the tree with 2 leaf nodes
        return 1 + max(left, right)  # 1 + max(-1, -1) = 0
