# at each level of tree extract
# nodes beadth first, and place in
# seperate lists
import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []  # node is none, then empty list
        # initialize queue, which does FiFo
        queue, output_list = collections.deque([root]), []
        # initialize output_list that stores breadthfirst data
        while queue:  # when there data in queue
            level = []
            # why ?? each level data is appended here
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            output_list.append(level)

        return output_list
