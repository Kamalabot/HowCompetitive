# Pattern: Binary Tree Traversal
# Introduction:
# Involves visiting all the nodes in a binary tree in a specific order (PreOrder, InOrder, PostOrder).

# Sample Problem:
# Perform inorder traversal of a binary tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# intuition 1 : will use stack for in-order traversal of the nodes
def inorder_traversal(root):
    result = []
    stack = []
    current = root
    # root is assigned to current node
    while current or stack:
        # while there are elements in stack
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result


def depthFirstPrint(node):
    stack = [
        node
    ]  # The node provided is the root, and it is immediately pushed into stack
    # algo has to run if there something in stack.
    # If nothing in stack, means the operation is completed
    while len(stack) > 0:
        curr = stack.pop(0)  # this means the particular node has been visited
        print(curr.val)
        # Add curr's children to the stack. It must be non-null

        # The append will push the element to the back, which is like queue
        # by doing that, the breadth first traversal happens
        if curr.right is not None:
            stack.insert(0, curr.right)

        if curr.left is not None:
            stack.insert(0, curr.left)


# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(inorder_traversal(root))  # Output: [1, 3, 2]
print(depthFirstPrint(root))  # Output:

# LeetCode Problems:
# 1. PreOrder → Binary Tree Paths (LeetCode #257)
# 2. InOrder → Kth Smallest Element in a BST (LeetCode #230)
# 3. PostOrder → Binary Tree Maximum Path Sum (LeetCode #124)
