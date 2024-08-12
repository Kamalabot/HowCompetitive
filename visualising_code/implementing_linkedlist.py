# Implementing Linked Lists iteratively
from typing import Union


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)  # only string has to be returned


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, newNode: Node) -> None:
        """Append the new node to end of the list"""
        # check if the head is none
        if self.head is None:
            # yes, then make the newNode as head
            self.head = newNode
            # inform user that, the node is the head
            print(f"{newNode.value} is the head")
            # return out
            return
        # create observer variable and assign it self.head
        observer = self.head
        # while observer.next is not None
        while observer.next is not None:
            # Then assign observer.next to observer
            observer = observer.next
        # Break out of while loop when next node becomes none
        # assign newNode to observer.next
        observer.next = newNode
        # Inform user the append is completed
        print(f"{newNode.value} node has been appended after {observer.value}")

    def rec_append(self, val):
        """Appends the value directly into the Linked list"""
        # if head is none
        if self.head is None:
            # then attach the Node
            self.head = Node(val)
            print(f"Appending {val} to head of list...")
            return
        # call the recursive append function with val and head
        LinkedList._rec_append(val, self.head)

    # Need to recursively call the function
    @staticmethod
    def _rec_append(val, curr):
        # check if the curr node doesn't have next node
        if curr.next is None:
            # yes then append new node in place of curr.next
            curr.next = Node(val)
            # inform the user where the new node is appended
            print(f"Appending {val} after {curr.value}")
            # Return to caller
            return
        # current node has next node, call "self" with next node
        LinkedList._rec_append(val, curr.next)

    def rec_print(self):
        """Prints the values of the list"""
        # Call the recursive print function
        return LinkedList._rec_print(self.head)

    @staticmethod
    def _rec_print(node):
        """Prints the value of the node and calls self recursively"""
        # check if node is none
        if node is None:
            # then return as empty list
            return "end..."
        # append the value of node to the recursive call with next node
        return str(node.value) + " -> " + LinkedList._rec_print(node.next)


def print_ll(start: Node) -> None:
    """Given head of a linkedlist print the rest of the list"""
    # create variable called string to hold the output
    string = ""
    # assign start to the current node, use it as reference
    curr = start
    # while the next element of current node is not none
    while curr.next is not None:
        # append the value of the curr node to the string
        string += str(curr.value) + " -> "
        # assign the next node to curr
        curr = curr.next
    # append last node value to string
    string += str(curr.value)
    # print the final string variable
    print(string)


#   def contains(self, val):
#         cur = self.head
#         while cur is not None:
#             if cur.val == val:
#                 return True
#
#             cur = cur.next
#
#         return False
#
#
# ll1 = LinkedList()
#
# ll1.append('a')
# ll1.append('b')
# ll1.append('c')
# ll1.append('d') # new tail
#
# ll1.print()
#
# print(ll1.contains('x'))
# print(ll1.contains('y'))
# print(ll1.contains('a'))
# print(ll1.contains('c'))

# Implementing LinkedList recursive


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        # Calling the static method
        LinkedList._append(val, self.head)

    @staticmethod
    def _append(val, curr):
        if curr.next is None:
            curr.next = Node(val)
            return

        LinkedList._append(val, curr.next)

    def print(self):
        output = LinkedList._print(self.head)
        print(output)

    @staticmethod
    def _print(curr):
        if curr is None:
            return ""

        return str(curr.val) + "->" + LinkedList._print(curr.next)

    def contains(self, val):
        return LinkedList._contains(self.head, val)

    @staticmethod
    def _contains(curr, val):
        if curr is None:
            return False
        if curr.val == val:
            return True

        return LinkedList._contains(curr.next, val)


ll1 = LinkedList()
#
# ll1.append('a')
# ll1.append('b')
# ll1.append('c')
# ll1.append('d') # new tail
#
# print("this ref: ", ll1.head)
# print("second ref: ", ll1.head.next)
# print("third ref: ", ll1.head.next.next)
#
# ll1.print()
#
# print(ll1.contains('x')) # False
# # print(ll1.contains('y'))
# print(ll1.contains('a')) # True
# # print(ll1.contains('c'))

