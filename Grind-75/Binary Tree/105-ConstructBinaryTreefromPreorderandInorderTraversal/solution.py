from logging import root
from typing import List, Optional


# Tree is constructed from 2 lists of elements provided 
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:
        # Only the node needs to be returned, after the tree 
        # has been built
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            # Tree is built inside this fn
            nonlocal preorder_index
            # nonlocal refers to var outside scope
            if left > right:
                return None

            root_value = preorder[preorder_index]
            # preorder_index is used for getting values
            root_node = TreeNode(root_value)  # root node is created
            preorder_index += 1  # idx is icremented on every call
            # the sub tree are generated recursively
            root_node.left = array_to_tree(left, inorder_map[root_value] - 1)
            # and attached to left and right of root nodes
            root_node.right = array_to_tree(inorder_map[root_value] + 1, right)
            # value's indices are taken from inorder_map

            return root_node  # this final root node

        inorder_map = {}
        preorder_index = 0
        for index, value in enumerate(inorder):
            inorder_map[value] = index

        return array_to_tree(0, len(preorder)-1)
