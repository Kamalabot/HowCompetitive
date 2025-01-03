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
    dummy = ListNode(0)
    curr = dummy
    for val in head:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


# intuition 1: the last node will have next node as None
# intuition 2: there are multiple node movements that require
# visual understanding
# intuition 3: curr is the head, through prev.next


# Example Implementation:
def reverseBetween(head, m, n):
    if head is None:
        return None

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(m - 1):
        prev = prev.next

    reverse = None
    curr = prev.next

    for _ in range(n - m + 1):
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
# beware the above process will make the input_head to None
# copying also wont work

print("\n")

input_head = create_linked_list(head=nums)

rev_head = reverseBetween(input_head, m, n)

print("printing output linked list\n")
while rev_head:
    print(rev_head.val, end=" ")
    rev_head = rev_head.next

print("\n")
# LeetCode Problems:
# - Reverse Linked List (LeetCode #206)
# - Reverse Linked List II (LeetCode #92)
# - Swap Nodes in Pairs (LeetCode #24)
