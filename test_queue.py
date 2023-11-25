# file is for practicing the linkedlist implementation and traversal
# recursive reverse and delete is still pending

import logging

# for a change use the basic logger
logging.basicConfig(filemode='w', filename='linklog.log',
                    datefmt="%b-%d | %H:%M",
                    format='%(message)s | %(asctime)s | %(levelname)s',
                    level=logging.INFO,
                    force=True)

# testing the logging
# logging.info("info is recorded")
# logging.warning("warning is recorded")
# logging.critical("critical is recieved")

# implementing linked-list with the nodes


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def _print_rec(start: Node):
    """Static method used by the print_rec for traversing the 
    Linkedlist recursively"""
    # create a string variable to hold the results
    # string = ""
    if start is None:
        return ''
    # create a return statement with value of start + " => " + values that is
    # recursively attached by calling _print_rec with start.next
    return start.value + " => " + _print_rec(start.next)


def reverse_list(start: Node):
    """Iteratively reversing the linked list which has start node"""
    # assign prev and curr
    prev = None
    curr = start
    # iteratively loop while curr is not none
    while curr is not None:
        # create a next variable and assign it to curr.next
        next = curr.next
        # assign curr.next variable to prev
        curr.next = prev
        # assign curr to prev
        prev = curr
        # assign next variable as curr
        curr = next
        # continue
    return prev


def append_node(start: Node, newNode: Node):
    """Append newNode to a list starting at start node"""
    # Start by looking at the start node
    # if start's next is None
    if start.next is None:
        # make start's next as newNode
        start.next = newNode
    
    # Traverse all the way to the end and find the last node
    # observe the start node
    observer = start  # A
    # as long as observer's next is not none keep looping
    while observer.next is not None:
        # assign observer to temp
        temp = observer  # D
        # assign observer's next to observer
        observer = observer.next  # E
    # entire list has been traversed, and temp is last node
    logging.info(f"Checking the obserer node {observer.value}") 
    # assign the newNode as temp's Next
    observer.next = newNode
    # print the entire list
    logging.info(f"printing full list after append: {_print_rec(start)}")


def delete_node(start: Node, delNode: Node):
    """Delete a node from a linked list with start node"""
    # if the start node is delNode
    if start == delNode:
        start = None
        start.next = None
        return 'List is empty'
    # assign start node as prev
    prev: Node = start  # A
    # observe the start's next node
    observe: Node = start.next  # B
    # as long as observe's next node is not None
    while observe.next is not None:  # C
        # check if observe is delNode, and detach it from list
        if observe.value == delNode.value: # B
            # assign prev's next node, 
            prev.next = observe.next
            # return delete completion
            return f"Node with {observe.value} value has been deleted"
        # continue by assigning observe to prev
        prev = observe
        # assign observe's next to observe
        observe = observe.next
    return 'Node not in list'


def append_rec(start: Node, newNode: Node):
    # if start's next is None
    if start.next is None:
        # log the last node
        logging.info(f"value of last node is: {start.value}")
        # assign newNode to start's next
        start.next = newNode
        # return
        return
    # test the recursive stack
    logging.info(f"value in stack is: {start.value}")
    # call self with start.next and newNode 
    append_rec(start.next, newNode)

# The following nodes are created

A = Node('a')
B = Node('b')
C = Node('c')
D = Node('d')
E = Node('e')

# the above nodes are connected by assigning it to the next attribute

A.next = B
B.next = C
C.next = D
D.next = E


# logging.info(_print_rec(E))  # should print only e

# logging.info(reverse_list(A).value)  # should return e

# logging.info(_print_rec(E))  # should return the reverse of the list

F = Node('f')
I = Node('i')

# append_node(start=A, newNode=F)  # prints temp value and full list a to f
# 
# delete_node(start=A, delNode=E)  # d has been deleted
# 
# logging.info(_print_rec(start=A))  # a => b => c => e
# 
# logging.info(delete_node(start=A, delNode=I))  # d has been deleted

append_rec(start=A, newNode=F)  # prints temp value and full list a to f

logging.info(_print_rec(start=A))