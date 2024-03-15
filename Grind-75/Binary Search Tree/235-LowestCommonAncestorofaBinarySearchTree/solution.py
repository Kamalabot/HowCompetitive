# Lowest Common Ancestor is the lowest
# node in tree T that has both P & Q as
# descendants. Node can be descendant
# of itself

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        max_value, min_value = max(p.val, q.val), min(p.val, q.val)
        # get the max and min between the given nodes
        while root:  # when root is not None
            if root.val > max_value:
                root = root.left  # root is shifted to left
            elif root.val < min_value:
                root = root.right  # root is shifted to right
            else:
                return root
        # while loop traverses the tree till the end
        # leaves of the given p and q nodes.