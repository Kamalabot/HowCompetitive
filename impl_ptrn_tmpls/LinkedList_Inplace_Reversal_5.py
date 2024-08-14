# Pattern: LinkedList In-place Reversal
# Introduction: The In-place Reversal of a LinkedList pattern reverses parts of a linked list without using extra space.

# Sample Problem: Reverse a sublist of a linked list from position m to n.
# Input: head = [1, 2, 3, 4, 5], m = 2, n = 4
# Output: [1, 4, 3, 2, 5]

# Example Implementation:
def reverseBetween(head, m, n):
    if not head:
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

# LeetCode Problems:
# - Reverse Linked List (LeetCode #206)
# - Reverse Linked List II (LeetCode #92)
# - Swap Nodes in Pairs (LeetCode #24)
