# Pattern: Fast & Slow Pointers
# Introduction: The Fast & Slow Pointers (Tortoise and Hare) pattern is used to detect cycles in linked lists and other
# similar structures.

# Sample Problem: Detect if a linked list has a cycle.
# Input: head = [3, 2, 0, -4], pos = 1
# Output: True (cycle exists)

# intuition 1: moving the nodes by 1 or 2 nodes is controlled by next attr
# intuition 2: looping of the nodes are controlled by the fast node
# intuition 3: if slow becomes same as fast, then there is cycle.

# Example Implementation:
class ListNode:
    # creating the list node with val & next
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    slow, fast = head, head
    # assign head to both slow and fast
    while fast and fast.next:
        # till the fast and fast.next node are not null
        slow = slow.next
        # move slow to just its next
        fast = fast.next.next
        # move fast next node of its next
        if slow == fast:
            # idea is if slow becomes equal to fast then there is cycle
            return True
    return False


# Creating a linked list: [3 -> 2 -> 0 -> -4]
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Linking the nodes together
node1.next = node2
node2.next = node3
node3.next = node4

# Creating a cycle: -4 -> 2 (node4.next = node2)
node4.next = node2

head = node1

print(hasCycle(head))
# LeetCode Problems:
# - Linked List Cycle (LeetCode #141)
# - Happy Number (LeetCode #202)
# - Find the Duplicate Number (LeetCode #287)
