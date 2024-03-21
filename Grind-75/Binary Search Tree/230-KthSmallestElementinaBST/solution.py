from typing import Optional
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []  # initialize stack
        # This is a binary search tree, so the elements will be 
        # placed biggest at root and smallest at leaves
        while True:  # start loop
            while root:  # go through the left tree 
                stack.append(root)
                root = root.left
                # till the end

            root = stack.pop()  # pop the top node
            k -= 1  # decrement k?
            if not k:  # if k is 0
                return root.val  # return the root's value
            root = root.right  # shift to the right side of the tree
