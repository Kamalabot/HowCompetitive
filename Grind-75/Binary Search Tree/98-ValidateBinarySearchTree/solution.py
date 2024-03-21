from typing import Optional
# The left subtree of a node contains only nodes with keys less than the 
# node's key. The right subtree of a node contains only nodes with keys
# greater than the node's key. Both the left and right subtrees must
# also be binary search trees.
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode],
                   ceil: int = float("inf"),
                   floor: int = float("-inf")) -> bool:
        if not root:
            return True  # if null also return True, Why?
        # check the floor & ceil with the root's value
        if floor < root.val < ceil:
            # in order traversal using recursion
            return self.isValidBST(root.left, root.val, floor) and self.isValidBST(root.right, ceil, root.val)
        else:
            return False


def checkBST(root: TreeNode):

    if root is None:
        return True
        # root is none, return True

    queue = [root]
    # initiate queue and append root into it
    while queue:  # loop until queue has elements
        curr = queue.pop(0)  # pop element at 0
        if curr.left is not None:  # check if left is not None
            queue.append(curr.left)
            print(curr.left.val)
            # append it to the queue
            if curr.left.val > root.val:
                # if left val is bigger then return false
                return False
        if curr.right is not None:  # check if right is not None
            queue.append(curr.right)
            print(curr.right.val)
            # append it to the queue
            if curr.right.val > root.val:
                # if right val is bigger then return false
                return False
        return True

# implement the above traversal using while loop, by checking the nodes
# think how to manage the null value


root = [2, 1, 3]  # to test the tree needs to be built from list

# sol = Solution()
# print(sol.isValidBST(root))