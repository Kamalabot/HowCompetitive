# Depth of the 2 subtrees of every node never differs by 
# more than one.

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    # usual Tree Node with Left and Right
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True  # the empty tree will be balanced

        self.memo = {}  # self is initialized before find_depth is called
        subtrees_height_diff = abs(self.find_depth(root.left)-self.find_depth(root.right))
        # recursively finds the height diff between the left and right
        # sub-tree recursively
        is_tree_balanced = subtrees_height_diff < 2
        return is_tree_balanced and self.isBalanced(root.left) and self.isBalanced(root.right)
        # recursively checks the left and right sub-trees

    def find_depth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            # depth of None node is 0
            return 0
        if node not in self.memo:
            self.memo[node] = max(self.find_depth(node.left),
                                  self.find_depth(node.right)) + 1
        # leaf nodes will return 0 every level above will have depth 
        # incremementing by 1, with the root node having the max depth
        return self.memo[node]

# isBalanced(treeNode)  will be called