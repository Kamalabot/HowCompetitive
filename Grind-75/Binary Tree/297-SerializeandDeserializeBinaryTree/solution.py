from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> Optional[str]:
        if root is None:
            return ""

        output_list = []
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    output_list.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    output_list.append("#")

        return " ".join(output_list)  # provides the string output

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None

        i = 0
        binary_tree = data.split()
        root = TreeNode(binary_tree[0])  # start with root node
        queue = deque([root])
        while queue:
            node = queue.popleft()
            i += 1
            if i < len(binary_tree) and binary_tree[i] != "#":
                # loop until there is list elems avbl & '#' is not reached
                node.left = TreeNode(int(binary_tree[i]))
                # create nodes and attach to left
                queue.append(node.left)

            i += 1
            if i < len(binary_tree) and binary_tree[i] != "#":
                # loop until there is list elems avbl & '#' is not reached
                node.right = TreeNode(int(binary_tree[i]))
                # create nodes and attach to right 
                queue.append(node.right)

        return root
        # once built return tree