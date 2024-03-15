from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        output_list = []
        queue = deque([root])
        # queue helps traversing the tree breadth first
        while queue:
            temp = []  # collect the node values
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)  # append val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            output_list.append(temp[-1])
            # only the right val is appended to 
            # output_list

        return output_list
