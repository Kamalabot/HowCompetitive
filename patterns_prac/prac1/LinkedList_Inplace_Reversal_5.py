# Pattern: LinkedList In-place Reversal
# Introduction: The In-place Reversal of a LinkedList pattern reverses parts of a linked list without using extra space.

# Sample Problem: Reverse a sublist of a linked list from position m to n.
# Input: head = [1, 2, 3, 4, 5], m = 2, n = 4
# Note the position is absolute
# Output: [1, 4, 3, 2, 5]

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# intuition is create and assign the new node
# to curr.next and then move curr to curr.next
def create_linked_list(head):
    dummy = ListNode(0)  # not to worry,  this will be discarded
    curr = dummy
    for val in head:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next  # the next node is returned


# intuition 1: the last node will have next node as None
# intuition 2: there are multiple node movements that require
# visual understanding


def create_ll(in_list):
    dummy = ListNode(0)
    curr = dummy
    for i in in_list:
        # assign the new node to curr.next
        curr.next = ListNode(i)
        curr = curr.next
    return dummy.next


def print_ll(head):
    if head is None:
        return "empty"
    curr = head
    string = ""

    while curr:
        string += str(curr.val) + " -> "
        curr = curr.next
    print(string)


# head = [1, 2, 3, 4, 5]
# m = 2
# n = 4

# print("creating and printing the LinkedList from head")
# l_head = create_ll(head)
# print_ll(l_head)


# intuition 3: In order to successfully reverse,
# Example Implementation:
def reverseBetween(head, m, n):
    if not head:
        return None  # no list so none

    dummy = ListNode(0)  # dummy node has to be created
    dummy.next = head
    prev = dummy  # why not assign directly ListNode(0) here?
    # neded to access prev.next so needed the dummy node

    for _ in range(m - 1):
        # travese the list up to m
        print(f"first for loop: {prev.val} \n")
        prev = prev.next
        # this is the starting point after traversal

    reverse = None  # initiate reverse linkedlist

    curr = prev.next

    # we are moving the curr to m index
    for _ in range(n - m + 1):
        # if prev:
        #     print(f"Reversing loop next value: {prev.val} \n")
        # if curr:
        #     print(f"Reversing loop curr value: {curr.val} \n")
        # if reverse:
        #     print(f"Reversing loop reverse value: {reverse.val} \n")
        # iterate over the range
        # curr's prev, and curr's next node needs to
        # be connected properly, as shown below
        next = curr.next
        curr.next = reverse
        reverse = curr
        # this will Assigned None at beginning
        curr = next
    # why are we doing it?
    prev.next.next = curr
    prev.next = reverse
    return dummy.next  # effectively we are returning reverse
    # through dummy, why?


def reverse_prac(head):
    if head is None:
        return None

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(m - 1):
        prev = prev.next

    curr = prev.next
    reverse = None

    for _ in range(n - m - 1):
        next = curr.next
        curr.next = reverse
        reverse = curr
        curr = next

    prev.next.next = curr
    prev.next = reverse
    return dummy.next


# Print the result

nums = [1, 2, 3, 4, 5]
m = 2
n = 4

input_head = create_linked_list(head=nums)

print("printing input linked list\n")
while input_head:
    print(input_head.val, end=" ")
    input_head = input_head.next
    print("\n")
# beware the above process will make the input_head to None
# copying also wont work

input_head = create_linked_list(head=nums)

rev_head = reverseBetween(input_head, m, n)

print("printing output linked list\n")
while rev_head:
    print(rev_head.val, end=" ")
    rev_head = rev_head.next

# LeetCode Problems:
# - Reverse Linked List (LeetCode #206)
# - Reverse Linked List II (LeetCode #92)
# - Swap Nodes in Pairs (LeetCode #24)
