# file is for practicing the linkedlist implementation and traversal
# Append, delete and recursive reverse is still pending

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


class Linkedlist:
    """Class is implemented to provide a set of methods that work on
    a linked list. The object is instantiated with head node of the
    linkedlist"""
    def __init__(self) -> None:
        self.head = None
    
    def print_all(self):
        """prints all the elements of the linkedlist by traversing iteratively"""
        if self.head is None:
            return 'Empty List'
        # create a variable to hold the result
        string = ""
        # make the head as observed
        observed = self.head
        # start loop the linkedlist, as long as next attr of observed
        # is not None
        while observed is not None:
            # attach value of head to the string
            string += str(observed.value) + " => "
            # make the next node as observed
            observed = observed.next
        # exit while loop once observed becomes None            
        # return the built string
        return string
    
    def print_rec(self):
        """prints all the elements of the linkedlist by traversing recursively"""
        # return the result of the _rec_print function result
        return Linkedlist._print_rec(self.head)

    @staticmethod
    def _print_rec(start: Node):
        """Static method used by the print_rec for traversing the 
        Linkedlist recursively"""
        # create a string variable to hold the results
        # string = ""
        if start is None:
            return ''
        # create a return statement with value of start + " => " + values that is
        # recursively attached by calling _print_rec with start.next
        return start.value + " => " + Linkedlist._print_rec(start.next)

#     def reverse_list(self):
#         """Method reverses the linkedlist in place iteratively"""
#         # check if the linkedlist is populated
#         if self.head is None:
#             # return empty list
#             return 'empty list'
#         # create a prev node with None value
#         prev = None
#         # make the next node of head node as observed
#         observed = self.head.next
#         # start the loop on linkedlist as long as observed is not None
#         while observed is not None:
#             # make the observed_node next 
#             next_node.next = observed
#             # make the observed node next to point to prev 
#             observed.next = prev


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


# linked list is instantiated with a given head node
ll1 = Linkedlist()
ll1.head = A

ll2 = Linkedlist()

# checking the print_all method

# logging.info(ll1.print_all())  # a => b => c => d => e =>
# logging.info(ll2.print_all())  # EmptyList

# logging.info(ll1.print_rec())  # a => b => c => d => e =>
# logging.info(ll2.print_rec())  # EmptyList

logging.info(reverse_list(A).value)

# linked list has not changed... Why?
logging.info(ll1.print_all())