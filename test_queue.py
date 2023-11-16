# Practice script for implementing the Linked list representation as nodes
# and operating on the linked list. The major operations are printing the 
# list elements, checking if an element is present in the list,
# reversing the entire list and deleting the list

class Node:
    def __init__(self, value) -> None:
        self.value: str | int = value
        self.next: Node = None

    def __str__(self):
        return str(self.value)


# class LinkedList:
#     # Instantiate a LinkedList Object
#     def __init__(self, start) -> None:
#         # assign the head with start node
#         self.head = start
# 
#     def print(self) -> None:
#         """Prints the elements of the linked list"""
#         # Check if the linked list head is none
#         if self.head is None:
#             # Yes. Then return. There is nothing to print 
#             return
#         # Create a variable string, to hold the output
#         string = ""
#         # Assign the head to observer variable
#         observer = self.head
#         # While the observer is not none,
#         while observer is not None:
#             # do the operation with the observer
#             string += str(observer.value) + ' -> '
#             # assign observer's next to observer
#             observer = observer.next
# 
#         print(string)

class LinkedList:
    def __init__(self) -> None:
        self. head = None

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
            # print(f"Appending {val} to head of list...")
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
            # print(f"Appending {val} after {curr.value}")
            # Return to caller
            return
        # current node has next node, call "self" with next node 
        LinkedList._rec_append(val, curr.next)

    def rec_contains(self, val):
        """Checks each node and returns true if val is present in list"""
        return LinkedList._rec_contains(val, self.head)

    @staticmethod        
    def _rec_contains(val, node):
        """Calls its recursively with the next nodes if available"""
        # If reached end of the list
        if node is None:
            # means the value is not in the list
            return False
        # If node's value is equal to val
        if node.value == val:
            # return True
            return True
        # Call "self" with next node
        return LinkedList._rec_contains(val, node.next)
    
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
        return str(node.value) + ' -> ' + LinkedList._rec_print(node.next)


# def del_linkedlist(node: Node) -> None: 
def del_linkedlist(mylist: LinkedList) -> None: 
    """Recursively deletes elements in the entire list""" 
    # check if the node is none
    node = mylist.head
    print(mylist.rec_print())
    if node is None:
        print("empty list...")
        return
    # check if next node is not none 
    if node.next is not None:
        # assign node to prev variable
        prev = node
        # inform the user the node connection is cut
        print(f"{prev.value} is disconnected from {node.next.value}")
        # cut the connection of prev to the next node
        prev.next = None
        # make the head's next node as the head
        mylist.head = node.next
        # show the new list
        print(mylist.rec_print())

    # call the function with updated mylist
    return del_linkedlist(mylist)  


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


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
 
# print_ll(a)  # a -> b -> c -> d -> e -> f

# ll1 = LinkedList(a)

# ll1.print()  # a -> b -> c -> d -> e -> f

ll1 = LinkedList()
ll2 = LinkedList()

# ll1.append(a)
# ll1.append(b)
# ll1.append(c)
# ll1.append(d)
# ll1.append(e)
# ll1.append(f)

ll1.rec_append('a')
ll1.rec_append('b')
ll1.rec_append('c')
ll1.rec_append('d')
ll1.rec_append('e')
ll1.rec_append('f')

# print(ll1.rec_contains('f'))  # True
# print(ll1.rec_contains('tf'))  # False

# print(ll1.rec_print())  # a -> b -> c -> d -> e -> f
# print_ll(a)

del_linkedlist(ll2)  # empty list 
del_linkedlist(ll1)  # list deleted