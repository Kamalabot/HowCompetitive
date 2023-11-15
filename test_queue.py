# Practice script for implementing the graph representation as nodes
# and traversing it breadth first and depth first for "binary tree" 
class Node:
    def __init__(self, value) -> None:
        self.value: str | int = value
        self.right: Node = None
        self.left: Node = None

    def __str__(self):
        return str(self.value)


# Starting the breadth first traversal of the nodes
# def traverse_bfs(node):
#     """Takes a head of a binary tree and prints out all the 
#     nodes value. """
#     # create the string that is going to returned
#     string = ""
#     # Create a supporting queue, using a simple list
#     queue = []
#     # Start the Node traversal with while loop
#     while True:
#         # assign a current node
#         curr: Node = node 
#         # First extract children to queue
#         if curr.left is not None:
#             queue.append(curr.left)     
#         if curr.right is not None:
#             queue.append(curr.right)
# 
#         # perform the activity on the
#         string += str(curr.value) + ' -> '

def traverse_bfs(node):
    # Create a string that will hold the return value
    string = ""
    # create a queue and push the current node into the queue
    queue = [node]
    # While there is element in this queue, there are nodes to visit
    while len(queue) > 0:
        # pop the 0th element of the queue and assign it as observation node
        observe = queue.pop(0)
        # Do some activity on the node, like reading values or modifying children
        string += str(observe.value) + ' -> '
        # check if there is right child and append it to queue
        if observe.right is not None:
            queue.append(observe.right)
        # check if there is left child and append it to queue
        if observe.left is not None:
            queue.append(observe.left)
    
    print(string)


def traverse_dfs(node):
    string = ""
    stack = [node]
    while len(stack) > 0:
        observer = stack.pop(0)
        string += str(observer.value) + " -> "

        if observer.right is not None:
            stack.insert(0, observer.right)

        if observer.left is not None:
            stack.insert(0, observer.left)

    print(string)


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f

# Checking the Nodes output
# print(a)
# print(b)
# print(c)

# traverse_bfs(a)  # a -> c -> b -> d -> f -> e
#       a
#      / \
#     b   c
#    /   / \
#   d    e  f

traverse_dfs(a)  # a -> b -> d -> c -> e -> f