# Implementing the function that returns the sum of values of the linked list

# ll1.append(11)
# ll1.append(7)
# ll1.append(10)
# ll1.append(2)
#
# ll1.print() # 11 -> 7 -> 10 -> 2
#
# def sum_list(lhead: Node):
#     curr = lhead
#     sum = 0
#     while curr is not None:
#         sum += curr.val
#         curr = curr.next
#
#     return sum


def sum_list(lhead: Node):
    if lhead is None:
        return 0

    return lhead.val + sum_list(lhead.next)


# print(sum_list(ll1.head))

# Implement the Linked List Deletion


def delete_by_loop(llist, val):
    if llist.head is None:
        return
    # create curr, prev
    curr = llist.head
    prev = None
    # check if the head val is to be
    # deleted
    if llist.head.val == val:
        llist.head = llist.head.next
        # simply assign the head to head.next
        return
    # start traversing with curr
    while curr is not None:
        # check if curr val is to be deleted
        if curr.val == val:
            # print('here')
            # connect prev's next to curr's next
            prev.next = curr.next
        # print(curr.val)
        prev = curr  # make curr as prev
        curr = curr.next  # make next as curr
    return


# def deleteValue(head: Node, val: int | str | float) -> bool:
#     curr = head
#     prev = None
#
#     if head.val == val:
#         return head.next.val
#
#     while curr is not None:
#         if curr.val == val:
#             prev.next = curr.next
#         prev = curr
#         curr = curr.next
#         # print(f"prev {prev.val}")
#         # print(f"curr {curr.val}")
#
#     return head.val


def deleteValue(head: Node, val: int | str | float) -> Node:
    """delete the node containing the value and return it"""
    if head.val == val:
        return head.next
    # call the recursive function
    _deleteValue(head, None, val)
    return head


def _deleteValue(curr: Node, prev: Node, val: int | str | float) -> Node:
    # check the order of the base cases
    # there are 3 args entering the recursive function, how to decide these?
    # check if current node is None
    if curr is None:
        return  # simply return None
    # proceed and check if current node value is equal to value
    if curr.val == val:
        # direct the prev node's next to current node's next, deleting current node
        prev.next = curr.next
        return  # return None
    # call self with next node of the current, current and value to be deleted
    _deleteValue(curr.next, curr, val)


def print_list(head):
    curr = head
    if curr is None:
        return ""

    return str(curr.val) + " + " + print_list(curr.next)


a = Node(11)
b = Node(10)
c = Node(6)
d = Node(-6)

a.next = b
b.next = c
c.next = d

# print(print_list(a))  # 11 + 10 + 6 + -6
# print(deleteValue(a, 10))  # 11
# print(print_list(a))  # 11 + 6 + -6
# print(deleteValue(a, -6))  # 11
# print(print_list(a))  # 11 + 6 +
# print(deleteValue(a, 11))  # 6

# def reverseList(head: Node):
#     """Iterative solution with help of while loop"""
#     prev = None
#     curr = head
#
#     while curr is not None:
#         next = curr.next  # temp variable to hold the next node
#         curr.next = prev
#         prev = curr
#         curr = next
#
#     return prev


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


def reverseList(head: Node, prev: Node = None):
    """Recursive solution"""
    # check if head is None, when the list is empty or
    # it is made None by below logic
    if head is None:
        # return prev, which can be None in 1st call
        # or be the final node, that is returned as head
        return prev
    # assign the next node of head node, to next variable
    next = head.next
    # direct the next node of the head node to prev node
    head.next = prev
    # call self with new next and head, in place of head and prev nodes
    return reverseList(next, head)


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


print("***Before Reverse****")
print(print_list(a))
new_head = reverseList(a)
print("***After Reverse****")
print(print_list(new_head))
