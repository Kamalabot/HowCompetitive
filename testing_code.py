# implementing binary Trees with Nodes
import logging

dfslog = logging.getLogger(__name__)
dfslog.setLevel(logging.INFO)
dfshnd = logging.StreamHandler()
dfshnd.setLevel(logging.INFO)
dform = logging.Formatter(fmt='%(message)s | %(asctime)s', datefmt='%d-%b | %H:%M')
dfshnd.setFormatter(dform)
dfslog.addHandler(dfshnd)


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.value)


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

A.right = B
A.left = C
B.right = D
C.right = E
C.left = F


def print_elem_dfs(start: Node):
    # if the node is None
    if start is None:
        return 'empty tree'
    # declare variable to hold final value
    string = ''
    # declare stack
    stack = []
    # push start node into stack
    stack.insert(0, start)
    # as long as there is element in stack
    while len(stack) > 0:
        # pop the top element
        curr = stack.pop()
        # do operation on the element
        string += str(curr.value) + ' -> '
        # check if right node is present
        if curr.right is not None:
            # push the element on to the stack
            stack.insert(0, curr.right)
        # check for left node 
        if curr.left is not None:
            stack.insert(0, curr.left) 
    # return the string value
    return string

# def print_elem_rec_dfs(start):
#     # if start is None
#     if start is None:
#         # return None
#         return
#     # do operation with a var
#     string = [str(start.value)]
#     # call self using start.right
#     string.append(print_elem_rec_dfs(start.right))
#     # call self using start.left
#     string.append(print_elem_rec_dfs(start.left))
#     # return string
#     return string


def print_elem_rec_dfs(start):
    # if start is None
    if start is None:
        # return None
        return
    # do operation with a var
    print(start.value)
    # call self using start.right
    print_elem_rec_dfs(start.right)
    # call self using start.left
    print_elem_rec_dfs(start.left)
    # return nothing 


def print_elem_rec_dfs_post(start):
    # if start is None
    if start is None:
        # return None
        return
    # call self using start.right
    print_elem_rec_dfs_post(start.right)
    # call self using start.left
    print_elem_rec_dfs_post(start.left)
    # do operation with a var
    print(start.value)
    # return nothing 


def print_elem_rec_dfs_in(start):
    # if start is None
    if start is None:
        # return None
        return
    # call self using start.right
    print_elem_rec_dfs_in(start.right)
    # do operation with a var
    print(start.value)
    # call self using start.left
    print_elem_rec_dfs_in(start.left)
    # return nothing 


# dfslog.info(print_elem_dfs(A))  # A -> B -> D -> C -> E -> F
# dfslog.info(print_elem_rec_dfs(A))  # A -> B -> D -> C -> E -> F   got ['A', ['B', ['D', None, None], None], ['C', ['E', None, None], ['F', None, None]]]
print_elem_rec_dfs(A)  # A B D C E F
print("********")
print_elem_rec_dfs_post(A)  # A B D C E F  D B E F C A
print("^*^^*^^*^*^^*^*")
print_elem_rec_dfs_in(A)  # A B D C E F  D B A E C F
