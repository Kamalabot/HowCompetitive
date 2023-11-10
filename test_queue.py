# implementing queue from start

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class Linkedlist:

    def __init__(self) -> None:
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
            return

        cur = self.head

        while cur.next is not None:
            cur = cur.next

        # Same value is assigned in two different
        cur.next = Node(val)

    def print(self):
        cur = self.head 
        string = str(cur.val)
        while cur.next is not None:
            cur = cur.next 
            string += '->' + str(cur.val)
        print(string)


ll = Linkedlist()
ll.append('a')
ll.append('b')
ll.append('c')

ll.print()