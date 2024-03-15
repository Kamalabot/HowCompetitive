from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:  # depth is 0 if root is none / leaf
            return 0
        # recursively call left and right nodes on maxDepth & 
        # extract the max value
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        # if leaf node then add 1 and return
