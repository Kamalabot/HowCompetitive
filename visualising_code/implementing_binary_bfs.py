class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

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

# Explore the level fully before going down the next level

def breadthFirstPrint(node):
    queue = [node] # The node provided is the root, and it is immediately pushed into stack
    # algo has to run if there something in stack. 
    # If nothing in stack, means the operation is completed
    while len(queue) > 0:
        curr = queue.pop(0) # this means the particular node has been visited
        print(curr.val)
        # Add curr's children to the stack. It must be non-null

        # The append will push the element in the back, which is required here
        # by doing that, the breadth first traversal happens
        if curr.right is not None:
            queue.append(curr.right)

        if curr.left is not None:
            queue.append(curr.left)

breadthFirstPrint(a)

# Problem: Given a bfs(root, target) binary tree, check if the "target"
# return True if Target present, else False 


def bfs_target(node, target):
    queue = [node] # The node provided is the root, and it is immediately pushed into stack
    # algo has to run if there something in stack. 
    # If nothing in stack, means the operation is completed
    while len(queue) > 0:
        curr = queue.pop(0) # this means the particular node has been visited
        if curr.val == target:
            return True
        # Add curr's children to the stack. It must be non-null

        # The append will push the element in the back, which is required here
        # by doing that, the breadth first traversal happens
        if curr.right is not None:
            queue.append(curr.right)

        if curr.left is not None:
            queue.append(curr.left)
    
    return False


print(bfs_target(a, 'f'))
print(bfs_target(a, 'n'))

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


def bfs_sum(node):
    queue = [node] # The node provided is the root, and it is immediately pushed into stack
    # algo has to run if there something in stack. 
    # If nothing in stack, means the operation is completed
    sum = 0
    while len(queue) > 0:
        curr = queue.pop(0) # this means the particular node has been visited
        sum = sum + curr.val 
        # Add curr's children to the queue. It must be non-null

        # The append will push the element in the back, which is required here
        # by doing that, the breadth first traversal happens
        if curr.right is not None:
            queue.append(curr.right)

        if curr.left is not None:
            queue.append(curr.left)
    
    return sum


print(bfs_sum(a))
