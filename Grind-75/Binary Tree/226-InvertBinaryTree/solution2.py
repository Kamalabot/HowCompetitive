from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Regular Tree node.
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def iTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # left is assigned to right, and right to left
            root.left, root.right = self.iTree(root.right), self.iTree(root.left)
        return root
