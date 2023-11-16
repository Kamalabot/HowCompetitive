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

ll1.append(a)
ll1.append(b)
ll1.append(c)
ll1.append(d)
ll1.append(e)
ll1.append(f)

print_ll(a)