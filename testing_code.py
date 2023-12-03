# practicing to implement the queue class, 
# using the node objects
from typing import List, Any
import logging

praclog = logging.getLogger('prac_log')
praclog.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
prform = logging.Formatter(fmt='%(message)s - %(levelname)s - %(asctime)s', 
                           datefmt='%b-%d')
handler.setFormatter(prform)
praclog.addHandler(handler)


class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

    def __str__(self) -> str:
        return str(self.value)


class Queue:
    def __init__(self, node: Node) -> None:
        # Queue with a node can be initialized
        self.node = node

    def __str__(self):
        # declare container var
        container = ''
        # declare curr node & assign first node to it
        curr = self.node
        # add curr node value to container
        container = str(curr.value)
        # start iterating until there is next node
        while curr.next is not None:
            # make the next node as curr
            curr = curr.next
            # add the node value to container
            container += ' =>' + str(curr.value)
        # after iterating return the container
        return container


def contains(node, check: str | int):
    """Checks all nodes of the queue,
    and returns True if value is present
    else returns false"""
   # check if node is None, return False 
    if node is None:
        return False
    # check if node value is equal to check
    if node.value == check:
        praclog.info(f'checking {node.value}')
        return True
    # recursively call this function with next node
    return contains(node.next, check)


def reverse(node: Node):
    """Takes a linked list of Nodes and reverses"""
    # if curr node is none, then list is empty, so return empty string 
    if node is not None:
    # declare a prev variable
        prev = None
    # declare node to curr variable
        curr = node
    # as that will be the head
    if curr.next is None:
        return curr.value
    # assign given node to prev
    prev = node
    # make the next node of the curr node as curr
    curr = curr.next
    # proceeding further assign, next node of given node as prev
    curr.next = prev
    # call self with curr
    reverse(curr)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# praclog.info(a)
# qq1 = Queue(['a', 'b', 'c', 'd', 'e', 'f'])
qq1 = Queue(a)
praclog.info(qq1)  # a => b => c => d => e => f
praclog.info(contains(a, 'f'))  # True
praclog.info(contains(a, 'it'))  # False
# praclog.info(qq1.pop())  # a
# praclog.info(qq1)  # b => c => d => e => f