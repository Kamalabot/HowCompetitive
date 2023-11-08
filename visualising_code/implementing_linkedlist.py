# Implementing Linked Lists iteratively 

class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def __str__(self):
        return self.val


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = Node(val)

    def print(self):
        str = ""
        cur = self.head
        while cur is not None:
            str += cur.val + "->"
            cur = cur.next  # This is key step 
 
        print(str)

    def contains(self, val):
        cur = self.head 
        while cur is not None:
            if cur.val == val:
                return True

            cur = cur.next
        
        return False


ll1 = LinkedList()

ll1.append('a')
ll1.append('b')
ll1.append('c')
ll1.append('d') # new tail

ll1.print()

print(ll1.contains('x'))
print(ll1.contains('y'))
print(ll1.contains('a'))
print(ll1.contains('c'))

# Implementing LinkedList recursive 


class LinkedList:

    def __init(self):
        self.head = None

    def append(self, val):
        if self.head == None:
            self.head = Node(val)

    @staticmethod
    def _append(val, curr):
        if curr.next == None:
            curr.next = Node(val)
            return 
        _append(val, curr.next)