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


print("Pre Order: \n")
dfs_recurse_pre(root)

print("In Order: \n")
dfs_recurse_in(root)

print("Post Order: \n")
dfs_recurse_post(root)

# Involves visiting all the nodes in a binary tree in a specific order (PreOrder, InOrder, PostOrder).
# intuition 1: using the while loop for iteration requires to maintain stack
# intuition 2: when visiting any node, append the current node to the stack


# intuition 0 : pre, in, post order traversals are variants of depth first search
# intuition 1 : will use stack for in-order traversal of the nodes
def inorder_traversal_01(root):
    if root is None:
        return None
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        if curr.left:
            stack.insert(0, curr.left)
            # print(curr.left.val)
        print(curr.val)
        if curr.right:
            stack.insert(0, curr.right)
            # print(curr.right.val)


def inorder_traversal(head):
    # this is correct in order traversal
    result = []
    stack = []
    current = head
    print(current)
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
            print("reaching...")
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result


print("In order 01 While loop")
inorder_traversal_01(root)

print("In order While loop")
print(inorder_traversal(root))


def depthFirstPrint(node):
    stack = [node]
    while len(stack) > 0:
        curr = stack.pop(0)
        print(curr.val)
        if curr.left is not None:
            stack.insert(0, curr.left)
        if curr.right is not None:
            stack.insert(0, curr.right)


def breadthFirstPrint(node):
    stack = [node]
    while len(stack) > 0:
        curr = stack.pop(0)
        print(curr.val)
        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)


print("depth first While loop")
depthFirstPrint(root)  # Output:

print("Breadth first While loop")
breadthFirstPrint(root)

# LeetCode Problems:
# 1. PreOrder → Binary Tree Paths (LeetCode #257)
# 2. InOrder → Kth Smallest Element in a BST (LeetCode #230)
# 3. PostOrder → Binary Tree Maximum Path Sum (LeetCode #124)
