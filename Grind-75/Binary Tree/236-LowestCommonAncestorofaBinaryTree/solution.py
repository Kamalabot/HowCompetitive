# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return root  # If None, then return it
        if root == p or root == q:  # if root is same as p or q
            return root  # return root
        # Find LCA on left and right side of tree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # if both left & right are not None
        if left and right:
            return root  # return None
        else:
            return left or right  # What will this return? Boolean or Node?

# Lowest common ancestor between two nodes p and q as the lowest node in T
# that has both p and q has descendant.