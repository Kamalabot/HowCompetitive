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
    for i in head:
        curr.next = ListNode(i)
        curr = curr.next

    return dummy.next


def reverseBetween(head: ListNode, m, n):
    if not head:
        return None  # no list so none

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(m - 1):
        print("First for loop: {prev.val}")
        prev = prev.next
    # 1 -> 2 -> 3 -> 4 -> 5
    reverse = None
    # will start at 3
    curr = prev.next

    for _ in range(n - m + 1):
        # next will point at 4
        next = curr.next
        # 3 will point back to None
        curr.next = reverse
        # reverse is point at 3
        reverse = curr
        # curr is pointing at 4
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
