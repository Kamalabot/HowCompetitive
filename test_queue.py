# implementing linked list. There are 2 ways to implement the LList, 
# and 3 seperate functions for search, delete and reverse

class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.next = None 


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def append(self, val: Node):
        if self.head is None:
            self.head = val
            return

        LinkedList._append(val, self.head)

    @staticmethod
    def _append(val, curr):
        if curr.next is None:
            curr.next = val
            return
        LinkedList._append(val, curr.next)

    def containsr(self, val):
        if self.head is None:
            return False
        
    def _containsr(val, head):


    def contains(self, val):
        curr = self.head
        while curr is not None:
            if curr.val == val:
                return True
            curr = curr.next
        return False


def print_list(head: Node) -> None:
    string = ""
    curr = head

    while curr is not None:
        string += str(curr.val) + "->"
        curr = curr.next

    print(string)

ll1 = LinkedList()

a = Node('a')
b = Node('b')
c = Node('c')

ll1.append(a)
ll1.append(b)
ll1.append(c)

print_list(a)

print(ll1.contains('c'))
print(ll1.contains('ac'))
