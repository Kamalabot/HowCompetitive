class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d 
b.right = e
c.right = f

#        a
#       / \
#      b   c
#     /\    \
#    d  e    f

def depthFirstPrint(node):
    stack = [node] # The node provided is the root, and it is immediately pushed into stack
    # algo has to run if there something in stack. 
    # If nothing in stack, means the operation is completed
    while len(stack) > 0:
        curr = stack.pop(0) # this means the particular node has been visited
        print(curr.val)
        # Add curr's children to the stack. It must be non-null

        # The append will push the element to the back, which is like queue
        # by doing that, the breadth first traversal happens
        if curr.right is not None:
            stack.insert(0, curr.right)

        if curr.left is not None:
            stack.insert(0, curr.left)

# depthFirstPrint(a)

def dfs_recursive(node):
    if node is None:
        return
    print(node.val)
    dfs_recursive(node.left)
    dfs_recursive(node.right)


# dfs_recursive(a)


def dfs_preorder(node):
    if node is None:
        return
    print(node.val)
    dfs_preorder(node.left)
    dfs_preorder(node.right)


def dfs_postorder(node):
    if node is None:
        return
    dfs_postorder(node.left)
    dfs_postorder(node.right)
    print(node.val)


def dfs_inorder(node):
    if node is None:
        return
    dfs_inorder(node.left)
    print(node.val)
    dfs_inorder(node.right)

# print("******post*********")
# dfs_postorder(a)
# print("******pre*********")
# dfs_preorder(a)
# print("******InOrder*******")
# dfs_inorder(a)
 
# Solving the tree to return the Sum of the values in the tree
# 
a = Node(2) 
b = Node(3) 
c = Node(7) 
d = Node(4) 
e = Node(-2) 
f = Node(8) 

a.left = b
a.right = c
b.left = e
b.right = f
c.right = d


def dfs_sum(node): 
    if node is None:
        return 0
    # Single line solution... 
    return dfs_sum(node.right) + node.val + dfs_sum(node.left)


print(dfs_sum(a))