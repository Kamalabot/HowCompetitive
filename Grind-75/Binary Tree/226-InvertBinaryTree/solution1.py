# Inverting the children is changing the left child to 
# right, and vice versa

from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Tree node similar to any other graph node
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:  # when root is not none
            root.left, root.right = self.inverter(root.left, root.right)
        # if root is none, then return it directly
        return root

    def inverter(self, left_child: Optional[TreeNode],
                 right_child: Optional[TreeNode]) -> List[TreeNode]:
        # when left child/ node is not None
        if left_child is not None:
            # invert its children
            left_child.left, left_child.right = self.inverter(left_child.left,
                                                              left_child.right)
        # when right child/ node is not None
        if right_child is not None:
            # invert its children
            right_child.left, right_child.right = self.inverter(right_child.left,
                                                                right_child.right)
        # return right_child and then left_child
        return right_child, left_child  # the return is swapping the children
        # so when it is assigned in the calling expression, the swap happens

