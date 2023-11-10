# Implementing Linked Lists iteratively 
from typing import Union

class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def __str__(self):
        return self.val


# class LinkedList:
# 
#     def __init__(self) -> None:
#         self.head = None
# 
#     def append(self, val):
#         if self.head is None:
#             self.head = Node(val)
#             return
#         cur = self.head
# While there is cur.next then make the current as current.next 
#         while cur.next is not None:
#             cur = cur.next
# Same val is assigned in two different locations in memory
# And it is assigned to head 
#         cur.next = Node(val)
# 
#     def print(self):
#         string = ""
#         cur = self.head
#         while cur is not None:
#             string += cur.val + "->"
#             cur = cur.next  # This is key step 
#  
#         print(string)

# Corrected print method 
#     def print(self):
        cur = self.head 
        string = str(cur.val)
        while cur.next is not None:
            cur = cur.next 
            string += '->' + str(cur.val)
        print(string) 

#     def contains(self, val):
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

        return str(curr.val) +  "->" + LinkedList._print(curr.next)
    
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

a = Node(11)
b = Node(10)
c = Node(6)
d = Node(-6)

a.next = b
b.next = c
c.next = d 

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


def deleteValue(head: Node, val: int | str | float) -> bool:
    if head.val == val:
        return head.next.val

    _deleteValue(head, None, val)
    return head.val


def _deleteValue(curr: Node, prev: Node, val: int | str | float) -> bool:
    # check the order of the base cases 
    if curr is None:
        return
    if curr.val == val:
        prev.next = curr.next
        return

    _deleteValue(curr.next,  curr, val)


def print_list(head):
    curr = head
    if curr is None:
        return ""

    return str(curr.val) + " + " + print_list(curr.next)


print(print_list(a))  # 11 + 10 + 6 + -6
print(deleteValue(a, 10))  # 11
print(print_list(a))  # 11 + 6 + -6
print(deleteValue(a, -6))  # 11
print(print_list(a))  # 11 + 6 +
print(deleteValue(a, 11))  # 6