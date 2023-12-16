# practicing graph traversals 

# creating logger
import logging
glogger = logging.getLogger('glog')
glogger.setLevel(logging.INFO)
gandle = logging.FileHandler(filename='tlog.txt', mode='w')
gorm = logging.Formatter(fmt='%(message)s | %(levelname)s')
gandle.setFormatter(gorm)
glogger.addHandler(gandle)

# testing logger
glogger.info("logging works")


# creating Node class that can be used for building graph 
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


# New nodes start with no children on their hands
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

# Assigning children to the nodes
a.left = b
a.right = c
b.right = d
c.left = e
d.right = f

# The above assignments have created below tree
#        a
#      /   \
#     b     c
#      \   / 
#       d  e
#        \
#         f


# writing a function to traverse depth first iteratively
def bfs_iterate(start: Node) -> str:
    # check if start node is None
    if start is None:
        return 'No Tree'
    # create a queue using a python list
    node_store = []
    # create a string store
    store = ''
    # assign start node to curr
    curr = start
    # traverse the tree, node by node
    while True:
        # add the start value to the store
        store += str(curr.value) + ' -> '
        # check if right and left children are there
        if curr.right:
            node_store.append(curr.right)
        if curr.left:
            node_store.append(curr.left)
        # if queue is empty
        if len(node_store) == 0:
            return store
        # assign the first node in the queue to curr
        curr = node_store.pop(0)


glogger.info(bfs_iterate(a))  # a -> c -> b -> d -> e -> f    


# writing a function to traverse depth first iteratively
def dfs_iterate(start: Node) -> str:
    # check if start node is None
    if start is None:
        return 'No Tree'
    # create a stack using a python list
    node_stack = []
    # create a string store
    store = ''
    # push one node into node_stack
    node_stack.append(start)
    # traverse the tree, node by node
    while len(node_stack) > 0:
        # assign the first node in the queue to curr
        curr = node_stack.pop(0)
        # add the start value to the store
        store += str(curr.value) + ' -> '
        # check if right and left children are there
        if curr.right:
            node_stack.insert(0, curr.right)
        if curr.left:
            node_stack.insert(0, curr.left)

    return store


glogger.info(dfs_iterate(a))  # a -> b -> d -> f -> c -> e ->


# write a function to recursively traverse the tree

def dfs_recurse(start: Node):
    # base 1: if start is none return ''
    if start is None:
        return ''
    # return by recursively calling self as belo 
    return dfs_recurse(start.right) + ' -> ' + str(start.value) + ' -> ' + dfs_recurse(start.left) 


glogger.info(dfs_recurse(a))  # No Idea
    
