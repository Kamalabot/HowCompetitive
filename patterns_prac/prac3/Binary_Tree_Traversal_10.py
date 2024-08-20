# Pattern: Binary Tree Traversal
# Introduction:

# Sample Problem:

# Perform all traversals in binary tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(5)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.left = TreeNode(7)


def dfs_recurse_pre(node):
    if node is None:
        return None
    print(node.val)
    dfs_recurse_pre(node.left)
    dfs_recurse_pre(node.right)


def dfs_recurse_in(node):
    if node is None:
        return None
    dfs_recurse_pre(node.left)
    print(node.val)
    dfs_recurse_pre(node.right)


def dfs_recurse_post(node):
    if node is None:
        return None
    dfs_recurse_pre(node.left)
    dfs_recurse_pre(node.right)
    print(node.val)


# Involves visiting all the nodes in a binary tree in a specific order (PreOrder, InOrder, PostOrder).
# intuition 0: result and the stack are maintained in different lists
# intuition 1: using the while loop for iteration requires to maintain stack
# intuition 2: when visiting any node, append the current node(head) to the stack
# intuition 3: make the current.left as current


def inorder_traversal(root):
    result = []
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
            # result.append(current.val)
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result


def depthFirstPrint(node):
    print("enterin")
    if node is None:
        return None
    string = ""
    stack = [node]
    while len(stack) > 0:
        curr = stack.pop()
        print(curr.val)
        string += str(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return string


def breadthFirstPrint(node):
    if node is None:
        return None
    string = ""
    stack = [node]
    while len(stack) > 0:
        curr = stack.pop(0)
        print(curr.val)
        string += str(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return string


print(inorder_traversal(root))  # Output: [1, 3, 2]

# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(5)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.left = TreeNode(7)

print(depthFirstPrint(root))  # Output:

# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(5)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.left = TreeNode(7)

print(breadthFirstPrint(root))  # Output:

# LeetCode Problems:
# 1. PreOrder → Binary Tree Paths (LeetCode #257)
# 2. InOrder → Kth Smallest Element in a BST (LeetCode #230)
# 3. PostOrder → Binary Tree Maximum Path Sum (LeetCode #124)
